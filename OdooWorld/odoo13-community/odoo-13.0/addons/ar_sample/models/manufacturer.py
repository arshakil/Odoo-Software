from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
    
    _name = 'sample.manufacturer'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Sample Record'
    _rec_name = "product_code"
    

    product_code = fields.Char(string='PRODUCT CODE',required=True, track_visibility="always")
    product_id = fields.Many2one('product.template',string="PRODUCT TITLE")
    items_and_materials = fields.Char(string='ITEMS & MATERIALS')
    size = fields.Char(string='SIZE')
    shape = fields.Char(string='SHAPE')
    logo = fields.Char(string='LOGO')
    logo_ref = fields.Char(string='LOGO REF')
    logo_type = fields.Char(string='LOGO type')
    finish = fields.Char(string='FINISH')
    finish_ref = fields.Char(string='FINISH REF')
    part_b = fields.Char(string='PART B')
    part_c = fields.Char(string='PART C')
    part_d = fields.Char(string='PART D')
    qty = fields.Char(string='PQTY(GRS)')
    po = fields.Char(string='PO')
    mold_set = fields.Char(string='MOLD SET')