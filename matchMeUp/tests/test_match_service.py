'''
Created on Jul 5, 2015

@author: Andrew
'''
import unittest

from pony.orm.core import db_session

from matchMeUp.models.arguments import RatingEnum
from matchMeUp.models.qualities import ConnectionStatusEnum
from matchMeUp.services.match_service import MatchService
from matchMeUp.tests import db
from matchMeUp.tests.seed_db import SeedDb

service = MatchService(db)
seeder = SeedDb(db)


class TestMatchService(unittest.TestCase):

    @db_session
    def setUp(self):
        seeder.seed()

    @db_session
    def tearDown(self):
        for user in db.User.select():
            user.delete()

    #########
    # Tests #
    #########

    @db_session
    def test_profile_prospects_get_next(self):
        self._get_users()

    @db_session
    def test_profile_prospects_not_at_all_rating(self):
        u1, u2 = self._get_users()
        service.rate_attractiveness(u1, u2, RatingEnum.notAtAll)
        self._check_connection(u1, u2, ConnectionStatusEnum.blocked)

    @db_session
    def test_profile_prospects_no_rating(self):
        u1, u2 = self._get_users()
        service.rate_attractiveness(u1, u2, RatingEnum.no)
        self._check_connection(u1, u2, ConnectionStatusEnum.blocked)

    @db_session
    def test_profile_prospects_yes_rating(self):
        u1, u2 = self._get_users()
        service.rate_attractiveness(u1, u2, RatingEnum.yes)
        self._check_connection(u1, u2, ConnectionStatusEnum.profile_requested)

    @db_session
    def test_profile_prospects_very_rating(self):
        u1, u2 = self._get_users()
        service.rate_attractiveness(u1, u2, RatingEnum.very)
        self._check_connection(u1, u2, ConnectionStatusEnum.profile_requested)

    @db_session
    def test_reject_profile_request(self):
        u1, u2 = self._get_users()
        service.rate_attractiveness(u1, u2, RatingEnum.very)
        service.rate_attractiveness(u2, u1, RatingEnum.no)
        self._check_connection(u1, u2, ConnectionStatusEnum.blocked)

    @db_session
    def test_accept_profile_request(self):
        self._get_contacts()

    @db_session
    def test_no_contact_request(self):
        u1, u2 = self._get_profile_contacts()
        service.block_user(u1, u2)
        service.rate_attractiveness(u1, u2, RatingEnum.yes)
        service.rate_attractiveness(u2, u1, RatingEnum.very)

    @db_session
    def test_make_contact_request(self):
        u1, u2 = self._get_profile_contacts()
        service.request_contact(u1, u2)
        self._check_connection(u1, u2, ConnectionStatusEnum.contact_requested)

    @db_session
    def test_reject_contact_request(self):
        u1, u2 = self._get_profile_contacts()
        service.request_contact(u1, u2)
        self._check_connection(u1, u2, ConnectionStatusEnum.contact_requested)

    @db_session
    def test_accept_contact_request(self):
        self._get_contacts()

    @db_session
    def test_end_contact(self):
        u1, u2 = self._get_contacts()
        service.block_user(u2, u1)
        self._check_connection(u1, u2, ConnectionStatusEnum.blocked)

    ###########
    # Helpers #
    ###########

    def _get_users(self):
        u1 = db.User.select()[:1][0]
        u2 = service.get_next_profile_prospect(u1)
        self.assertIsNotNone(u1)
        self.assertIsNotNone(u2)
        self.assertNotEqual(u1, u2)
        self._check_connection(u1, u2, ConnectionStatusEnum.no_interaction)
        return (u1, u2)

    def _get_profile_contacts(self):
        u1, u2 = self._get_users()
        service.rate_attractiveness(u1, u2, RatingEnum.yes)
        service.rate_attractiveness(u2, u1, RatingEnum.very)
        self._check_connection(u1, u2, ConnectionStatusEnum.profile_access)
        return (u1, u2)

    def _get_contacts(self):
        u1, u2 = self._get_profile_contacts()
        service.request_contact(u1, u2)
        service.request_contact(u2, u1)
        self._check_connection(u1, u2, ConnectionStatusEnum.in_contact)
        return (u1, u2)

    def _check_connection(self, user1, user2, status_enum):
        connection = service._get_connection(user1, user2)
        self.assertIs(connection.get_status(), status_enum)

if __name__ == '__main__':
    unittest.main()
