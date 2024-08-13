from odoo import http
from odoo.http import request

class WebNurse(http.Controller):
    @http.route('/hospital/nurses', type='http' ,auth='user', website=True)
    def index(self):

        user =request.env.user

        if not user.has_group('base.group_system'):
            return request.redirect('/sorry')


        nurse = request.env['wb.nurse'].sudo().search([])
        return request.render('hospital_management.nurse_template', {'nurse': nurse})
