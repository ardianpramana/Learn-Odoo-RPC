import xmlrpc.client

host = 'http://localhost:8014'
db = 'v14_bulog_dev'
username = 'admin'
password = 'admin'

def get_uid():
    uid = False
    # ServerProxy is object that manages communication with a remote XML-RPC server.
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(host))
    # print(common.version())
    uid = common.authenticate(db, username, password, {})
    return uid

print('Your user uid:', get_uid())