'''
Created on Jul 11, 2015

@author: Andrew
'''


class ProfileService():

    def __init__(self, db):
        self._db = db

    def _get_about(self, user):
        return user.about or self._db.UserAbout(user=user)

    def set_about_section(self, user, label, value):
        data = {label: value}
        self._get_about(user).set(**data)
        return value

    def set_about(
            self, user, summary, interests, with_life, spare_time,
            diet_restrictions):
        data = {
                'summary': summary,
                'interests': interests,
                'doing_with_life': with_life,
                'in_spare_time': spare_time,
                'diet_restrictions': diet_restrictions}

        about = self._get_about(user)
        about.set(**data)

    def set_employment_data(self, user, employment_status_enum, occupation):
        data = {
                'status': employment_status_enum.name,
                'occupation': occupation}

        if user.employment:
            user.employment.set(**data)
        else:
            user.employment = self._db.UserEmployment(user=user, **data)

    def set_contact_prefs(
            self, user, first_name, shyness, message_tips, convo_ideas):
        data = {
                'first_name': first_name,
                'shyness': shyness,
                'message_tips': message_tips,
                'convo_ideas': convo_ideas}

        if user.contact_prefs:
            user.contact_prefs.set(**data)
        else:
            user.contact_prefs = self._db.ContactPrefs(user=user, **data)
