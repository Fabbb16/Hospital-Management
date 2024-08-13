from odoo import http
from odoo.http import request

class WebVaccination(http.Controller):
    @http.route('/vaccination/form', type='http', auth='user', website=True)
    def index(self, **kwargs):
        vaccines = request.env['wb.vaccine'].sudo().search([])
        return request.render('hospital_management.vaccination_template', {'vaccines': vaccines})


    @http.route('/vaccination/create', type='http', auth='user', website=True, csrf=False, methods=['POST'])
    def vaccination(self, **kwargs):
        partner = request.env.user.partner_id

        vaccine_id = request.params.get('vaccine_id')
        date = request.params.get('date')

        if vaccine_id and date:
            patient = request.env['wb.patient'].sudo().search([('name', '=', partner.name)], limit=1)
            if not patient:
                patient = request.env['wb.patient'].sudo().create({
                    'name': partner.name,
                    'phone': partner.phone,
                    'date_of_birth': partner.date_of_birth
                })

            request.env['wb.vaccination'].sudo().create({
                'patient_id': patient.id,
                'vaccine_id': vaccine_id,
                'date': date
            })

        return request.redirect('/flm')
