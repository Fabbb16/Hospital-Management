from odoo import http
from odoo.http import request

class WebPatient(http.Controller):
    @http.route('/my/patients' ,type='http', auth='user', website=True)
    def index(self):

        user = request.env.user
        #shikojme nese useri eshte administrator ose jo
        if not user.has_group('base.group_system'):
            return request.redirect('/sorry')

        #marrim daten nga backu e shfaqim ne fornt
        patients = request.env['wb.patient'].sudo().search([])
        return request.render('hospital_management.patient_template', {'patients': patients})
