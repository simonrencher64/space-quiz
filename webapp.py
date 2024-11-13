from flask import Flask, request, render_template, flash, make_response, session
from markupsafe import Markup
from datetime import datetime

import os
import json

app = Flask(__name__)
app.secret_key=os.environ["secret_key"];

@app.route('/')
def render_home():
    return render_template('home.html')
 
 
@app.route('/question1',methods=["GET","POST"])
def render_question1():
    session["qNum"] = 0
    session["uArray"] = []
    with open('static/answers.json') as data:
        answers = json.load(data)
        
    # for loop that puts answers from json file into "ans" array
    ans = []
    for i in range(4): # 4 options to choose from
        ans.append(answers[session["qNum"]]["Answers"][i])
    # sets q to question in json file
    q = answers[session["qNum"]]["Question"]
    return render_template('questionLayout.html',question=q,a=ans,qNum=int(session["qNum"])+1)
    
    
    
    
@app.route('/next',methods=["GET","POST"])
def render_next():
    uA = request.form["answer"]
    session["uArray"].append(uA)
    session["qNum"] += 1
    with open('static/answers.json') as data:
        answers = json.load(data)
        
    # -1 because qNum starts at 1
    if session["qNum"] + 1 > len(answers):
        return render_template('end.html',score=calculateScore(session["uArray"]))
    # for loop that puts answers from json file into "ans" array
    ans = []
    for i in range(4): # 4 options to choose from
        ans.append(answers[session["qNum"]]["Answers"][i])
    
    # sets q to question in json file
    q = answers[session["qNum"]]["Question"]
    return render_template('questionLayout.html',question=q,a=ans,qNum=int(session["qNum"])+1)



def calculateScore(arr):
    score = 0;
    maxScore = len(arr)
    with open('static/answers.json') as data:
        answers = json.load(data)
    for i in range(len(arr)):
        if int(answers[i]["Correct"]) == int(arr[i]):
            score += 1
    return str(score) + " / "+ str(maxScore)


def is_localhost():
    """ Determines if app is running on localhost or not
    Adapted from: https://stackoverflow.com/questions/17077863/how-to-see-if-a-flask-app-is-being-run-on-localhost
    """
    root_url = request.url_root
    developer_url = 'http://127.0.0.1:5000/'
    return root_url == developer_url


if __name__ == '__main__':
    app.run(debug=True)
