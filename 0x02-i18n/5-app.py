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


app.config.from_object('5-app.Config')


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """ GET
    return: 5-index.html
    """
    return render_template('5-index.html')


@babel.localeselector
def get_locale() -> str:
    """ determines the best match with the supported language"""
    # check if locale parameter exiets
    if request.args.get("locale"):
        locale = request.args.get("locale")
        if locale in app.config['LANGUAGES']:
            return locale
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


if __name__ == "__main__":
    app.run()
