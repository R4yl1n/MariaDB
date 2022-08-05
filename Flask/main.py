#to activate venv  inside of Falsk dir -> PowerShell = venv/Scripts/activate
#to use as main file ->    $env:FLASK_APP = "main.py"
from flask import Flask, render_template
from GetRequests import getrequests
from PostRequests import postrequests


app = Flask(__name__)
@app.route("/")

def helloWorld():
    this = getrequests.getRequests()
    return render_template("index.html",value=this)
