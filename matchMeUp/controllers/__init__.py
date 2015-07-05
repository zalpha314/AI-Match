import functools

from flask import redirect, flash
from flask.ext.login import current_user

from matchMeUp.models.qualities import UserLevel


def admin(view):
    @functools.wraps(view)
    def inner(*args, **kwargs):
        if current_user.user_level >= UserLevel.admin.value:
            return view(*args, **kwargs)
        else:
            flash('You do not have sufficient rights to view that page')
            return redirect("/")
    return inner
