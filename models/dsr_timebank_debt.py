from openerp.osv import fields,osv

class dsr_timebank_debt(osv.osv):
    _name = "dsr.timebank.debt"

    _columns = {
        'member': fields.many2one('res.partner', 'member', ondelete='cascade', select=1, required=True),
        'intervention_date': fields.date('Intervention date', required=True, translate=True),
        'hours': fields.integer('due hours', required=True, translate=True),
    }

    def _check_hours(self, cr, uid, ids, context=None):
        record = self.browse(cr, uid, ids, context=context)
        for data in record:
            if data.hours < 1:
                return False
        return True

    _constraints = [(_check_hours, 'Error: hours must be Positive', ['hours'])]

dsr_timebank_debt()

