from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")
    
@app.route("/menu")
def about_me():
    return render_template("menu.html")
    
@app.route("/music")
def music page():
    returm render_template("music.html")
    
@app.route("/jobs")
def jobs_page():
    return render_template("jobs.html")