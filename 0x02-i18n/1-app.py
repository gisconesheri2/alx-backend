#!/usr/bin/env python3
"""
start up a babel instance
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config():
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config())

babel = Babel(app)


@app.route('/')
def home():
    return render_template('1-index.html')
