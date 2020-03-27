from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SampleBooking(models.Model):
    
    _name = 'sample.samplebooking'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Sample Booking'
    _rec_name = "sa_no"
    

    sa_no = fields.Char(string='SA NO')
    sa_date = fields.Date(string='SA DATE')
    ppd = fields.Date(string='PPD')
    customer_name = fields.Char(string='CUSTOMER NAME')
    buyer_name = fields.Char(string='BUYER NAME')
    sales_person = fields.Char(string='SALES PERSON')
    revised_on = fields.Char(string='REVISED ON')
    style = fields.Char(string='STYLE')
    season = fields.Char(string='SEASON')
    # samplebooking_lines = fields.One2many('sample.samplebooking.lines', 'booking_id', string='Sample Booking Lines')
    samplebooking_lines = fields.One2many('sample.productgenerator', 'booking_id', string='Sample Booking Lines')




class SampleBookingLines(models.Model):
    
    _name = 'sample.samplebooking.lines'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Sample Booking Lines'
    _rec_name = "product_id"

    product_id = fields.Many2one('sample.productgenerator', string='Product')
    booking_id = fields.Many2one('sample.samplebooking', string='Booking')
    

