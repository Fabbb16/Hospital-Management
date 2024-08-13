from odoo import http
from odoo.http import request

class WebPharmacy(http.Controller):
    @http.route('/hospital/pharmacy', auth='user', type='http', website=True)
    def index(self):
        pharmacy = request.env['wb.pharmacy'].sudo().search([])
        return request.render('hospital_management.pharmacy_template', {'pharmacy': pharmacy})