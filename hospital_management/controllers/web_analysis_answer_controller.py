from odoo import http
from odoo.http import request
import base64

class WebAnswer(http.Controller):
    @http.route('/answer/form', type='http', auth='user', website=True)
    def index(self):
        user = request.env.user
        # Check if the user is an administrator
        if not user.has_group('base.group_system'):
            return request.redirect('/sorry')

        return request.render('hospital_management.answer_template')

    @http.route('/answer/create', type='http', auth='user', website=True)
    def create(self, **kwargs):
        try:
            uploaded_file = request.httprequest.files.get('file')
            description = request.params.get('description')
            patient_id = request.params.get('patient_id')

            if uploaded_file and description and patient_id:
                # Read the content of the file and encode it in base64
                file_content = base64.b64encode(uploaded_file.read())
                file_name = uploaded_file.filename

                # Create the record in the backend
                request.env['wb.answer'].sudo().create({
                    'patient_id' : patient_id,
                    'file': file_content,
                    'file_name': file_name,
                    'description': description
                })

            return request.redirect('/flm')
        except Exception as e:
            return request.redirect('/scusa')



