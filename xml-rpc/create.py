import xmlrpc.client
import common

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(common.host))
res = models.execute_kw(common.db, common.get_uid(), common.password,
    'res.partner', 'create',
    [{'name': 'Partner 0002', 'email': 'email@ardian.com'}], {})
print(res)