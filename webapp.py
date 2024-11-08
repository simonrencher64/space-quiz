from flask import Flask, request, render_template, flash
from markupsafe import Markup
from datetime import datetime

import os

app = Flask(__name__)

@app.route('/')
def render_about():
    return render_template('home.html')
 
def is_localhost():
    """ Determines if app is running on localhost or not
    Adapted from: https://stackoverflow.com/questions/17077863/how-to-see-if-a-flask-app-is-being-run-on-localhost
    """
    root_url = request.url_root
    developer_url = 'http://127.0.0.1:5000/'
    return root_url == developer_url


if __name__ == '__main__':
    app.run(debug=False)
