from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime
import time
from datetime import date
from datetime import date, datetime


class EarnLeaveRequest(models.Model):
    _name = 'earn.leave'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _description = 'Earn Leave request Record'
    _rec_name = "earn_leave_user_id"
    _order = "id desc"

    earn_leave_user_id = fields.Many2one('hr.employee', string="Requester")
    allotted_days = fields.Integer(string="Allotted Days",)
    remaining_days = fields.Integer(string="Remaining Days")
    requested_days = fields.Integer(string="Requested Days")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    state = fields.Selection([
        ('done', "Not approved"),
        ('confirm', "Confirm"),], string="State of the onboarding bank data step", default='done')



    @api.onchange('earn_leave_user_id')
    def calculate_allotted_days(self):
        if self.earn_leave_user_id:
            print("change ",self.earn_leave_user_id.name)
            print("Create Date of User ", self.earn_leave_user_id.joining_date)
            print("Create Date of User type:: ", type(self.earn_leave_user_id.joining_date))

            if self.earn_leave_user_id.joining_date:
                d1 = datetime.strptime(self.earn_leave_user_id.joining_date, "%Y-%m-%d").date()
                d2 = datetime.now().date()
                d3 = (d2 - d1).days
                earn_leave_days = d3/18
                print('earn leave is: ',earn_leave_days)
                self.allotted_days=d3
            else:
                raise ValidationError("Please Check Employees Joining Date")




    @api.onchange('start_date', 'end_date','requested_days')
    def calculate_requested_days(self):
        if self.start_date and self.end_date:
            d1 = datetime.strptime(self.start_date, '%Y-%m-%d')
            d2 = datetime.strptime(self.end_date, '%Y-%m-%d')

            print('type is d1 :', type(d1))
            print('type is d2 :', type(d2))


            d3=d2-d1
            cont_days = int(d3.days)+1
            print('type is :',type(d3),int(d3.days))
            if cont_days<1:
                self.requested_days=0
                # time.sleep(500)
                # raise ValidationError("you cant select leave less then 1 days but you selected: %s" %d3.days +" days")
            else:
                self.requested_days=cont_days