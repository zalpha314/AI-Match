'''
Created on Jun 26, 2015

@author: Andrew
'''
from datetime import date, datetime

from pony.orm import Required, Optional, LongStr, Set

from matchMeUp.models.qualities import (
        UserLevel, ConnectionStatusEnum, GenderEnum, EmploymentStatusEnum,
    LookingForEnum, ExclusivityEnum, SmokesEnum, DrugsEnum, DrinksEnum,
    HasKidsEnum, LivingWithEnum)


def _get_scale():
    return Required(int, size=8, unsigned=True, min=1, max=10)


def define_entities(db):

    class User(db.Entity):
        # Required Security
        email = Required(str, unique=True)
        pw_hash = Required(str)
        username = Required(str, unique=True)
        authenticated = Optional(bool)
        user_level = Required(int)

        # Required Profile
        birth_date = Required(date)
        gender = Required(str)
        gps_lat = Required(float)
        gps_lon = Required(float)

        last_activity = Required(datetime)

        photos = Set("Photo")

        # Other Categories
        about = Optional('UserAbout')
        seeking = Optional("Seeking")
        employment = Optional('UserEmployment')
        attractions = Set('UserAttraction')
        my_deal_breakers = Optional('MyDealBreakers')
        match_deal_breakers = Optional('MatchDealBreakers')

        # compatability = Optional("Compatability")
        contact_prefs = Optional("ContactPrefs")

        # ratings
        ratings_in = Set('Rating', reverse='to_user')
        ratings_out = Set('Rating', reverse='from_user')

        # Connections
        connected_to = Set('User', reverse='connected_to')
        connections = Set('Connection', reverse='users')
        requests_out = Set('Connection', reverse='requester')

        # Messages
        message_threads = Set('MessageThread', reverse='users')
        messages_out = Set('Message', reverse='from_user')
        messages_in = Set('Message', reverse='to_user')

        ''' Required by Flask-login '''
        def is_authenticated(self):
            return self.authenticated

        ''' Required by Flask-login '''
        def is_active(self):
            return True

        ''' Required by Flask-login '''
        def is_anonymous(self):
            return False

        ''' Required by Flask-login '''
        def get_id(self):
            return self.id

        def get_age(self):
            born = self.birth_date
            today = date.today()
            return (
                    today.year -
                    born.year -
                    ((today.month, today.day) < (born.month, born.day))
                    )

        def is_admin(self):
            return self.user_level >= UserLevel.admin.value

        def get_main_photo(self):
            for photo in self.photos:
                return photo

        def get_gender(self):
            return GenderEnum[self.gender]

        def get_attractions(self):
            return [GenderEnum[i.gender] for i in self.attractions]

    class UserAbout(db.Entity):
        user = Required(User)

        summary = Optional(LongStr)
        interests = Optional(LongStr)
        doing_with_life = Optional(LongStr)
        in_spare_time = Optional(LongStr)
        diet_restrictions = Optional(LongStr)

    class Photo(db.Entity):
        user = Required(User)

        file_name = Required(str)
        description = Optional(str)
        order = Required(int, size=8, unsigned=True)  # TODO, unused

        def get_url(self):
            return '/images/photos/{0}/{1}'.format(self.user.id, self.id)

    class Seeking(db.Entity):
        user = Required(User, reverse='seeking')

        looking_for = Required(str)
        exclusivity = Required(str)
        years_above = Required(int)
        years_below = Required(int)

        def get_min_years_below(self):
            return self.user.get_age() - 18

        def get_min_age(self):
            return self.user.get_age() - self.years_below

        def get_max_age(self):
            return self.user.get_age() + self.years_above

        def get_looking_for(self):
            return LookingForEnum(self.looking_for)

        def get_exclusivity(self):
            return ExclusivityEnum(self.exclusivity)

    class UserEmployment(db.Entity):
        user = Required(User)

        status = Required(str)
        occupation = Optional(str)

        def get_status(self):
            return EmploymentStatusEnum[self.status]

    class UserAttraction(db.Entity):
        user = Required(User)
        gender = Required(str)

    class MyDealBreakers(db.Entity):
        user = Required(User)

        smokes = Required(str)
        drugs = Required(str)
        drinks = Required(str)
        has_kids = Required(str)
        living_with = Required(str)

        def get_smokes(self):
            return SmokesEnum[self.smokes]

        def get_drugs(self):
            return DrugsEnum[self.drugs]

        def get_drinks(self):
            return DrinksEnum[self.drinks]

        def get_has_kids(self):
            return HasKidsEnum[self.has_kids]

        def get_living_with(self):
            return LivingWithEnum[self.living_with]

    class MatchDealBreakers(db.Entity):
        user = Required(User)

        smokes = Set('SmokesDealbreaker')
        drugs = Set('DrugsDealbreaker')
        drinks = Set('DrinksDealbreaker')
        has_kids = Set('HasKidsDealbreaker')
        living_with = Set('LivingWithDealbreaker')

        def get_smokes(self):
            return [SmokesEnum[i.smokes] for i in self.smokes]

        def get_drugs(self):
            return [DrugsEnum[i.drugs] for i in self.drugs]

        def get_drinks(self):
            return [DrinksEnum[i.drinks] for i in self.drinks]

        def get_has_kids(self):
            return [HasKidsEnum[i.has_kids] for i in self.has_kids]

        def get_living_with(self):
            return [LivingWithEnum[i.living_with] for i in self.living_with]

    class SmokesDealbreaker(db.Entity):
        deal_breakers = Required(MatchDealBreakers)
        smokes = Required(str)

    class DrugsDealbreaker(db.Entity):
        deal_breakers = Required(MatchDealBreakers)
        drugs = Required(str)

    class DrinksDealbreaker(db.Entity):
        deal_breakers = Required(MatchDealBreakers)
        drinks = Required(str)

    class HasKidsDealbreaker(db.Entity):
        deal_breakers = Required(MatchDealBreakers)
        has_kids = Required(str)

    class LivingWithDealbreaker(db.Entity):
        deal_breakers = Required(MatchDealBreakers)
        living_with = Required(str)

    '''
    class Pets(db.Entity):
        compatability = Required("Compatability")

        has = Required(bool)
        pet = Required(str)


    class Compatability(db.Entity):
        user = Required(User)

        demeanour = _get_scale()
        dominance = _get_scale()
        ambition = _get_scale()
        independence = _get_scale()
        confidence = _get_scale()
        tidiness = _get_scale()
        sex_positivity = _get_scale()
        activity = _get_scale()
        affection = _get_scale()
        adventurousness = _get_scale()
        # desire for kids
        # maturity

        likes_pets = Set(Pets)
    '''

    class ContactPrefs(db.Entity):
        user = Required(User, reverse='contact_prefs')

        first_name = Optional(str)
        shyness = _get_scale()
        message_tips = Required(LongStr)
        convo_ideas = Required(LongStr)

    class Rating(db.Entity):

        from_user = Required(User, reverse='ratings_out')
        to_user = Required(User, reverse='ratings_in')
        rating = Required(bool)

        @classmethod
        def create(cls, from_user, to_user, rating_bool):
            return cls(
                from_user=from_user, to_user=to_user, rating=rating_bool)

    class Connection(db.Entity):

        users = Set(User)
        requester = Optional(User)
        status = Required(int)

        @classmethod
        def create(cls, user1, user2):
            return cls(
                users=[user1, user2],
                status=ConnectionStatusEnum.no_interaction.value)

        def set_status(self, status_enum):
            self.status = status_enum.value
            self.requester = None

        def get_status(self):
            return ConnectionStatusEnum(self.status)

        def get_other(self, user):
            for u in self.users:
                if u != user:
                    return u

    class MessageThread(db.Entity):
        messages = Set('Message', reverse='thread')
        users = Set('User', reverse='message_threads')

    class Message(db.Entity):
        thread = Set(MessageThread, reverse='messages')
        from_user = Required(User)
        to_user = Required(User)
        text = Required(LongStr)
        sent_on = Required(datetime)
        read = Optional(bool)

    db.generate_mapping(check_tables=True, create_tables=True)
