'''
Created on Jun 26, 2015

@author: Andrew
'''
from enum import Enum


class Quality(Enum):

    def as_dict(self):
        return {'name': self.name, 'value': self.value}

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


class GenderEnum(Quality):
    male = ('Man', 'Men', 'he')
    female = ('Woman', 'Women', 'she')
    male_born_as_female = ('Man born as Woman', 'Men born as Women', 'he')
    female_born_as_male = ('Woman born as Man', 'Women born as Men', 'she')

    def __init__(self, display_name, plural, addressed_as):
        self.display_name = display_name
        self.plural = plural
        self.addressed_as = addressed_as


class EmploymentStatusEnum(Enum):
    unemployed = 'Unemployed'
    student = 'a Student'
    part_time = 'working Part-Time'
    full_time = 'working Full-Time'
    self_employed = 'Self-Employed'
    retired = 'Retired'


class LookingForEnum(Enum):
    relationship = 'a Comitted Relationship'
    dates = 'Dates, but not comitting to anything'
    adventures = 'someone to go on adventures with'
    fwb = 'a Cuddle Buddy or Friend with Benefits'


class ExclusivityEnum(Enum):
    yes = 'Exclusive'
    no = 'Non-Exclusive'


class SmokesEnum(Quality):
    yes = 'Yes'
    occasionally = 'Occasionally'
    no = 'No'


class DrugsEnum(Quality):
    yes = 'Yes'
    soft = '"Soft" drugs only'
    no = 'No'


class DrinksEnum(Quality):
    excessively = 'Excessively'
    often = 'Often'
    socially = 'Socially'
    rarely = 'Rarely'
    no = 'Never'


class HasKidsEnum(Quality):
    yes = 'Yes'
    legal = 'Yes, but all over 18'
    no = 'No'


class LivingWithEnum(Quality):
    with_family = 'Living with Family'
    with_roommate = 'Living with Roommate(s)'
    with_partner = 'Living with a Partner'
    alone = 'Living Alone'


class PetsEnum(Enum):
    cats = 'Cats'
    dogs = 'Dogs'
    birds = 'Birds'
    other = 'Other'


class Religion(Enum):
    non = 'Non-Religious'
    spiritual = 'Spiritual'
    islamic = 'Islamic'
    jewish = 'Jewish'
    christian = 'Christian'
    hindu = 'Hindu'
    sikh = 'Sikh'
    other = 'Other'


class ConnectionStatusEnum(Enum):
    no_interaction = 0
    profile_requested = 1
    profile_access = 2
    contact_requested = 3
    contact_queued = 4
    in_contact = 5
    blocked = 6


class UserLevel(Enum):
    banned = 1
    suspended = 2
    standard = 3
    moderator = 4
    admin = 5
