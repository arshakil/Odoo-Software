from odoo import api, fields, models, modules, _


class TestUsers(models.Model):
    _inherit = 'res.users'


    @api.model
    def create(self, vals):
        print("user is created")

        return super(TestUsers, self).create(vals)