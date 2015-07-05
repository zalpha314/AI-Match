'''
Created on Jun 27, 2015

@author: Andrew
'''
from pony.orm.core import count
from matchMeUp.models.arguments import RatingEnum
from matchMeUp.models.qualities import ConnectionStatusEnum

NUM_CONTACT_SLOTS = 1


class MatchService():

    def __init__(self, db):
        self._db = db

    def get_next_profile_prospect(self, user):
        # First search for users that have requested your profile
        results = self._db.Connection.select(
            lambda c:
            user in c.users and
            c.status == ConnectionStatusEnum.profile_requested.value and
            c.requester is not user
        )
        if results.exists():
            users = results[:1][0].users
            return users[0] if users[0] is not user else users[1]

        # Get user that has not requested your profile
        results = self._db.User.select(
            lambda u: u is not user and u not in user.connected_to
        )
        return results[:1][0] if results.exists() else None

    def rate_attractiveness(self, from_user, to_user, rating_enum):
        cncn = self._get_connection(from_user, to_user)

        # Add Rating
        self._db.Rating.create(from_user, to_user, rating_enum)

        # Decide whether to request profile
        if (rating_enum in [RatingEnum.yes, RatingEnum.very]):
            if cncn.get_status() == ConnectionStatusEnum.profile_requested:
                # Grant Profile Access
                cncn.set_status(ConnectionStatusEnum.profile_access)
            else:
                # Make a profile request
                cncn.set_status(ConnectionStatusEnum.profile_requested)
                cncn.requester = from_user
        else:
            self.block_user(from_user, to_user)

    def next_contact_prospect(self, user):
        return self._get
        results = self._db.Connection.select(
            lambda c:
            user in c.users and
            (
                c.status is ConnectionStatusEnum.profile_access or
                (
                    c.status is ConnectionStatusEnum.profile_requested and
                    c.requester is not user
                )
             )
        )
        if results.exists():
            users = results[:1][0].users
            return users[0] if users[0] is not user else users[1]
        return None

    def request_contact(self, from_user, to_user):
        connection = self._get_connection(from_user, to_user)

        if connection.get_status() is ConnectionStatusEnum.contact_requested:
            # Grant Access if exsting reverse-request
            connection.set_status(ConnectionStatusEnum.contact_queued)

            # Try to pop contact from queue
            if (
                    self.is_contact_slot_available(from_user) and
                    self.is_contact_slot_available(to_user)
            ):
                connection.set_status(ConnectionStatusEnum.in_contact)
        else:
            connection.set_status(ConnectionStatusEnum.contact_requested)
            connection.requester = from_user

    def block_user(self, from_user, user_to_block):
        connection = self._get_connection(from_user, user_to_block)
        connection.set_status(ConnectionStatusEnum.blocked)
        connection.requester = from_user

    def get_contacts(self, user):
        contact_connections = self._db.Connection.select(
            lambda c:
            user in c.users and
            c.status is ConnectionStatusEnum.in_contact
        )
        return (c.get_other(user) for c in contact_connections)

    def _get_connection(self, user1, user2):
        for c in user1.connections:
            if user2 in c.users:
                return c

        return self._db.Connection.create(user1, user2)

    def is_contact_slot_available(self, user):
        num_contacts = count(
                c for c in self._db.Connection
                if user in c.users and
                c.status == ConnectionStatusEnum.in_contact.value)
        return num_contacts < NUM_CONTACT_SLOTS
