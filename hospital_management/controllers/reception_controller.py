from odoo import http
from odoo.http import request
import json

class Reception(http.Controller):
    @http.route('/reception', type='json', auth='public', csrf=False)
    def reception(self, **kw):
        #kerkojm apikey
        api_key = request.httprequest.headers.get('Authorization')
        if not api_key:
            return {'Success': False, 'Message': 'Api key needed'}

        api_key = api_key.replace('Bearer ', '')

        #verifikohet nese apikey esht i nje recepsionisti
        receptionist = request.env['wb.reception'].sudo().search([('api_key', '=', api_key)])
        if not receptionist:
            return {'Success': False, 'Message': 'This page can only be accessed by receptionists'}

        try:
            json_data = json.loads(request.httprequest.data)
        except json.JSONDecodeError:
            return {'Success': False, 'Message': 'Invalid JSON data'}

        appointment_id = json_data.get('appointment_id')
        doctor_id = json_data.get('doctor_id')

        if not appointment_id:
            return {'Success': False, 'Message': 'Appointment id not found'}

        if not doctor_id:
            return {'Success': False, 'Message': 'Doctor id not found'}

        Appointment = request.env['wb.app'].sudo()
        Doctor = request.env['wb.doctor'].sudo()

        appointment = Appointment.browse(appointment_id)
        doctor = Doctor.browse(doctor_id)

        if not appointment.exists():
            return {'Success': False, 'Message': 'This appointment does not exists'}

        if not doctor.exists():
            return {'Success': False, 'Message': 'This doctor does not exists'}


        appointment.doctor_id = doctor_id

        json_response = {
            'appointment_id' : appointment.id,
            'doctor_name' : doctor.name
        }
        return {'Success': True, 'Message': 'Doctor assigned successfully!!!', 'data': json_response}



    @http.route('/reception/doc', type='json', csrf=False, auth='public')
    def lab_reception(self, **kw):
        #kerkojme apiKey nqs ka ose ska
        api_key = request.httprequest.headers.get('Authorization')
        if not api_key:
            return {'Success': False, 'Message': 'Api key needed'}

        api_key = api_key.replace('Bearer ', '')

        #verifikojme nese ky key esht i recepsionistit
        receptionist = request.env['wb.reception'].sudo().search([('api_key', '=', api_key)])
        if not receptionist:
            return {'Success': False, 'Message': 'This page can only be accessed by receptionists'}

        try:
            json_data = json.loads(request.httprequest.data)
        except json.JSONDecodeError:
            return {'Success': False, 'Message': 'Invalid JSON data'}

        doctor_id = json_data.get('doctor_id')
        patient_lab_id = json_data.get('patient_lab_id')

        if not doctor_id:
            return {'Success': False, 'Message': 'Invalid Doctor id'}

        if not patient_lab_id:
            return {'Success': False, 'Message': 'Invalid Patient test id'}

        Doctor = request.env['wb.doctor'].sudo()
        Patient_lab = request.env['patient.test'].sudo()

        doctor = Doctor.browse(doctor_id)
        patient_lab = Patient_lab.browse(patient_lab_id)

        if not doctor.exists():
            return {'Success': False, 'Message': 'Doctor does not exists'}

        if not patient_lab.exists():
            return {'Success': False, 'Message': 'Patient test does not exists'}

        patient_lab.doctor_id = doctor_id

        json_response = {
            'doctor_name' : f"Doctor {doctor.name}",
        }

        return {'Success': True, 'Message': 'Doctor assigned successfully!', 'data': json_response}


    class WebAnswer(http.Controller):
        @http.route('/assign/analysis', type='json', auth='public', csrf=False)
        def assign_analysis(self, **kwargs):
            # Get the API key from headers
            api_key = request.httprequest.headers.get('Authorization')
            if not api_key:
                return {'Success': False, 'Message': 'API key needed'}

            api_key = api_key.replace('Bearer ', '')

            # Verify if the API key belongs to a receptionist
            reception = request.env['wb.reception'].sudo().search([('api_key', '=', api_key)])
            if not reception:
                return {'Success': False, 'Message': 'This page can only be accessed by reception'}

            try:
                json_data = json.loads(request.httprequest.data)
            except json.JSONDecodeError:
                return {'Success': False, 'Message': 'Invalid JSON data'}

            patient_id = json_data.get('patient_id')
            file_id = json_data.get('file_id')

            if not patient_id:
                return {'Success': False, 'Message': 'Invalid patient ID'}

            if not file_id:
                return {'Success': False, 'Message': 'Invalid file ID'}

            Patient = request.env['wb.patient'].sudo()
            File = request.env['wb.answer'].sudo()

            patient = Patient.browse(patient_id)
            file = File.browse(file_id)

            if not patient.exists():
                return {'Success': False, 'Message': 'Patient does not exist'}

            if not file.exists():
                return {'Success': False, 'Message': 'File does not exist'}

            # Make sure patient has the correct field to store the file ID or file content
            # Assuming `file` field is of type `Binary` in `wb.patient` model
            patient.write({
                'file': file.file,  # If `file` field is Binary
                'file_name': file.file_name  # Assuming you also want to store the file name
            })

            json_response = {
                'name': patient.name,
                'file_name': file.file_name
            }

            return {'Success': True, 'Message': 'Analysis assigned successfully', 'data': json_response}
