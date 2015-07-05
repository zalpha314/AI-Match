'''
Created on Jul 4, 2015

@author: Andrew
'''
from pony.orm.core import db_session

from matchMeUp import db
from matchMeUp.models.orm import define_entities
from matchMeUp.models.qualities import Gender
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

    def seed(self):
        with db_session:
            self.create_user('andrew', Gender.male)
            self.create_user('claire', Gender.female)
            self.create_user('jessica', Gender.female)
            self.create_user('miranda', Gender.female)
            self.create_user('khaled', Gender.male)
            self.create_user('jennifer', Gender.female)
            self.create_user('stacie', Gender.female)


if __name__ == '__main__':
    print('Seeding database')
    SeedDb(db).seed()
    print("Done seeding'")
