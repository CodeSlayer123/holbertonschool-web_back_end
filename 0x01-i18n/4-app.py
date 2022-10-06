#!/usr/bin/env python3

"""task 4 flask app.py"""
from flask import Flask, escape, request, render_template, session
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
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """gets the locale"""
    language = request.args.get("locale")
    if (language):
        if (language in Config.LANGUAGES):
            return language
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
