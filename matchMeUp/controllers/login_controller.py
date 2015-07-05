'''
Created on Jun 27, 2015

@author: Andrew
'''
from datetime import date, datetime, timedelta

from flask import render_template, request, redirect, url_for, flash
from flask.ext.login import login_required
from validate_email import validate_email
from pony.orm.core import db_session

from matchMeUp import app, login_manager, db
from matchMeUp.models.qualities import Gender
from matchMeUp.services.user_service import UserService

##############
# Attributes #
##############

user_service = UserService(db)

MINIMUM_AGE = 18
DAYS_IN_YEAR = 365

MIN_USERNAME_LENGTH = 6
MIN_PASSWORD_LENGTH = 6

DATE_FORMAT = '%Y-%m-%d'

##################
# Error Messages #
##################

ERROR_USERNAME_LENGTH = (
    'Username must be at least {} characters long'
    .format(MIN_PASSWORD_LENGTH)
)
ERROR_USERNAME_TAKEN = 'That username has already been taken!'
ERROR_PASSWORD_MISMATCH = 'The passwords must match'
ERROR_EMAIL_INVALID = 'Please enter a valid email address'
ERROR_PASSWORD_LENGTH = (
        'Password must be at least {} characters long'
        .format(MIN_PASSWORD_LENGTH)
)
ERROR_BIRTH_DATE_UNDERAGE = (
        'You must be at least {} to register'
        .format(MINIMUM_AGE)
)


#############
# Endpoints #
#############

@app.route('/')
@db_session
@login_required
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET'])
@db_session
def register():
    return render_template(
            'register.html',
            gender_choices=[(g.name, g.value) for g in Gender]
    )


@app.route('/register', methods=['POST'])
@db_session
def doRegister():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    birth_date = datetime.strptime(
            request.form['birth_date'], DATE_FORMAT
    ).date()

    # verify Inputs
    errors = list()
    if len(username) < MIN_USERNAME_LENGTH:
        errors.append(ERROR_USERNAME_LENGTH)
    if user_service.user_exists(username):
        errors.append(ERROR_USERNAME_TAKEN)
    if not validate_email(email):
        errors.append(ERROR_EMAIL_INVALID)
    if len(password) < MIN_PASSWORD_LENGTH:
        errors.append(ERROR_PASSWORD_LENGTH)
    if password != confirm_password:
        errors.append(ERROR_PASSWORD_MISMATCH)
    min_birth_date = date.today() - timedelta(days=DAYS_IN_YEAR * MINIMUM_AGE)
    if birth_date > min_birth_date:
        errors.append(ERROR_BIRTH_DATE_UNDERAGE)

    # Raise Error if any errors recorded
    if errors:
        for error in errors:
            flash(error)
        return redirect(url_for('register'))
    else:
        user = user_service.create_user(username, email, password, birth_date)
        user_service.login_user(user)
        flash('User: {} was created!'.format(user.username))
        return redirect(url_for('index'))


@login_manager.unauthorized_handler
@app.route('/login', methods=['GET'])
@db_session
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
@db_session
def doLogin():
    username = request.form['username']
    password = request.form['password']

    user = user_service.authenticate_user(username, password)
    if user:
        user_service.login_user(user)

        next_url = request.args.get('next')  # FIXME: verify that next is valid
        return redirect(next_url or url_for("index"))

    flash('Incorrect username/password combination')
    return redirect(url_for("login"))


@app.route('/logout', methods=['POST'])
@db_session
@login_required
def doLogout():
    user_service.logout_user()
    return redirect('/')


###########
# Helpers #
###########


@login_manager.user_loader
def load_user(user_id):
    return user_service.get_user(user_id)
