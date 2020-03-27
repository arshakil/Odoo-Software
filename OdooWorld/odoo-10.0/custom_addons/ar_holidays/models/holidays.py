from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class Course(models.Model):
    _name = 'ar.holidays'

    name = fields.Char(string="Type Of Holidays", required=True,)
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")

    requested_days = fields.Integer(string="Requested Days")
    description = fields.Text()






    @api.onchange('start_date', 'end_date','requested_days')
    def calculate_date(self):
        if self.start_date and self.end_date:
            d1=datetime.strptime(str(self.start_date),'%Y-%m-%d')
            d2=datetime.strptime(str(self.end_date),'%Y-%m-%d')
            d3=d2-d1
            print('type is :',type(d3),int(d3.days))
            if int(d3.days)<0:
                raise ValidationError("you cant select leave less then 1 days but you selected: %s" %d3.days +" days")
            else:
                self.requested_days=int(d3.days)+1