from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class LeaveTypeOff(models.Model):
    _name = 'leave.type_off'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Leave Type request Record'
    _rec_name = "leave_type_off"
    _order = "id desc"

    leave_type_off = fields.Char(string='Leave Type', required=True, track_visibility="always")
    leave_days = fields.Integer(string="Days")
