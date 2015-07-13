'''
Created on Jul 11, 2015

@author: Andrew
'''
from flask import redirect, request, jsonify, url_for
from flask.ext.login import login_required
from flask.templating import render_template
from pony.orm.core import db_session

from matchMeUp import app, db
from matchMeUp.controllers import get_current_user
from matchMeUp.models.qualities import EmploymentStatusEnum
from matchMeUp.services.connection_service import ConnectionService
from matchMeUp.services.profile_service import ProfileService
from matchMeUp.services.user_service import UserService


connection_service = ConnectionService()
user_service = UserService(db)
profile_service = ProfileService(db)


@app.route('/profile', methods=['GET'])
@db_session
@login_required
def my_profile():
    return redirect('/profile/{}'.format(get_current_user().id))


@app.route('/profile/<int:user_id>', methods=['GET'])
@db_session
@login_required
def profile(user_id):
    user = get_current_user()
    view_user = user_service.get_user(user_id)
    if (
            connection_service.can_view_profile(user, view_user) or
            user.is_admin()
            ):
        return render_template(
                'my_profile.html',
                user=view_user,
                employment_status_options=[i for i in EmploymentStatusEnum]
                )
    return 'You do not have permission to view this profile', 403


@app.route('/profile/about', methods=['POST'])
@db_session
@login_required
def update_profile_section():
    new_value = profile_service.set_about_section(
            get_current_user(),
            request.form['label'],
            request.form['value'])
    return jsonify({'newValue': new_value})


@app.route('/profile/employment', methods=['POST'])
@db_session
@login_required
def update_profile_employment():
    status_enum = EmploymentStatusEnum[request.form['status']]
    occupation = request.form['occupation']
    profile_service.set_employment_data(
            get_current_user(), status_enum, occupation)
    return redirect(url_for('my_profile'))
