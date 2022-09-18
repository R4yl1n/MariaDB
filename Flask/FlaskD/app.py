#to activate venv  inside of Falsk dir -> PowerShell = venv/Scripts/activate
#to use as main file ->    $env:FLASK_APP = "main.py"
#run instance python3 -m flask run --host=0.0.0.0
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
        getResponse = getrequests.getRequests()
        return render_template("index.html",value=getResponse)

    if request.method == "POST":
        firstname = request.form["firstname"]
        familyname = request.form["familyname"]
        telnummer = request.form["telnummer"]

        try:
            postrequests.postRequests(firstname,familyname,telnummer)
            print("Post request succefuly")
            return redirect("http://20.91.193.124:80")
        except:
            errorpost = postrequests.postRequests(firstname,familyname,telnummer)
            print("Post request failed")
            return render_template("index.html", errorhandling=errorpost)

    if request.method == "DELETE":
        firstname = request.form["firstname"]
        familyname = request.form["familyname"]
        telnummer = request.form["telnummer"]

        deleterequests.deleterequests(firstname,familyname,telnummer)
        return redirect("http://20.91.193.124:80")
      
@app.route("/delete",methods = ["POST","GET"])
def delete():
    if request.method == "GET":
        getResponse = getrequests.getRequests()
        return render_template("Delete.html",value=getResponse)

    if request.method == "POST":
        firstname = request.form["firstname"]
        familyname = request.form["familyname"]
        telnummer = request.form["telnummer"]   
        try:
            deleterequests.deleterequests(firstname,familyname,telnummer)
            print("Delete request succefuly")
            return redirect("http://20.91.193.124:80")
        except:
            errorpost = deleterequests.deleterequests(firstname,familyname,telnummer)
            print("Delete request failed")
            return render_template("index.html", errorhandling=errorpost)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')