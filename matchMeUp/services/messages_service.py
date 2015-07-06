'''
Created on Jul 5, 2015

@author: Andrew
'''
from datetime import datetime


class MessagesService():

    def __init__(self, use_db):
        self._db = use_db

    def _get_message_thread(self, user, with_user):
        user_pair = {user, with_user}
        for thread in user.message_threads:
            if thread.users == user_pair:
                return thread

        # If not thread found, create one
        thread = self._db.MessageThread()
        thread.users.add(user)
        thread.users.add(with_user)
        user.message_threads.add(thread)
        # TODO ensure with_user gets thread too

    def get_messages(self, user, with_user):
        thread = self._get_message_thread(user, with_user)
        if thread.messages:
            return thread.messages.order_by(self._db.Message.sent_on)
        return list()

    def send_message(self, from_user, to_user, message_text):
        thread = self._get_message_thread(from_user, to_user)
        thread.messages.create(
            from_user=from_user,
            to_user=to_user,
            text=message_text,
            sent_on=datetime.now()
        )
