from odoo import http
from odoo.http import request

class WebVaccine(http.Controller):
    @http.route('/hospital/vaccine', type='http', auth='user', website=True)
    def index(self):
        vaccines = request.env['wb.vaccine'].sudo().search([])
        return request.render('hospital_management.vaccine_template', {'vaccines': vaccines})

