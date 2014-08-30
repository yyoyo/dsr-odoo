from osv import osv, fields

class Partner(osv.osv):
    _inherit = 'res.partner'

    _columns = {
        'test': fields.boolean('Test'),
    }

    _defaults = {
        'test': False,
    }

joder()