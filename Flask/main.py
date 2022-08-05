#to activate venv  inside of Falsk dir -> PowerShell = venv/Scripts/activate
from flask import Flask
from .GetRequests import getrequests
from .PostRequests import postrequests

app = Flask(__name__)
@app.route("/")

def helloWorld():
    this = "this thing"
    return render_template("index.html",value=this)

#error message
#  __import__(module_name)
#  File "C:\Users\rayli\go\src\MariaDB\Flask\main.py", line 3, in <module>
#    from .GetRequests import getrequests
#ImportError: attempted relative import with no known parent package