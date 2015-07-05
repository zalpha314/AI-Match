'''
Created on Jun 27, 2015

@author: Andrew
'''
from datetime import datetime

from passlib.apps import custom_app_context
from flask.ext.login import (login_user, logout_user, current_user)
from pony.orm.core import ObjectNotFound


class UserService():

    def __init__(self, db):
        self._db = db

    def create_user(
                    self, username, email, password, gender_enum, birth_date,
                    gps_lat, gps_lon):
        if self.user_exists(username):
            raise ValueError('username exists')

        pw_hash = custom_app_context.encrypt(password)
        return self._db.User(
            username=username,
            email=email,
            pw_hash=pw_hash,
            birth_date=birth_date,
            gender=gender_enum.value,
            last_activity=datetime.utcnow(),
            gps_lat=gps_lat,
            gps_lon=gps_lon
        )

    def get_user(self, user_id_or_name):
        try:
            if isinstance(user_id_or_name, int):
                return self._db.User[user_id_or_name]
            elif isinstance(user_id_or_name, str):
                return self._db.User.get(username=user_id_or_name)
            raise ValueError(user_id_or_name)
        except ObjectNotFound:
            return None

    def authenticate_user(self, username, password):
        user = self.get_user(username)
        if user and custom_app_context.verify(password, user.pw_hash):
            return user
        return None

    def user_exists(self, username):
        return self.get_user(username) is not None

    def login_user(self, user):
        login_user(user)
        user.authenticated = True

    def logout_user(self):
        current_user.authenticated = False
        logout_user()

    def update_password(self, user, new_password):
        user.pw_hash = custom_app_context.encrypt(new_password)
