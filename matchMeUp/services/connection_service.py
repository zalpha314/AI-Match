'''
Created on Jul 5, 2015

@author: Andrew
'''
from enum import Enum

from matchMeUp.models.qualities import ConnectionStatusEnum


class ConnectionFilterEnum(Enum):
    no_filter = 1
    in_only = 2
    out_only = 3

no_filter = ConnectionFilterEnum.no_filter
in_only = ConnectionFilterEnum.in_only
out_only = ConnectionFilterEnum.out_only


class ConnectionService():

    def can_view_profile(self, user, view_user):
        return (
                view_user == user or
                user.is_admin() or
                view_user in self.get_profile_contacts(user) or
                view_user in self.get_contacts(user)
                )

    def get_profile_requests_in(self, user):
        return self._get_connected_user(
            user, ConnectionStatusEnum.profile_requested, in_only)

    def get_profile_requests_out(self, user):
        return self._get_connected_user(
            user, ConnectionStatusEnum.profile_requested, out_only)

    def get_profile_contacts(self, user):
        return self._get_connected_user(
            user, ConnectionStatusEnum.profile_access, no_filter)

    def get_contacts(self, user):
        return self._get_connected_user(
            user, ConnectionStatusEnum.in_contact, no_filter)

    def is_blocked(self, user1, user2):
        return user1 in self._get_connected_user(
                user2, ConnectionStatusEnum.blocked, no_filter)

    def _get_connected_user(self, user, state_enum, filter_enum):
        return (
            c.get_other(user)
            for c in user.connections
            if c.status == state_enum.value and
            (
                (filter_enum == no_filter) or
                (filter_enum == in_only and user is not c.requester) or
                (filter_enum == out_only and user is c.requester)
            )
        )
