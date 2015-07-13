'''
Created on Jun 27, 2015

@author: Andrew
'''
from flask import render_template, request, redirect, url_for, flash
from flask.ext.login import login_required
from pony.orm.core import db_session

from matchMeUp import app, db
from matchMeUp.controllers import get_current_user
from matchMeUp.services.connection_service import ConnectionService
from matchMeUp.services.match_service import MatchService
from matchMeUp.services.user_service import UserService


user_service = UserService(db)
match_service = MatchService(db)
connection_service = ConnectionService()


@app.route('/match/profiles', methods=['GET'])
@db_session
@login_required
def profile_requests():
    user = get_current_user()
    return render_template(
            'match/profile_queue.html',
            next_prospect=match_service.get_next_profile_prospect(user)
    )


@app.route('/match/profiles', methods=['POST'])
@db_session
@login_required
def do_profile_requests():
    prospect_id = int(request.form['prospect_id'])
    prospect = user_service.get_user(prospect_id)
    from_user = get_current_user()

    request_profile = bool(int(request.form['request']))
    match_service.rate_attractiveness(from_user, prospect, request_profile)

    return redirect(url_for('profile_requests'))


@app.route('/match/contacts', methods=['GET'])
@db_session
@login_required
def contact_requests():
    from_user = get_current_user()

    if match_service.is_contact_slot_available(from_user):
        return render_template(
                'match/contact_queue.html',
                next_prospect=match_service.next_contact_prospect(from_user)
        )
    else:
        flash('You already have a contact.  Talk to them!')
        return redirect(url_for('index'))


@app.route('/match/contacts', methods=['POST'])
@db_session
@login_required
def do_contact_request():
    prospect_id = int(request.form['user-id'])
    prospect = user_service.get_user(prospect_id)
    from_user = get_current_user()

    request_contact = bool(int(request.form['request']))
    if request_contact:
        match_service.request_contact(from_user, prospect)
    else:
        match_service.block_user(from_user, prospect)

    return redirect(url_for('contact_requests'))


@app.route('/match/block', methods=['POST'])
@db_session
@login_required
def block():
    # TODO: get reason
    blocker = get_current_user()

    to_block_id = int(request.form['user_id'])
    to_block = user_service.get_user(to_block_id)

    match_service.block_user(blocker, to_block)
    flash('You have blocked {}'.format(to_block.username))
    return redirect(url_for('index'))
