from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
    
    _name = 'ar_purchase.request'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'purchase request Record'
    _rec_name = "ref_no"
    

    ref_no = fields.Char(string='Ref No',required=True, track_visibility="always")
    approver_name = fields.Many2one('res.partner',string='Approver')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')

    product_request_lines = fields.One2many('ar_purchase.request_lines', 'purchase_request_id', string='product Booking Lines')
    # product_request_lines_2 = fields.Many2one('product.product',  string='product Booking Lines')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('to_be_approved', 'To be Approved'),
        ('manage_approved', 'Manage Approved'),
        ('rejected', 'Rejected'),
        ('done', 'Done'),
    ], string='Status', readonly=True, index=True, copy=False, default='draft', tracking=True)

    class productInheritLines(models.Model):
        _name = 'ar_purchase.request_lines'
        _description = 'purchase request Lines Record'
        _rec_name = "product_title"

        purchase_request_id = fields.Many2one('ar_purchase.request', string='purchase request')
        product_description = fields.Char(string='Description')
        product_qty = fields.Integer(string='Quantity')
        reqst_date = fields.Date(string='Request Date')
        product_title = fields.Many2one('product.template', string='Product')