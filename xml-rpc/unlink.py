import xmlrpc.client
import common

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(common.host))
res = models.execute_kw(common.db, common.get_uid(), common.password,
    'res.partner', 'unlink',
    [302], {})
print(res)