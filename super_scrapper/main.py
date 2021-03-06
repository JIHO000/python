import imp
import re
from flask import Flask, redirect, render_template, request, send_file
from indeed import get_jobs
from expoter import save_to_file

app = Flask(__name__, template_folder='templates')
@app.route("/")
def home():
    return render_template("home.html")

db = {}

@app.route("/report")
def report():
    word =request.args.get("word")
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            pass
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template("report.html", searchingBy=word, resultsNumber =len(jobs), jobs=jobs)

@app.route("/export")
def export():
    try:
        word = request.args.get("word")
        if not word:
            raise Exception()
        word=word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")
   

app.run(host="0.0.0.0")