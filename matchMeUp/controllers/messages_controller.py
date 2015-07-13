'''
Created on Jul 5, 2015

@author: Andrew
'''
from flask import request, redirect
from flask.ext.login import login_required, current_user
from flask.templating import render_template
from pony.orm.core import db_session

from matchMeUp import app, db
from matchMeUp.controllers import get_current_user
from matchMeUp.services.connection_service import ConnectionService
from matchMeUp.services.match_service import MatchService
from matchMeUp.services.messages_service import MessagesService
from matchMeUp.services.user_service import UserService


match_service = MatchService(db)
user_service = UserService(db)
connection_service = ConnectionService()
messages_service = MessagesService(db)


@app.route('/messages', methods=['GET'])
@db_session
@login_required
def contacts():
    return render_template(
        'messages/list.html',
        contacts=connection_service.get_contacts(current_user)
        )


@app.route('/messages/<int:contact_id>', methods=['GET'])
@db_session
@login_required
def messages(contact_id):
    user = get_current_user()
    contact = user_service.get_user(contact_id)
    return render_template(
            'messages/show.html',
            contact=contact,
            messages=messages_service.get_messages(user, contact)
            )


@app.route('/messages/<int:contact_id>', methods=['POST'])
@db_session
@login_required
def send_message(contact_id):
    from_user = get_current_user()
    to_user = user_service.get_user(contact_id)
    message_text = request.form['message']
    messages_service.send_message(from_user, to_user, message_text)
    return redirect(request.referrer)
