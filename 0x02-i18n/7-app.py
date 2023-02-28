#!/usr/bin/env python3
""" instatiates a Bael object"""
from flask import (
        Flask, g,
        render_template,
        request
        )
from flask_babel import Babel
from os import getenv
from typing import Union
from pytz import timezone
import pytz.exceptions

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ babel configuration sets default
    """
    LANGUAGES = ["en", "fr"]

    # Defaults language and timezone
    BABEL_DAFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object('7-app.Config')


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """ GET
    return: 7-index.html
    """
    return render_template('7-index.html')


@babel.localeselector
def get_locale() -> str:
    """ determines the best match with the supported language"""
    # check if locale parameter exiets
    if request.args.get("locale"):
        locale = request.args.get("locale")
        if locale in app.config['LANGUAGES']:
            return locale
    # check for locale in user settings
    elif g.user:
        if g.user['locale']:
            locale = g.user['locale']
            if locale in app.config['LANGUAGES']:
                return locale
    # default locale to return as failsafe
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[dict, None]:
    """ Returns user dict if ID can be found else returns None """
    if request.args.get('login_as'):
        # type cast  the param to int to be able to search the user dict
        user = int(request.args.get('login_as'))
        if user in users:
            return users.get(user)
    else:
        return None


@app.before_request
def before_request():
    """ Finds user if any and sets as global on flask.g.user """
    g.user = get_user()


@babel.timezoneselector
def get_timezone():
    """ infer appropriate time zone"""
    # check if there is a timezone query string
    if request.args['timezone']:
        timezone = request.args['timezone']
        try:
            return timezone(timezone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None
    # check if there is a timezone in a user's settings
    elif g.user and g.user['timezone']:
        try:
            return timezone(g.user['timezone']).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None
    # default to return as a failsafe
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
