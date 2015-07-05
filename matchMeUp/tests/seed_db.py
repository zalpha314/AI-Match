'''
Created on Jul 4, 2015

@author: Andrew
'''
from pony.orm.core import db_session

from matchMeUp import db
from matchMeUp.models.arguments import RatingEnum
from matchMeUp.models.orm import define_entities
from matchMeUp.models.qualities import Gender
from matchMeUp.services.match_service import MatchService
from matchMeUp.services.user_service import UserService


class SeedDb():

    def __init__(self, db_in_use):
        define_entities(db_in_use)
        self._user_service = UserService(db_in_use)

    def create_user(self, username, gender_enum, birth_date='1991-12-5'):
        self._user_service.create_user(
            username,
            '{}@foo.com'.format(username),
            username,
            gender_enum,
            birth_date,
            45.3461463,
            - 75.81246199999998
        )

    @db_session
    def seed(self):
        self.create_user('andrew', Gender.male)
        self.create_user('claire', Gender.female)
        self.create_user('jessica', Gender.female)
        self.create_user('miranda', Gender.female)
        self.create_user('khaled', Gender.male)
        self.create_user('jennifer', Gender.female)
        self.create_user('stacie', Gender.female)

    @db_session
    def seed_connections(self, match_service):
        andrew = self._user_service.get_user('andrew')
        claire = self._user_service.get_user('claire')
        jessica = self._user_service.get_user('jessica')

        # setup profile contact with andrew and claire
        match_service.rate_attractiveness(andrew, claire, RatingEnum.yes)
        match_service.rate_attractiveness(claire, andrew, RatingEnum.very)

        # setup contact with andrew and jessica
        match_service.rate_attractiveness(andrew, jessica, RatingEnum.yes)
        match_service.rate_attractiveness(jessica, andrew, RatingEnum.very)

        match_service.request_contact(andrew, jessica)
        match_service.request_contact(jessica, andrew)


if __name__ == '__main__':
    print('Seeding database')
    seeder = SeedDb(db)
    seeder.seed()
    seeder.seed_connections(MatchService(db))
    print("Done seeding'")
