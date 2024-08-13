from odoo import http
from odoo.http import request

class WebLabTest(http.Controller):
    @http.route('/lab/tests', type='http', auth='user', website=True)
    def index(self, **kw):
        lab_tests = request.env['wb.lab'].sudo().search([])
        return request.render('hospital_management.lab_template', {'tests': lab_tests})
