import base64

from odoo import http
from odoo.http import request


class WebAnalysis(http.Controller):
    @http.route('/analysis/form', type='http', auth='user', website=True)
    def index(self):
        return request.render('hospital_management.analysis_template')

    @http.route('/analysis/create', type='http', auth='user', website=True)
    def create(self, **kwargs):
        partner = request.env.user.partner_id

        file = request.params.get('file')
        date = request.params.get('date')
        notes = request.params.get('notes')

        if file and date and notes:
            file_content = base64.b64encode(file.read())
            file_name = file.filename

            patient = request.env['wb.patient'].sudo().search([('name', '=', partner.name)], limit=1)
            if not patient:
                patient = request.env['wb.patient'].sudo().create({
                    'name': partner.name,
                    'phone': partner.phone,
                    'date_of_birth': partner.date_of_birth
                })

            request.env['wb.analysis'].sudo().create({
                'patient_id': patient.id,
                'file': file_content,
                'file_name': file_name,
                'date': date,
                'notes': notes
            })

        return request.redirect('/flm')
