from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/menu")
def menu():
    return render_template("menu.html")
    
@app.route("/music")
def music():
    return render_template("music.html")
    
@app.route("/jobs")
def jobs():
    return render_template("jobs.html")
    
if __name__ == "__main__":
    app.run()