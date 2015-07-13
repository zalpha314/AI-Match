'''
Created on Jul 12, 2015

@author: Andrew
'''
from flask import render_template, request, redirect
from flask.ext.login import login_required
from pony.orm.core import db_session

from matchMeUp import app, db
from matchMeUp.controllers import get_current_user
from matchMeUp.models.qualities import (
        LookingForEnum, ExclusivityEnum, GenderEnum, SmokesEnum, DrugsEnum,
        DrinksEnum, HasKidsEnum, LivingWithEnum)
from matchMeUp.services.match_settings_service import MatchSettingsService


service = MatchSettingsService(db)


@app.route('/match/settings', methods=['GET'])
@db_session
@login_required
def match_settings():
    return render_template(
            'match/settings.html',
            attraction_options=GenderEnum,
            looking_for_options=LookingForEnum,
            exclusivity_options=ExclusivityEnum,
            smokes_options=SmokesEnum,
            drugs_options=DrugsEnum,
            drinks_options=DrinksEnum,
            has_kids_options=HasKidsEnum,
            living_with_options=LivingWithEnum
            )


@app.route('/match/settings/seeking', methods=['POST'])
@db_session
@login_required
def set_match_settings_seeking():
    # Update Attractions
    my_attractions = request.form.getlist('attracted-to')
    my_attractions_enum = [GenderEnum[name] for name in my_attractions]
    service.set_attracted_to(get_current_user(), my_attractions_enum)

    # Update other seeking data
    looking_for_enum = LookingForEnum[request.form['looking-for']]
    exclusivity_enum = ExclusivityEnum[request.form['exclusivity']]
    num_years_below = request.form['years-below']
    num_years_above = request.form['years-above']
    service.set_seeking(
            get_current_user(), looking_for_enum, exclusivity_enum,
            num_years_below, num_years_above)

    return redirect(request.referrer)


@app.route('/match/settings/dealbreakers/mine', methods=['POST'])
@db_session
@login_required
def set_match_settings_my_dealbreakers():
    smokes_enum = SmokesEnum[request.form['smokes']]
    drugs_enum = DrugsEnum[request.form['drugs']]
    drinks_enum = DrinksEnum[request.form['drinks']]
    has_kids_enum = HasKidsEnum[request.form['has-kids']]
    living_with_enum = LivingWithEnum[request.form['living-with']]

    service.set_own_deal_breakers(
            get_current_user(), smokes_enum, drugs_enum, drinks_enum,
            has_kids_enum, living_with_enum)

    return redirect(request.referrer)


@app.route('/match/settings/dealbreakers/match', methods=['POST'])
@db_session
@login_required
def set_match_settings_match_dealbreakers():
    smokes_enums = [SmokesEnum[i] for i in request.form.getlist('smokes')]
    drugs_enums = [DrugsEnum[i] for i in request.form.getlist('drugs')]
    drinks_enums = [DrinksEnum[i] for i in request.form.getlist('drinks')]
    has_kids_enums = [HasKidsEnum[i] for i in request.form.getlist('has-kids')]
    living_with_enums = [
            LivingWithEnum[i]
            for i in request.form.getlist('living-with')]

    service.set_match_deal_breakers(
            get_current_user(), smokes_enums, drugs_enums, drinks_enums,
            has_kids_enums, living_with_enums)

    return redirect(request.referrer)
