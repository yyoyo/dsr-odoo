from openerp.osv import fields, osv

class Partner(osv.osv):
    '''Partner'''
    _inherit = 'res.partner'

    _columns = {
        'timebank_debts': fields.one2many('dsr.timebank.debt', 'member', 'Timebank debts'),
        }

Partner()