from odoo import http
from odoo.http import request


class Leave(http.Controller):

    # getting all leave
    @http.route('/get_leave', type='json', auth='user')
    def get_leave(self):
        print("Yes here entered")
        leave_rec = request.env['leave.type_off'].search([])
        leaves = []
        for rec in leave_rec:
            vals = {
                'id': rec.id,
                'leave_type_off': rec.leave_type_off,
                'leave_days': rec.leave_days,
            }
            leaves.append(vals)
        print("Patient List--->", leaves)
        data = {'status': 200, 'response': leaves, 'message': 'Done All leaves Returned'}
        return data

    # Create leave
    @http.route('/create_leave', type='json', auth='user')
    def create_leave(self, **rec):
        if request.jsonrequest:
            print("rec", rec)
            if rec['leave_type_off']:
                vals = {
                    'leave_type_off': rec['leave_type_off'],
                    'leave_days': rec['leave_days']
                }
                new_leave = request.env['leave.type_off'].sudo().create(vals)
                print("New Patient Is", new_leave)
                args = {'success': True, 'message': 'Success', 'id': new_leave.id}
        return args

    # update leave
    @http.route('/update_leave', type='json', auth='user')
    def update_leave(self, **rec):
        if request.jsonrequest:
            if rec['id']:
                print("rec...", rec)
                leave_id = request.env['leave.type_off'].sudo().search([('id', '=', rec['id'])])
                if leave_id:
                    leave_id.sudo().write(rec)
                args = {'success': True, 'message': 'Leave Updated'}
        return args

    # delete leave
    @http.route('/delete_leave', type='json', auth='user')
    def delete_leave(self, **rec):
        if request.jsonrequest:
            if rec['id']:
                print("rec...", rec)
                leave_id = request.env['leave.type_off'].sudo().search([('id', '=', rec['id'])])
                if leave_id:
                    leave_id.sudo().unlink()
                args = {'success': True, 'message': 'Leave deleted'}
        return args
