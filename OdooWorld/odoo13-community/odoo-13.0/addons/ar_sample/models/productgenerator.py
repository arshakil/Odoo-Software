from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ProductGenerator(models.Model):
    
    _name = 'sample.productgenerator'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Product Generator'
    _rec_name = "product_code"
    

    product_code = fields.Char(string="PRODUCT CODE")
    # product_code = fields.Many2one('sample.manufacturer', string="PRODUCT CODE")
    # product_title = fields.Many2one(related='product_code.product_id', string='PRODUCT TITLE')
    items_and_materials = fields.Char(string='ITEMS AND MATERIALS')
    size = fields.Char(string='SIZE')
    # size = fields.Selection(selection=[('sm', 'SM'),('m', 'M'),('xl', 'XL'),('xxl', 'XXL'),], string='SIZE', default='m') 
    shape = fields.Char(string='SHAPE')
    logo = fields.Char(string='LOGO')
    logo_ref = fields.Char(string='LOGO REF')
    logo_type = fields.Char(string='LOGO TYPE')
    finish = fields.Char(string='FINISH')
    finish_ref = fields.Char(string='FINISH REF')
    part_b = fields.Char(string='PART B')
    part_c = fields.Char(string='PART C')
    part_d = fields.Char(string='PART D')
    # qty = fields.Char(string='PQTY(GRS)', related='product_code.qty')
    qty = fields.Char(string='PQTY(GRS)', default='1')
    po = fields.Char(string='PO')
    # mold_set = fields.Char(string='MOLD SET', related='product_code.mold_set')
    mold_set = fields.Char(string='MOLD SET',default='1')

    
    booking_id = fields.Many2one('sample.samplebooking', string='Booking')

