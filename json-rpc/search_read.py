import requests
import json
import common

headers={
    "Content-Type":"application/json",
}
data = {
    "jsonrpc": "2.0",
    "methods": "call",
    "params": {
        "service": "object",
        "method": "execute_kw",
        "args": [
            common.db,
            common.get_uid(),
            common.password,
            'res.partner',
            'search_read',
            [[('name', '=', 'Ali')]],
            {
                "fields": ["name", "email", "phone"],
                "limit": 2,
                "context": {
                    "rpc_request": 1
                }
            }
        ]
    }
}
res = requests.get(common.url, headers=headers,
    data=json.dumps(data).encode())
print(res)
if res.status_code == 200:
    res = res.json()
    print(res)
