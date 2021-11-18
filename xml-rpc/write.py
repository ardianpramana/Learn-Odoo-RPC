import xmlrpc.client
import common

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(common.host))
res = models.execute_kw(common.db, common.get_uid(), common.password,
    'res.partner', 'write',
    [302, {'name': 'Partner 0003', 'email': 'email@ardian.com'}], {})
print(res)