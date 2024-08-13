from odoo import http
from odoo.http import request


class PatientAnalysis(http.Controller):
    @http.route('/patient/analysis/answer', type='http', website=True, auth='user')
    def index(self, **kwargs):

        answers = request.env['wb.answer'].sudo().search([])

        return request.render('hospital_management.patient_analysis_template', {'answers': answers})

