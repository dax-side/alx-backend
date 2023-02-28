#!/usr/bin/env python3
""" instatiates a Babel object"""
from flask import Flask, render_template
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


app.config.from_object('1-app.Config')


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """ GET
    return: 1-index.html
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
