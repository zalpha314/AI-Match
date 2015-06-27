# AI-Match

#Introduction

This app focuses on matching people for dating and relationships.  It is somewhat of a mix between Tinder and OkCupid, trying to cultivate the benefits of each, while staying away from the downsides.

Tinder is great because you both have to "like" each other in order to get into contact, but it is very shallow, has very little filtering, and some people abuse the system by "liking" everyone, or by cultivating large contact lists for a confidence boost with no intention to meet or even talk with any of them.  This app uses the benefits by requiring users to mutually "like" each other in order to get into contact, but sets a hard limit on the number of people you can actually be in contact with at any one time, so every contact has their time to shine without having to worry too much about being played.

OkCpuid ius great because there are so many categories of compatability you can look at to find the perfect match, you are given a handy match score to make it even easier, and the most attractive people are hidden from you unless you are voted into their league.  The downside is that you have so many choices all at once, popular people will be bombarded with messages from anyone with very little filtering, and you have no guarantee that people will have the slightest inclination to respond to your messages.  This app will attempt to find your match scores with other people using a series of compatability questions.  Your matches will be prioritized first by compatability, and then by proximity to your attractiveness.  By requiring both users to "like" each other before getting into contact, you can be more confident that your contacts will respond to your messages, and put more individual effort into each of your first messages to get off to a better start.

# Profile MetaData
- Can change filter settings once a day

Base
- Birthdate (filterable by age range)
- Gender (male, female, male born as female, female born as male)
- Postal Code (filterable by distance, bus time, or drive time)
- Ocupation (Unemployed, Student, Part-Time, Full-Time, Retired)

Seeking
- Attracted to (multi-select gender identity) (matched to relavent type)
- Looking For (Relationship, Dates but no commitment, Friend with Benefits)
- Priority (Seriously, Casualy) (affects compatability score ?)
- Monogamy (Monogomous, Neutral, Promiscuous) (neutral can be matched to any type)
- Relationship Status (Single, In a Relationship, Married)

Dealbreakers (must also choose what is acceptable)
- Smokes (yes, occasionally, no)
- Drugs (yes, "soft" only, no)
- Drinks (often, socially, rarely, no)
- Has Kids (Yes, Yes but over 18, No)
- Wants Kids (Yes, Maybe, No)
- Residence Situation (With Family, With Roommate(s), Alone)
- BMI (enter as number, does not appear in profile, filterable by category multi-select)

Compatibility (affects compatability score, you must choose your ideal partner's traits)
- Demeanour (1 to 10 from serious to calm to wild)
- Dominance (1 to 10 from Submissive to Balanced to Dominant)
- Ambition (1 to 10 from Unambitious to Ambitious)
- Independence (1 to 10 from Reclusive to Reliant)
- Confidence (1 to 10 from Unconfident to Confident)
- Tidiness (1 to 10 from Messy to Tidy)
- Sex-Positivity (1 to 10 from traditional to free) (marriage to love to stable relationship to comfortable to first date)
- Likes Pets (Cats, Dogs, Birds, Other) multi

About
- Introduction
- Interests (comma-seperated)
- What I'm doing with my Life
- What I like to do in my spare time

About Meta
- Dietary Restrictions (free text, or find database with list to choose from)
- Has Pets (multi same as Likes Pets) 

Contact Meta (show only when in contact)
- Shyness (1 to 10 from shy to outgoing)
- How I like to be messaged
- Some ideas for conversation topics

# Match Game

## Step 1: Request Profile (Rate Attractiveness by: Not At All, No, Yes, Very)
  - Ratings on you affect your hidden attractiveness level
    - you start at 0.5, and anyone within 0.3 of you is in your league
  - Everyone in your league that matches your filters is queued
    - Ordered based on similar attractiveness level, if you have already been liked, and compatability perferences 
  - You cannot see what someone has rated you
  - Rating Yes or Very will queue them for Step 2
## Step 2: Request Contact (View Profile and ask to get in contact with: Yes, No)
  - Order based on if you have already been liked, and compatability preferences
  - You can only play if you have open contact slots
  - You must wait 30 seconds on a profile before you can request contact
## Step 3: Request Pending
  - If you both request contact, and:
     - the other person has an empty contact slot, you will be put in contact
     - the other person does not have an empty contact slot, you will both be be "queued"
## Step 3.5: Queued
  - you will have to wait until you both have an open slot to get in contact
  - you cannot see who you are queued to talk to
## Step 4: In Contact
  - you only have 3 contact slots available (you will see this counter)
    - You must end contact with someone to get another contact
    - If you have not received a message, you must wait 24 hours until you can end contact
## Step 4: End Contact
  - You must give reason(s) to end contact (that they will see)
    - If you did not respond to their first message
    - If you responded to their first message
  
  
# Technologies
- Python
- Flask
- Database: MySQL or PostgreSQL
- ORM: SQLAlchemy or Alembic
  
