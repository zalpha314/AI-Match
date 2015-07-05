'''
Created on Jul 5, 2015

@author: Andrew
'''
from flask.ext.login import login_required
from flask.templating import render_template
from pony.orm.core import db_session

from matchMeUp import app, db
from matchMeUp.controllers import admin
from matchMeUp.services.connection_service import ConnectionService
from matchMeUp.services.user_service import UserService


user_service = UserService(db)
connection_service = ConnectionService()


@app.route('/admin/users', methods=['GET'])
@db_session
@login_required
@admin
def list_users():
    return render_template(
        'admin/users/list.html',
        users=user_service.get_users()
    )


@app.route('/admin/users/<int:user_id>/connections', methods=['GET'])
@db_session
@login_required
@admin
def list_connections(user_id):
    user = user_service.get_user(user_id)
    return render_template(
        'admin/users/connections.html',
        user=user,
        profile_contacts=connection_service.get_profile_contacts(user),
        contacts=connection_service.get_contacts(user)
    )
