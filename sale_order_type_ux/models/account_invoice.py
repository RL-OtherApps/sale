##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################

from odoo import api, fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    sale_type_id = fields.Many2one(
        readonly=True,
        states={'draft': [('readonly', False)]},
    )

    @api.onchange('sale_type_id')
    def onchange_sale_type_id(self):
        super().onchange_sale_type_id()
        if self.sale_type_id.journal_id:
            self.company_id = self.sale_type_id.journal_id.company_id.id
