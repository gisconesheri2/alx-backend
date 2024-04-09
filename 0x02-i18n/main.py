#!/usr/bin/env python3
"""Define locale selector for babel"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext


class Config():
    """
    Configuration for some flask variables
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

def get_locale():
    """Get locale from request headers"""
    lc = request.args.get('locale', None)
    lng = app.config['LANGUAGES']

    if lc is None and lc not in lng:
        return request.accept_languages.best_match(app.config['LANGUAGES'])
    return lc

app = Flask(__name__)
babel = Babel(app, locale_selector=get_locale)
app.config.from_object(Config())


def get_locale():
    """Get locale from request headers"""
    lc = request.args.get('locale', None)
    if lc is not None:
        lng = app.config['LANGUAGES']

        if lc in lng:
            return lc
    
    return request.accept_languages.best_match(app.config['LANGUAGES'])
    

@app.route('/')
def home():
    """Home route"""
    lc = request.args.get('locale', None)
    lng = app.config['LANGUAGES']
    print(lc in lng)
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
