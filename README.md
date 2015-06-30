MatchMeUp

#Introduction

This app focuses on matching people for dating and relationships.  It is somewhat of a mix between Tinder and OkCupid, trying to cultivate the benefits of each, while staying away from the downsides.

Tinder is great because you both have to "like" each other in order to get into contact, but it is very shallow, has very little filtering, and some people abuse the system by "liking" everyone, or by cultivating large contact lists for a confidence boost with no intention to meet or even talk with any of them.  This app uses the benefits by requiring users to mutually "like" each other in order to get into contact, but sets a hard limit on the number of people you can actually be in contact with at any one time, so every contact has their time to shine without having to worry too much about being played.

OkCpuid ius great because there are so many categories of compatability you can look at to find the perfect match, you are given a handy match score to make it even easier, and the most attractive people are hidden from you unless you are voted into their league.  The downside is that you have so many choices all at once, popular people will be bombarded with messages from anyone with very little filtering, and you have no guarantee that people will have the slightest inclination to respond to your messages.  This app will attempt to find your match scores with other people using a series of compatability questions.  Your matches will be prioritized first by compatability, and then by proximity to your attractiveness.  By requiring both users to "like" each other before getting into contact, you can be more confident that your contacts will respond to your messages, and put more individual effort into each of your first messages to get off to a better start.

# Profile MetaData
- Can change each section (profile or match settings) only once a day, unless otherwise specified

Base
- Birthdate (filterable by age range)
- Gender (male, female, male born as female, female born as male)
- Postal Code (filterable by distance, bus time, or drive time)
- Ocupation (Unemployed, Student, Part-Time, Full-Time, Self-Employed, Retired)

Seeking
- Attracted to (multi-select gender identity) (matched to relavent type)
- Looking for (Relationship, Dates but no commitment, Friend with Benefits, Adventure Buddy, Attention)
- Priority (Seriously, Casualy) (affects compatability score)
- Monogamy (Monogomous, Neutral, Promiscuous) (neutral can be matched to any type)
- Relationship Status (Single, In a Relationship, Married)

Dealbreakers (must also choose what is acceptable)
- Smokes (yes, occasionally, no)
- Drugs (yes, "soft" only, no)
- Drinks (often, socially, rarely, no)
- Has Kids (Yes, Yes but over 18, No)
- Residence Situation (With Family, With Roommate(s), Alone)

Mutual Compatibility (scored bosed on proximity to your own values)
- Tidiness (1 to 10 from Messy to Tidy)
- Sex-Positivity (1 to 10 from traditional to free) (marriage to love to stable relationship to comfortable to first date)
- Affection (1 to 10 from unaffectionate to affectionate)
- Likes Pets (Cats, Dogs, Birds, Other) multi
- Desire for Kids (1 to 10 from No to Maybe to Yes)

Desired Comptatbility (scored based on proximity to your desired values in a match)
- Demeanour (1 to 10 from serious to calm to wild)
- Dominance (1 to 10 from Submissive to Balanced to Dominant)
- Ambition (1 to 10 from Unambitious to Ambitious)
- Independence (1 to 10 from Reclusive to Reliant)
- Confidence (1 to 10 from Unconfident to Confident)
- Activity (1 to 10 from Potato to Athlete)
- Adventurousness (1 to 10 from Unadventurous to Adventurous)

About (can change as often as user likes)
- Introduction
- Interests (comma-seperated)
- What I'm doing with my Life
- What I like to do in my spare time

About Meta
- Dietary Restrictions (free text, or find database with list to choose from)
- Has Pets (multi same as Likes Pets) 

Contact Meta (show only when in contact)
- Contact Initiative (shy, little shy, not shy) and (don't init, sometimes init, do init)
- How I like to be messaged
- Some conversation topic ideas

# Match Game

## Step 1: Request Profile (Rate Attractiveness by: Not At All, No, Yes, Very
  - You are only elegible to start playing when your profile is complete
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
  - You will get a notification when you get a contact or message
## Step 5: End Contact
  - You can only end contact at least 24 hours after your first sent message, 1 hour after receving first message, or by reporting a message
  - You must give reason(s) to end contact (that they will see in a notification)
  - Available reasons if neither ever messaged:
    - impatient and don't have initiative, changed mind about them, Their profile changed and don't like
  - Available reasons if they never messaged:
    - They're ignoring me
  - Available reasons if I never messaged:
    - changed mind about them, Their profile changed and don't like, their message was spammy or copyPasta
  - Available reasons if both have messaged:
    - (boring, don't like, dated but didn't like
  - If no one messages within 72 hours, contact will automatically be ended
    - If no first messages have been sent, revert to profile access
    - If one first message was sent, but recipient has not been online, rever to contact request from sender
    - Otherwise, completely end contact
  

# Reporting
- A user may be reported by another user for:
  - Sexual Profile content, unwarranted sexual message content, or abusive message content
  - Falsified Profile Information (two suspensions
- A user will get two suspensions, and then a ban

Suspensions
  - User's account is locked for 48 hours
  - All contacts and requests are removed and added back to the queue
    - Contacts receive a notification saying their contact was banned, and for what reason

Bans
  - Same as suspension, except:
    - Locked permenately (emails are never removed, so user cannot re-register with same address)

  
  
# Technologies
- Python
- Flask
- Database: MySQL or PostgreSQL
- ORM: SPony ORM
  
