from odoo import http
from odoo.http import request
import json

class DirectorAssign(http.Controller):
    @http.route('/director', auth='public', type='json', csrf=False)
    def director(self, **kw):
        #kerkohet nese ka apiKey
        api_key = request.httprequest.headers.get('Authorization')
        if not api_key:
            return {'Success': False, 'Message': 'Api key needed'}

        api_key = api_key.replace('Bearer ', '')

        #verifikohet nqs apikey i perket director apo jo
        director = request.env['wb.director'].sudo().search([('api_key', '=', api_key)])
        if not director:
            return {'Success': False, 'Message': 'This page can only be accessed only by directors'}

        try:
            json_data = json.loads(request.httprequest.data)
        except json.JSONDecodeError:
            return {'Success': False, 'Message': 'Invalid JSON data'}

        patient_id = json_data.get('patient_id')
        doctor_id = json_data.get('doctor_id')

        if not patient_id:
            return {'Success': False, 'Message': 'Patient id  not found'}

        if not doctor_id:
            return {'Success': False, 'Message': 'Doctor id not found'}

        Patient = request.env['wb.patient'].sudo()
        Doctor = request.env['wb.doctor'].sudo()

        patient = Patient.browse(patient_id)
        doctor = Doctor.browse(doctor_id)

        if not patient.exists():
            return {'Success': False, 'Message': 'Patient does not exists'}

        if not doctor.exists():
            return {'Success': False, 'Message': 'Doctor does not exists'}

        patient.doctor_id = doctor_id
        json_response = {
            'patient_name' : patient.name,
            'doctor_name' : doctor.name
        }
        return {'Success': True, 'Message': 'Doctor assigned successfully', 'data': json_response}

    @http.route('/appointments', type='http', auth='public', methods=['GET'], csrf=False)
    def get_appointments(self, **kw):
        api_key = request.httprequest.headers.get('Authorization')
        if not api_key:
            return http.request.make_response(
                json.dumps({'Success': False, 'Message': 'Api key needed'}),
                headers=[('Content-Type', 'application/json')]
            )

        api_key = api_key.replace('Bearer ', '')

        # Verify if the API key belongs to a director
        director = request.env['wb.director'].sudo().search([('api_key', '=', api_key)])
        if not director:
            return http.request.make_response(
                json.dumps({'Success': False, 'Message': 'This page can only be accessed by directors'}),
                headers=[('Content-Type', 'application/json')]
            )

        appointments = request.env['wb.app'].sudo().search([])
        appointment_list = []
        for appointment in appointments:
            appointment_list.append({
                'id': appointment.id,
                'patient': appointment.patient_id.name,
                'date': appointment.date.strftime('%Y-%m-%d') if appointment.date else None,
                'reason': appointment.reason,
                'doctor_id': appointment.doctor_id.id,
            })
        return http.request.make_response(
            json.dumps(appointment_list),
            headers=[('Content-Type', 'application/json')]
        )


    @http.route('/blood/bank', type='http', csrf=False, methods=['GET'], auth='public')
    def get_blood_bank(self, **kwargs):
        #kerkohet APIkey
        api_key = request.httprequest.headers.get('Authorization')
        if not api_key:
            return http.request.make_response(
                json.dumps({'Success': False, 'Message': 'API key needed'}),
                headers=[('Content-Type', 'application/json')]
            )

        api_key = api_key.replace('Bearer ', '')

        #verifikohet nese api_key eshte i directorit apo jo
        director = request.env['wb.director'].sudo().search([])
        if not director:
            return http.request.make_response(
                json.dumps({"Success": False, "Message": 'This page can only be accessed by directors'}),
                headers=[('Content-Type', 'application/json')]
            )

        blood_bank = request.env['wb.blood'].sudo().search([])
        blood_bank_list = []
        for blood in blood_bank:
            blood_bank_list.append({
                'donor_name': blood.name,
                'donor_last_name': blood.last_name,
                'donor_blood_group': blood.blood_group,
                'patient': blood.patient_id.name
            })

        return http.request.make_response(
            json.dumps(blood_bank_list),
            headers=[('Content-Type', 'application/json')]
        )



    @http.route('/all/reception', type='http', auth='public', methods=['GET'], csrf=False)
    def get_all_reception(self, **kwargs):
        #kerkohet apikey
        api_key = request.httprequest.headers.get('Authorization')
        if not api_key:
            return http.request.make_response(
                json.dumps({'Success': False, 'Message': 'Api key needed'}),
                headers=[('Content-Type', 'application/json')]
            )

        api_key = api_key.replace('Bearer ', '')

        #verifikohet nqs api_key eshte i directorit
        director = request.env['wb.director'].sudo().search([('api_key', '=', api_key)])
        if not director:
            return http.request.make_response(
                json.dumps({"Success": False, "Message": "This page can only be accessed by directors"}),
                headers=[('Content-Type', 'application/json')]
            )

        receptionists = request.env['wb.reception'].sudo().search([])
        receptionist_list = []
        for receptionist in receptionists:
            receptionist_list.append({
                'name': receptionist.name,
                'last_name': receptionist.last_name,
                'gender': receptionist.gender,
                'reception_number': receptionist.rec_number
            })

        return http.request.make_response(
            json.dumps(receptionist_list),
            headers=[('Content-Type', 'application/json')]
        )

    @http.route('/patient/tests', auth='public', type='http', csrf=False, methods=['GET'])
    def get_patient_tests(self, **kwargs):
        #kerkohet nje apiKey
        api_key = request.httprequest.headers.get('Authorization')
        if not api_key:
            return http.request.make_request(
                json.dumps({'Success': False, 'Message': 'Api key needed'}),
                headers=[('Content-Type', 'application/json')]
            )

        api_key = api_key.replace('Bearer ', '')

        #verifikojme nese ky apiKEY eshte i directorit
        director = request.env['wb.director'].sudo().search([('api_key', '=', api_key)])
        if not director:
            return http.request.make_response(
                json.dumps({'Success': False, 'Message': 'This page can only be accessed by directors'}),
                headers=[('Content-Type', 'application/json')]
            )

        patient_tests = request.env['patient.test'].sudo().search([])
        patient_tests_list = []
        for test in patient_tests:
            lab_tests = [{'id': lab.id, 'name': lab.test_name, 'type': lab.type, 'price': lab.price}for lab in test.lab_test_id]
            patient_tests_list.append({
                'patient': test.patient_id.name if test.patient_id else None,
                'doctor': test.doctor_id.name if test.doctor_id else None,
                'date': test.date.strftime('%Y-%m-%d') if test.date else None,
                'tests': lab_tests
            })

        return http.request.make_response(
            json.dumps(patient_tests_list),
            headers=[('Content-Type', 'application/json')]
        )
