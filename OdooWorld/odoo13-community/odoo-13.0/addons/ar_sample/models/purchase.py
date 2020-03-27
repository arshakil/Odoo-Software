from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class PurchaseInherit(models.Model):

    _inherit = 'purchase.order'

    ref_no = fields.Char(string="REF NO")

    state = fields.Selection([
        ('draft', 'RFQ'),
        ('step1', 'STEP 1'),
        ('step2', 'STEP 2'),
        ('sent', 'RFQ Sent'),
        ('to approve', 'To Approve'),
        ('purchase', 'Purchase Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled')
    ], string='Status', readonly=True, index=True, copy=False, default='draft', tracking=True)