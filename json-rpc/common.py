import requests
import json

url = 'http://localhost:8014/jsonrpc'
db = 'v14_bulog_dev'
login = 'admin'
password = 'admin'

def get_uid():
    uid = False
    headers={
        "Content-Type":"application/json",
    }
    data = {
        "jsonrpc": "2.0",
        "methods": "call",
        "params": {
            "service": "common",
            "method": "login",
            "args": [db, login, password],
            "kwargs": {}
        }
    }
    res = requests.get(url, headers=headers,
        data=json.dumps(data).encode())
    if res.status_code == 200:
        res = res.json()
        uid = res.get('result', False)
    return uid

# print('Your user uid:', get_uid())
