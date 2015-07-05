'''
Created on Jun 27, 2015

@author: Andrew
'''
from flask import render_template, request, redirect, url_for, flash
from flask.ext.login import login_required, current_user
from pony.orm.core import db_session

from matchMeUp import app, db
from matchMeUp.models.arguments import RatingEnum

from matchMeUp.services.user_service import UserService
from matchMeUp.services.match_service import MatchService


user_service = UserService(db)
match_service = MatchService(db)


@app.route('/match/profiles', methods=['GET'])
@db_session
@login_required
def profile_requests():
    return render_template(
            'match/profile_queue.html',
            next_prospect=match_service.get_next_profile_prospect(current_user)
    )


@app.route('/match/profiles', methods=['POST'])
@db_session
@login_required
def do_profile_requests():
    prospect_id = int(request.form['prospect_id'])
    prospect = user_service.get_user(prospect_id)
    from_user = user_service.get_user(current_user.id)

    rating_arg = request.form['rating']
    try:
        rating_enum = RatingEnum[rating_arg]
        match_service.rate_attractiveness(from_user, prospect, rating_enum)
    except TypeError:
        flash('Invalid rating: {}'.format(rating_arg))

    return redirect(url_for('profile_requests'))


@app.route('/match/contacts', methods=['GET'])
@db_session
@login_required
def contact_requests():
    from_user = user_service.get_user(current_user.id)

    if from_user.is_contact_slot_available():
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
    prospect_id = int(request.form['prospect_id'])
    prospect = user_service.get_user(prospect_id)
    from_user = user_service.get_user(current_user.id)
    request_contact = bool(int(request.form['request_contact']))

    if request_contact:
        match_service.request_contact(from_user, prospect)
    else:
        match_service.block_user(from_user, prospect)

    return redirect(url_for('contact_requests'))
