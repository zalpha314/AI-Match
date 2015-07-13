'''
Created on Jul 4, 2015

@author: Andrew
'''
from pony.orm.core import db_session

from matchMeUp import db
from matchMeUp.models.arguments import RatingEnum
from matchMeUp.models.orm import define_entities
from matchMeUp.models.qualities import (
        GenderEnum, UserLevel, LookingForEnum, ExclusivityEnum,
        EmploymentStatusEnum)
from matchMeUp.services.match_service import MatchService
from matchMeUp.services.match_settings_service import MatchSettingsService
from matchMeUp.services.profile_service import ProfileService
from matchMeUp.services.user_service import UserService


class SeedDb():

    def __init__(self, db_in_use):
        define_entities(db_in_use)
        self._user_service = UserService(db_in_use)
        self._profile_service = ProfileService(db_in_use)
        self._match_settings_service = MatchSettingsService(db_in_use)

    def create_user(self, username, gender_enum, birth_date='1991-12-5'):
        user = self._user_service.create_user(
            username,
            '{}@foo.com'.format(username),
            username,
            gender_enum,
            birth_date,
            45.3461463,
            - 75.81246199999998
        )

        # Add Photo
        gender = GenderEnum[user.gender]
        file_name = None
        if gender in (GenderEnum.male, GenderEnum.male_born_as_female):
            file_name = 'blank_male.jpg'
        elif gender in (GenderEnum.female, GenderEnum.female_born_as_male):
            file_name = 'blank_female.jpg'
        else:
            raise ValueError('unhandled gender: {}'.format)
        user.photos.create(file_name=file_name, description='desc', order=1)

        # Fill out sample profile
        self._profile_service.set_about(
                user, 'My Summary', 'cuddling, skiing',
                'Just graduated and started my first job!', 'Watch TV',
                'Don\'t like Peanuts!')
        self._match_settings_service.set_seeking(
                user, LookingForEnum.relationship, ExclusivityEnum.yes, 3, 3)
        self._profile_service.set_contact_prefs(
                user, username, 7, 'Don\'t be a creep',
                'I can\'t stop talking about Star Wars!')
        self._profile_service.set_employment_data(
                user, EmploymentStatusEnum.full_time, 'Slave')

        return user

    @db_session
    def seed(self):
        andrew = self.create_user('andrew', GenderEnum.male)
        andrew.user_level = UserLevel.admin.value

        self.create_user('claire', GenderEnum.female)
        self.create_user('jessica', GenderEnum.female)
        self.create_user('miranda', GenderEnum.female)
        self.create_user('khaled', GenderEnum.male)
        self.create_user('jennifer', GenderEnum.female)
        self.create_user('stacie', GenderEnum.female)

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
