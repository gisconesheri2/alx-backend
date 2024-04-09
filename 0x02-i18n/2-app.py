from flask import Flask, render_template, request
from flask_babel import Babel

class Config():
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

app = Flask(__name__)
babel = Babel(app, locale_selector=get_locale)
app.config.from_object(Config())


@app.route('/')
def home():
    return render_template('1-index.html')