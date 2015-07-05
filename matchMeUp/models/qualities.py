'''
Created on Jun 26, 2015

@author: Andrew
'''
from enum import Enum


class Gender(Enum):
    male = ' Male'
    female = 'Female'
    male_born_as_female = 'Male born as Female'
    female_born_as_male = 'Female born as Male'


class EmploymentStatus(Enum):
    unemployed = 'Unemployed'
    student = 'Student'
    part_time = 'Part-Time'
    full_time = 'Full-Time'
    self_employed = 'Self-Employed'
    retired = 'Retired'


class LookingFor(Enum):
    relationship = 'a Relationship'
    dates = 'Dates, but no commitment'
    adventures = 'an Adventure Buddy'
    fwb = 'a Friend with Benefits'


class Priority(Enum):
    seriously = 'Seriously'
    casualy = 'Casualy'


class Monogamy(Enum):
    mono = 'Monogamous'
    neutral = 'Neutral'
    prom = 'Promiscuous'


class RelationshipStatus(Enum):
    single = 'Single'
    inRelationship = 'In a Relationship'
    married = 'Married'


class Smokes(Enum):
    yes = 'Yes'
    occasionally = 'Occasionally'
    no = 'No'


class Drugs(Enum):
    yes = 'Yes'
    soft = '"Soft" drugs only'
    no = 'No'


class Drinks(Enum):
    excessively = 'Excessively'
    often = 'Often'
    socially = 'Socially'
    rarely = 'Rarely'
    no = 'No'


class HasKids(Enum):
    yes = 'Yes'
    legal = 'Yes, but all over 18'
    no = 'No'


class WantsKids(Enum):
    yes = 'Yes'
    maybe = 'Maybe'
    no = 'No'


class ResidenceSituation(Enum):
    withFamily = 'Living with Family'
    withRoommate = 'Living with Roommate(s)'
    alone = 'Living Alone'


class Pet(Enum):
    cats = 'Cats'
    dogs = 'Dogs'
    birds = 'Birds'
    other = 'Other'


class Religion(Enum):
    non = 'Non-Religious'
    spiritual = 'Spiritual'
    islam = 'Islamic'
    jewish = 'Jewish'
    christian = 'Christian'
    hindu = 'Hindu'
    sikh = 'Sikh'
    other = 'Other'


class ConnectionStatusEnum(Enum):
    no_interaction = 'No Interaction'
    profile_requested = 'Profile Requested'
    profile_access = "Profile Visible"
    contact_requested = 'Contact Requested'
    contact_queued = 'Queued for Contact'
    in_contact = 'In Contact'
    blocked = 'Blocked'


class UserLevel(Enum):
    banned = 1
    suspended = 2
    standard = 3
    moderator = 4
    admin = 5
