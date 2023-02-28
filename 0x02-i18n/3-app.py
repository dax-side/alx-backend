#!/usr/bin/env python3
""" instatiates a Babel object"""
from flask import (
        Flask,
        render_template,
        request
        )
from flask_babel import Babel
from os import getenv

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ babel configuration sets default
    """
    LANGUAGES = ["en", "fr"]

    # Defaults language and timezone
    BABEL_DAFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object('3-app.Config')


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """ GET
    return: 3-index.html
    """
    return render_template('3-index.html')


@babel.localeselector
def get_locale() -> str:
    """ determines the best match with the supported language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
