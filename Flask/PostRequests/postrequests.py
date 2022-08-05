#do all the postrequests
#Ip adress 127.0.0.1:4000 as Json
#127.0.0.1/api/datas -> getall
#127.0..0.1/api/datas/{user} -> get user
#format -> {"vorname":"user.firstname", "nachname":"user.secondname", "telnummer":"user.phonenumber"}
import requests
import json


def postRequests(vorname, nachname, telnummer):
    data = {'vorname':   vorname,
    'nachname': nachname,
    'telnummer':  telnummer}
    header={'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post("127.0.0.1:4000",data=json.dumps(data),headers=header)