#to activate venv  inside of Falsk dir -> PowerShell = venv/Scripts/activate
#to use as main file ->    $env:FLASK_APP = "main.py"
from contextlib import _RedirectStream, redirect_stderr, redirect_stdout
from urllib import request
from flask import Flask, render_template, request, url_for,redirect
from GetRequests import getrequests
from PostRequests import postrequests
from DeleteRequests import deleterequests

app = Flask(__name__)
@app.route("/",methods = ["POST","GET","DELETE"])

def helloWorld():
    if request.method == "GET":
        this = getrequests.getRequests()
        return render_template("index.html",value=this)

    if request.method == "POST":
        firstname = request.form["firstname"]
        familyname = request.form["familyname"]
        telnummer = request.form["telnummer"]

        postrequests.postRequests(firstname,familyname,telnummer)
        return redirect("http://Localhost:5000")

    if request.method == "DELETE":
        firstname = request.form["firstname"]
        familyname = request.form["familyname"]
        telnummer = request.form["telnummer"]

        deleterequests.deleterequests(firstname,familyname,telnummer)
        return redirect("http://Localhost:5000")

