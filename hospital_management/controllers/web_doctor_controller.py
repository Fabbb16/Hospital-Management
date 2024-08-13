from odoo import http
from odoo.http import request

class DocWeb(http.Controller):
    @http.route('/doctors', type='http', auth='public', website=True)
    def index(self):
        doctors = request.env['wb.doctor'].sudo().search([])
        return request.render('hospital_management.doctors_template', {'doctors': doctors})