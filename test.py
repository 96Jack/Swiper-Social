import json
import requests

api = "https://open.ucpaas.com/ol/sms/sendsms"

config = {
        "sid":"b8986f9d2717e385ac5f705b1ffec443",
        "token":"2f16a331eca3d8892e665afdc0224e52",
        "appid":"4f73ec27a7b54221b7dca9ee4f0def9b",
        "templateid":"154501",
        "param":"",
        "mobile":"",
        
}

p = 18018664051
def send(phone, code):
    config['param'] = code
    config['mobile'] = phone
    response = requests.post(api, json=config)
    return response
    
