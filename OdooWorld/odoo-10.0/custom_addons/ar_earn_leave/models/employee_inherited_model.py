from odoo import fields, models

class EmployeeJoining(models.Model):
    _inherit = 'hr.employee'

    joining_date = fields.Date(string="Joining Date")