import requests
import json

def deleterequests(vorname,nachname,telnummer):
    url = "http://20.91.193.124:4000/api/datas"
    payload = {
        'vorname':vorname,
        'nachname':nachname,
        'telnummer':telnummer

    }
    headers = {'content-type': 'application/json'}
    r = requests.delete(url=url,data=json.dumps(payload),headers=headers)


 