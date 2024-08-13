from odoo import http
from odoo.http import request

class PatientInfo(http.Controller):
    @http.route('/patient/info', type='http', website=True, auth='user')
    def patient_info(self, **kw):
        return request.render('hospital_management.patient_info_template')

    @http.route('/patient/info/create', type='http', website=True, auth='user')
    def create_patient_info(self, **kw):

        partner = request.env.user.partner_id

        # Extract form data
        blood_group = request.params.get('blood_group')
        gender = request.params.get('gender')
        date_of_birth = request.params.get('date_of_birth')
        last_name = request.params.get('last_name')



        if blood_group and gender and date_of_birth and last_name:

            patient = request.env['wb.patient'].sudo().search([('name', '=', partner.name)], limit=1)
            if not patient:
                patient = request.env['wb.patient'].sudo().create({
                    'name': partner.name,
                    'phone': partner.phone,
                })

            patient.sudo().write({
                'blood_group': blood_group,
                'gender': gender,
                'date_of_birth': date_of_birth,
                'last_name': last_name
            })

        return request.redirect('/flm')

