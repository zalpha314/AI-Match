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

    @db_session
    def test_profile_prospects_get_next(self):
        u1 = db.User.select()[:1][0]
        u2 = service.get_next_profile_prospect(u1)
        self.assertIsNotNone(u1)
        self.assertIsNotNone(u2)

    @db_session
    def test_profile_prospects_not_at_all_rating(self):
        u1 = db.User.select()[:1][0]
        u2 = service.get_next_profile_prospect(u1)
        service.rate_attractiveness(u1, u2, RatingEnum.notAtAll)
        self._check_connection(u1, u2, ConnectionStatusEnum.blocked)

    @db_session
    def test_profile_prospects_no_rating(self):
        u1 = db.User.select()[:1][0]
        u2 = service.get_next_profile_prospect(u1)
        service.rate_attractiveness(u1, u2, RatingEnum.no)
        self._check_connection(u1, u2, ConnectionStatusEnum.blocked)

    @db_session
    def test_profile_prospects_yes_rating(self):
        u1 = db.User.select()[:1][0]
        u2 = service.get_next_profile_prospect(u1)
        service.rate_attractiveness(u1, u2, RatingEnum.yes)
        self._check_connection(u1, u2, ConnectionStatusEnum.profile_requested)

    ###########
    # Helpers #
    ###########

    def _check_connection(self, user1, user2, status_enum):
        connection = service._get_connection(user1, user2)
        self.assertIs(connection.get_status(), status_enum)

if __name__ == '__main__':
    unittest.main()
