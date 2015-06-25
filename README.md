# AI-Match


## Profile MetaData
- Can change filter settings once a day

Base
- Birthdate (filterable by age range)
- Gender (male, female, male born as female, female born as male)
- Postal Code (filterable by distance, bus time, or drive time)
- BMI (as number, does not appear in profile, filterable by category multi-select)
- Ocupation (Unemployed, Student, Part-Time, Full-Time, Retired)

Seeking
- Attracted to (multi-select gender identity)
- Looking For (long-term, short-term, dating but no commitment)
- Intent (serious, casual)
- Monogamy (Monogomous, Neutral, Polygamous)
- Relationship Status (Single, In a Relationship, Married)

Dealbreakers
- Smokes (yes, occasionally, no)
- Drugs (yes, "soft" only, no)
- Drinks (often, socially, rarely, no)
- Has Kids (Yes, Yes but over 18, No)
- Wants Kids (Yes, Maybe, No)

Compatibility
- Demeanour (wild, calm, serious) (may need more research)
- Dominance (Dominant, Somewhat Dominant, Neutral, Somwhat Submissive, Submissive)
- Ambition (Very Ambitious, Ambitious, Unambitious)
- Independence (Reclusive, Independent, Balanced, Dependent, Reliant)
- Confidence (Very Confident, Confident, Neutral, Unconfidant, Very Unconfidant)
- Tidiness (Tidy, Neutral, Messy)
- Residence Situation (With Family, With Roommate(s), Alone)

Additional
- Has Pets (Cats, Dogs, Birds, Other) multi
- But Also Likes (same as above)
- Dietary Restrictions (free text, or find database with list to choose from)

About
- Introduction
- Interests (comma-seperated)
- What I'm doing with my Life
- What I do in my spare time
- Why I'm here
  
# Match Game

## Step 1: Request Profile (Rate Attractiveness by: Not At All, No, Yes, Very)
  - Ratings on you affect your hidden attractiveness level
  - Everyone in your attractiveness league that matches your filters is queued
    - Ordered based on similar attractiveness level, if you have already been liked, and compatability perferences 
  - You cannot see what someone has rated you
  - Rating Yes or Very will queue them for Step 2
## Step 2: Request Contact (View Profile and ask to get in contact with: Yes, No)
  - Order based on if you have already been liked, and compatability preferences
  - You can only play if you have less than X people queued to talk to you
## Step 3: In Contact
  - maximum number of people based on monogomy
    - You must end contact with someone to get another contact
    - If you have not received a message, you must wait 24 hours until you can end contact
  - you see number of people
    - queued to talk to you
    - you are queued to talk to
## Step 4: End Contact
  - You must give reason(s) to end contact (that they will see)
    - If you did not respond to their first message
    - If you responded to their first message
  
  
# Technologies
- Python
- Flask
- Database: MySQL or PostgreSQL
- ORM: SQLAlchemy or Alembic
  
