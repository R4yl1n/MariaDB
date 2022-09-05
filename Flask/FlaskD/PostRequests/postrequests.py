#do all the postrequests
#Ip adress 127.0.0.1:4000 as Json
#127.0.0.1/api/datas -> getall
#127.0..0.1/api/datas/{user} -> get user
#format -> {"vorname":"user.firstname", "nachname":"user.secondname", "telnummer":"user.phonenumber"}
from ast import Str
from tokenize import String
import requests


def postRequests(vorname, nachname, telnummer):
    datas = {'vorname':   vorname,
    'nachname': nachname,
    'telnummer':  telnummer}

    for data in datas:
        if isinstance(datas[data], int):
            return "please check the format something went wrong"

    try:
        r = requests.post("http://127.0.0.1:4000/api/datas",datas)
        return "succes"
    except:

        return "server is not reachable"