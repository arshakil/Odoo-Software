from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime


class LeaveRequest(models.Model):
    _name = 'leave.request'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Leave request Record'
    _rec_name = "leave_user_id"
    _order = "id desc"

    leave_user_id = fields.Many2one('res.partner', string="Requester")
    leave_type = fields.Many2one('leave.type_off', string="Leave Type")
    allotted_days = fields.Integer(string="Allotted Days", related="leave_type.leave_days")
    remaining_days = fields.Integer(string="Remaining Days")
    requested_days = fields.Integer(string="Requested Days")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    state = fields.Selection([
        ('done', "Not approved"),
        ('confirm', "Confirm"),], string="State of the onboarding bank data step", default='done')

    # @api.onchange('leave_type')
    # def onchange_value(self):
    #     self.allotted_days = self.leave_type.leave_days
    #



        # for rec in self:
        #     if rec.leave_type:
        #         # leave_type_off_val = rec.env['leave.type_off'].sudo().search([('id', '=', rec.leave_type.id)])
        #         # print('Change', leave_type_off_val)
        #         rec.allotted_days = rec.leave_type.leave_days
        #         print('Change',rec.leave_type.leave_type_off)
        #         print('Change', rec.leave_type.leave_days)

    # @api.depends('start_date', 'end_date')
    # def days_count(self):
    #     fmt = '%Y-%m-%d'
    #     d1 = datetime.strptime(str(self.start_date), fmt)
    #     d2 = datetime.strptime(str(self.end_date), fmt)
    #     daysDiff = str((d2 - d1).days + 1)
    #     print(daysDiff)

    @api.onchange('leave_type','remaining_days')
    def calculate_remaining_days(self):
        print('leave type',self.leave_type.leave_type_off)

        for rec in self:
            check_exists= self.env['leave.request'].search([("leave_type","=",rec.leave_type.leave_type_off),])
            print("check_exists",check_exists)





        # pass



        # if self.remaining_days==0:
        #     self.remaining_days = self.allotted_days





    @api.onchange('start_date', 'end_date','requested_days')
    def calculate_date(self):
        if self.start_date and self.end_date:
            d1=datetime.strptime(str(self.start_date),'%Y-%m-%d')
            d2=datetime.strptime(str(self.end_date),'%Y-%m-%d')
            d3=d2-d1
            # print('type is :',type(d3),int(d3.days))
            if int(d3.days)<1:
                raise ValidationError("you cant select leave less then 1 days but you selected: %s" %d3.days +" days")
            else:
                self.requested_days=str(d3.days)

    def action_confirm(self):
        if self.remaining_days == 0:
            raise ValidationError("you cant get a leave")
        else:
            self.remaining_days= self.remaining_days-self.requested_days
        self.state = "confirm"
        # print('confirmed')


    def action_cancel(self):
        self.state = "done"
        # print('done')


class RemaningLeaveRequest(models.Model):
    _name = 'leave.request.remaning'
    _description = 'Leave request remaning Record'
    _rec_name = "leave_user_remaining_days"
    _order = "id desc"

    leave_user_name = fields.Char(string="User name")
    leave_user_remaining_days = fields.Char(string="User name")
    leave_user_leave_type = fields.Char(string="User name")