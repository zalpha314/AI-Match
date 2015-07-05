'''
Created on Jun 26, 2015

@author: Andrew
'''
from datetime import date, datetime

from pony.orm import Required, Optional, LongStr, Set

from matchMeUp.models.qualities import ConnectionStatusEnum

'''
def _get_scale():
    return Required(int, size=8, unsigned=True, min=1, max=10)
'''


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

        # photos = Set("Photos")

        # Other Categories
        about = Optional('UserAbout')
        # seeking = Optional("Seeking")
        # deal_breakers = Optional("DealBreakers")
        # compatability = Optional("Compatability")
        # contact_prefs = Optional("ContactPrefs")

        # ratings
        ratings_in = Set('Rating', reverse='to_user')
        ratings_out = Set('Rating', reverse='from_user')

        # Connections
        connected_to = Set('User', reverse='connected_to')
        connections = Set('Connection', reverse='users')
        requests_out = Set('Connection', reverse='requester')

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

    class UserAbout(db.Entity):
        user = Required(User)

        # Base
        first_name = Required(str)
        postal_code = Required(str)
        gender = Required(str)
        employed = Required(str)
        occupation = Optional(str)

        # About
        intro = Optional(LongStr)
        interests = Optional(str)
        doingWithLife = Optional(LongStr)
        inSpareTime = Optional(LongStr)
        dietRestrictions = Optional(str)

    '''
    class Photos(db.Entity):
        user = Required(User)

        file_name = Required(str)
        description = Required(str)
        data = Required(bytes)
        order = Required(int, size=8, unsigned=True)


    class AttractedTo(db.Entity):
        seeking = Required("Seeking")
        gender = Required(str)


    class Seeking(db.Entity):
        user = Required(User)

        attracted_to = Set(AttractedTo)
        looking_for = Required(str)
        priority = Required(str)
        monogamy = Required(str)
        relationship_status = Required(str)


    class DealBreakers(db.Entity):
        user = Required(User)

        smokes = Required(str)
        drugs = Required(str)
        drinks = Required(str)
        has_kids = Required(str)
        wants_kids = Required(str)
        residende_situation = Required(str)


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

        likes_pets = Set(Pets)


    class ContactPrefs(db.Entity):
        user = Required(User)

        shyness = _get_scale()
        message_tips = Required(LongStr)
        conversation_ideas = Required(LongStr)
    '''

    class Rating(db.Entity):

        @classmethod
        def create(cls, from_user, to_user, rating_enum):
            return cls(
                from_user=from_user, to_user=to_user, rating=rating_enum.value)

        from_user = Required(User, reverse='ratings_out')
        to_user = Required(User, reverse='ratings_in')
        rating = Required(float)

    class Connection(db.Entity):

        @classmethod
        def create(cls, user1, user2):
            return cls(
                users=[user1, user2],
                status=ConnectionStatusEnum.no_interaction.value)

        users = Set(User)
        requester = Optional(User)
        status = Required(str)

        def set_status(self, status_enum):
            self.status = status_enum.value
            self.requester = None

        def get_status(self):
            return ConnectionStatusEnum(self.status)

        def get_other(self, user):
            users = list(self.users)
            return users[1] if users[0] is user else users[0]

    db.generate_mapping(check_tables=True, create_tables=True)
