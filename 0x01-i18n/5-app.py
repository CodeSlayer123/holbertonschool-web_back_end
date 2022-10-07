#!/usr/bin/env python3

"""task 5 flask app.py"""
from flask import Flask, escape, request, render_template, session
from flask_babel import Babel
import flask
app = Flask(__name__)

babel = Babel(app)


class Config():
    """the config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app.config.from_object(Config())


@app.route('/', methods=['GET'], strict_slashes=False)
def startup():
    """renders 0-index html page"""
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    """gets the locale"""
    language = request.args.get("locale")
    if (language):
        if (language in Config.LANGUAGES):
            return language
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """gets the user"""
    user_id = request.args.get("login_as")
    if (user_id):
        user = users.get(int(user_id))
        if (user):
            return user
    return None


@app.before_request
def before_request():
    """is called before request"""
    flask.g.user = get_user()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
