'''
Created on Jul 11, 2015

@author: Andrew
'''
from flask import send_file, flash, request
from flask.ext.login import login_required
from pony.orm.core import db_session

from matchMeUp import app, db
from matchMeUp.controllers import get_current_user
from matchMeUp.services.connection_service import ConnectionService
from matchMeUp.services.user_service import UserService


user_service = UserService(db)
connection_service = ConnectionService()


@app.route('/images/photos/<int:user_id>/<int:photo_id>', methods=['GET'])
@db_session
@login_required
def photo(user_id, photo_id):
    cur = get_current_user()
    user = user_service.get_user(user_id)

    if not connection_service.is_blocked(cur, user):
        for photo in user.photos:
            if photo.id == photo_id:
                return send_file('images/photos/{}'.format(photo.file_name))
    flash('You do not have permission to view that photo')
    return request.referrer, 403


@app.route('/images/photos', methods=['PUT'])
@db_session
@login_required
def put_photo(user_id):
    pass


@app.route('/images/photos/<int:photo_id>', methods=['DELTE'])
@db_session
@login_required
def delete_photo(user_id):
    pass
