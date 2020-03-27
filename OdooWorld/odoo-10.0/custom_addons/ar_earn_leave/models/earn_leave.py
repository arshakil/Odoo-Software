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

    earn_leave_user_id = fields.Many2one('hr.employee', string="Employee")
    allotted_days = fields.Integer(string="Allotted Days",)
    remaining_days = fields.Integer(string="Remaining Days")
    requested_days = fields.Integer(string="Requested Days")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    state = fields.Selection([
        ('to_submit', "To Submit"),
        ('to_approved', "To Approved"),
        ('approved', "Approved"),
        ('refuse', "Refuse"),], string="Status", default='to_approved')


    # @api.multi
    # def action_approved(self):
    #     if self.earn_leave_user_id:
    #         for rec in self:
    #             check_exists = self.env['earn.leave'].search([("earn_leave_user_id", "=", rec.earn_leave_user_id.name), ])
    #             if check_exists:
    #                 for e in check_exists:
    #                     print("Name: ", e.earn_leave_user_id)
    #                     print("remaining_days: ", e.remaining_days)
    #
    #             else:
    #                 self.remaining_days = self.allotted_days - self.requested_days
    #                 print ('remaining days less then 0',rec.remaining_days)
    #
    #
    #
    #
    #
    #
    #         # for rec in self:
    #         #     check_exists = self.env['earn.leave'].search([("earn_leave_user_id", "=", rec.earn_leave_user_id.name), ])
    #         #     if check_exists:
    #         #         for e in check_exists:
    #         #             e.leave_taken=e.leave_taken+self.requested_days
    #         #
    #         #
    #         #     else:
    #         #         self.leave_taken = self.requested_days
    #         #         self.remaining_days=self.allotted_days-self.requested_days
    #         #
    #
    #
    #     self.state = 'approved'

    @api.multi
    def action_confirm(self):
        self.state = 'to_approved'

    # @api.multi
    # def action_refuse(self):
    #     self.state = 'refuse'


    @api.multi
    def action_draft(self):
        self.state = 'to_submit'


    # Calculate  allotted days
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
                self.allotted_days = earn_leave_days
                print('earn leave is: ',earn_leave_days)

                # self.allotted_days=d3
            else:
                raise ValidationError("Please Check Employees Joining Date")





    # Calculate Requested Days
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




    # Calculate remaining Days
    @api.onchange('earn_leave_user_id')
    def calculate_remaining_days(self):

        # check_user_state_exists = self.env['earn.leave'].search(['&',
        #     ("earn_leave_user_id", "=", self.earn_leave_user_id.name),
        #     ("state", "=", "to_approved")])
        # if check_user_state_exists:
        #     print ('username exists')
        #     raise ValidationError(_('Error! You already requested for a leave!!! '))
        # else:
        #     print ('does not exists')




        if self.earn_leave_user_id:
            check_remaining_exists = self.env['annualleave.remaining'].search([("leave_user_name", "=", self.earn_leave_user_id.name), ])
            if check_remaining_exists:
                print("check_exists", check_remaining_exists)
                for e in check_remaining_exists[0]:
                    print("Name: ", e.leave_user_name)
                    print("remaining_days: ", e.leave_user_remaining_days)
                    # self.remaining_days=e.leave_user_remaining_days
                    new_allotted_days = self.allotted_days - e.leave_taken
                    self.remaining_days = new_allotted_days
                    print ('\n\n\nleave taken :  ',e.leave_taken)



            else:
                self.remaining_days = self.allotted_days



    @api.multi
    def action_approved(self):
        if self.earn_leave_user_id:
            check_remaining_exists = self.env['annualleave.remaining'].search([("leave_user_name", "=", self.earn_leave_user_id.name), ])
            if check_remaining_exists:
                print ('remaining exists',check_remaining_exists)
                for e in check_remaining_exists[0]:
                    new_allotted_days = self.allotted_days-(e.leave_taken+self.requested_days)
                    print('new_allotted_days',new_allotted_days)

                    # self.remaining_days = new_allotted_days - self.requested_days
                    self.remaining_days = new_allotted_days
                    print('new_remaining_days',  self.remaining_days)

                    leave_taken=e.leave_taken+self.requested_days
                    print('new_leave_taken', leave_taken)



                    # self.remaining_days = self.remaining_days - self.requested_days
                    annual_remaining_days = abs(self.remaining_days - self.requested_days)
                    print ('annual_remaining_days',annual_remaining_days)
                    annualRemainingLeave = self.env['annualleave.remaining'].browse(self.env.context.get('active_ids', []))
                    annualRemainingLeave.create({'leave_user_name': self.earn_leave_user_id.name,'leave_user_remaining_days':annual_remaining_days,'leave_taken':leave_taken})

            else:
                self.remaining_days=self.allotted_days - self.requested_days
                annual_remaining_days = self.allotted_days-self.requested_days
                annualRemainingLeave = self.env['annualleave.remaining'].browse(self.env.context.get('active_ids', []))
                annualRemainingLeave.create({'leave_user_name': self.earn_leave_user_id.name,'leave_user_remaining_days':annual_remaining_days,'leave_taken':self.requested_days})
                print ('remaining does not exists',check_remaining_exists)
        self.state = 'approved'


    @api.multi
    def action_refuse(self):
        remaining_days=self.remaining_days+self.requested_days
        self.remaining_days=remaining_days
        check_remaining_exists = self.env['annualleave.remaining'].search([("leave_user_name", "=", self.earn_leave_user_id.name), ])
        for e in check_remaining_exists[0]:
            print ('leave taken: ',e.leave_taken)
            taken_leave = e.leave_taken-e.leave_user_remaining_days
            annualRemainingLeave = self.env['annualleave.remaining'].browse(self.env.context.get('active_ids', []))
            annualRemainingLeave.create({'leave_user_name': self.earn_leave_user_id.name, 'leave_user_remaining_days': remaining_days, 'leave_taken': taken_leave})
        self.state = 'refuse'


    @api.model
    def create(self, values):
        annual=super(EarnLeaveRequest, self.with_context(mail_create_nosubscribe=True)).create(values)
        if annual.requested_days>annual.remaining_days:
            raise ValidationError(_('Error! You cannot create you don\'t have enough leave'))


        check_user_state_exists = annual.env['earn.leave'].search([
            ("earn_leave_user_id", "=", "Rubel"),
            ("state", "=", "To Approved")])
        print('check_user_state_exists', check_user_state_exists)
        if check_user_state_exists:
            for e in check_user_state_exists:
                print ("User name Is: ",e.earn_leave_user_id.name)
                raise ValidationError(_('Error! You cannot create'))
        else:
            print('doesnot exists')


        return annual

    # @api.constrains('earn_leave_user_id')
    # def _check_something(self):
    #     check_user_state_exists = self.env['earn.leave'].search(
    #         [("earn_leave_user_id", "=", self.earn_leave_user_id.name),
    #          ("state", "=", "to_approved")])
    #     print('check_user_state_exists', check_user_state_exists.name)
    #     if check_user_state_exists:
    #         for e in check_user_state_exists:
    #             if e.earn_leave_user_id == self.earn_leave_user_id.name and self.state == "To Approved":
    #                 raise ValidationError(_('Error! You cannot create You already requested for a leave'))


class AnnualRemainingLeave(models.Model):
    _name = 'annualleave.remaining'
    _description = 'Annual Leave request remaining Record'
    _rec_name = "leave_user_name"
    _order = "id desc"

    leave_user_name = fields.Char(string="User name")
    leave_user_remaining_days = fields.Integer(string="leave remaining",default=0)
    leave_taken = fields.Integer(string="leave taken", default=0)


