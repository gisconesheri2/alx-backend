from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    print(request.args.get('lang', None))
    return render_template('0-index.html')