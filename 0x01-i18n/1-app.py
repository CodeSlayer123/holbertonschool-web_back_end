#!/usr/bin/env python3

"""task 1 flask app.py"""
from flask import Flask, escape, request, render_template
from flask_babel import Babel, gettext

app = Flask(__name__)

babel = Babel(app)


class Config():
    """the config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config())


@app.route('/', methods=['GET'], strict_slashes=False)
def startup():
    """renders 0-index html page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
