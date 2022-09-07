#do all the getrequests
#Ip adress 127.0.0.1:4000 as Json
#127.0.0.1/api/datas -> post
#format -> {"vorname":"user.firstname", "nachname":"user.secondname", "telnummer":"user.phonenumber"}
#https://rf-naruto-api.herokuapp.com/api/v1/shinobi example api
import requests
import json


def getRequests():
    try:
        r = requests.get("http://20.91.193.124:4000/api/datas")#return array dict
        data = json.loads(r.text)
        return data
    except:

        return "server is not reachable"