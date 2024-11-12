from flask import Flask, request, render_template, flash, make_response, session
from markupsafe import Markup
from datetime import datetime

import os
import json

app = Flask(__name__)
app.secret_key=os.environ["secret_key"];

@app.route('/')
def render_about():
    return render_template('home.html')
 
 
@app.route('/question1',methods=["GET","POST"])
def render_question1():
    session["qNum"] = 1
    session["uArray"] = []
    with open('static/answers.json') as data:
        answers = json.load(data)
        
    # for loop that puts answers from json file into "ans" array
    ans = []
    for i in range(4): # 4 options to choose from
        ans.append(answers[session["qNum"]-1]["Answers"][i])
    
    # sets q to question in json file
    q = answers[session["qNum"]-1]["Question"]
    return render_template('questionLayout.html',question=q,a=ans)
    
    
    
    
@app.route('/next',methods=["GET","POST"])
def render_next():
    uA = request.form["answer"]
    session["uArray"].append(uA)
    session["qNum"] += 1
    with open('static/answers.json') as data:
        answers = json.load(data)
        
    # -1 because qNum starts at 1
    if session["qNum"] - 2 > len(answers):
        return render_template('end.html')
    # for loop that puts answers from json file into "ans" array
    ans = []
    for i in range(4): # 4 options to choose from
        ans.append(answers[session["qNum"]-1]["Answers"][i])
    
    # sets q to question in json file
    q = answers[session["qNum"]-1]["Question"]
    return render_template('questionLayout.html',question=q,a=ans)
    
def is_localhost():
    """ Determines if app is running on localhost or not
    Adapted from: https://stackoverflow.com/questions/17077863/how-to-see-if-a-flask-app-is-being-run-on-localhost
    """
    root_url = request.url_root
    developer_url = 'http://127.0.0.1:5000/'
    return root_url == developer_url


if __name__ == '__main__':
    app.run(debug=True)
