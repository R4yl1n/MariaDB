import requests
import json

def deleterequests(vorname,nachname,telnummer):
    data = {
        'vorname':vorname,
        'nachname':nachname,
        'telnummer':telnummer
    }
    r = requests.delete("http://127.0.0.1:4000/api/datas",data)


#wrong delete request 