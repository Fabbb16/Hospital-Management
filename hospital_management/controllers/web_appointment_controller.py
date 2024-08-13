from odoo import http
from odoo.http import request

class WebAppointments(http.Controller):
    @http.route('/appointment/form', type='http', auth='user', website=True)
    def index(self, **kw):
        # Render the appointment form
        return request.render('hospital_management.appointment_template')

    @http.route('/appointment/create', type='http', auth='user', website=True)
    def create_app(self, **kw):
        # Automatically get the patient_id from the logged-in user's partner_id
        partner = request.env.user.partner_id

        date = request.params.get('date')
        reason = request.params.get('reason')

        if date and reason:
            # Check if there are any free rooms available
            free_rooms = request.env['wb.room'].sudo().search([('state', '=', 'free')])
            if not free_rooms:
                return request.redirect('/scusa')

            # Check if the patient record exists, if not, create it
            patient = request.env['wb.patient'].sudo().search([('name', '=', partner.name)], limit=1)
            if not patient:
                patient = request.env['wb.patient'].sudo().create({
                    'name': partner.name,
                    'phone': partner.phone,
                    'date_of_birth': partner.date_of_birth,
                    # Add any other necessary fields
                })



            # Create the appointment
            request.env['wb.app'].sudo().create({
                'patient_id': patient.id,
                'date': date,
                'reason': reason
            })


        return request.redirect('/patient/info')
