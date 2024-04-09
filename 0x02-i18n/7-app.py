#!/usr/bin/env python3
"""Define locale selector for babel"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
import pytz

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config():
    """
    Configuration for some flask variables
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config())


@babel.localeselector
def get_locale():
    """Get locale from request headers"""

    lc = request.args.get('locale', None)
    lng = app.config['LANGUAGES']
    if lc and lc in lng:
        return lc

    if 'user' in g:
        if g.user is not None:
            lc = g.user['locale']
            return lc

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """mock a user login"""
    user_login = request.args.get('login_as', None)
    if user_login is not None:
        user = users.get(int(user_login), None)
        if user is None:
            return None
        return user
    return None


@app.before_request
def load_user():
    if 'user' not in g:
        g.user = get_user()
    return g.user


@babel.timezoneselector
def get_timezone():
    """check timezone"""
    lc = request.args.get('timezone', None)
    if lc:
        try:
            pytz.timezone(lc)
            return lc
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if 'user' in g:
        if g.user is not None:
            lc = g.user['timezone']
            try:
                pytz.timezone(lc)
                return lc
            except pytz.exceptions.UnknownTimeZoneError:
                pass
        
@app.route('/')
def home():
    """Home route"""
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run()
