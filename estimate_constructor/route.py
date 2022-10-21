from flask import render_template
import datetime

from estimate_constructor import app, config

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html', year=datetime.datetime.now().year, creator=config.CREATOR)