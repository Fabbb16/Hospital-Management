from odoo import http
from odoo.http import request
import json


class DocHospital(http.Controller):
    # @http.route('/hospital', auth='public', csrf=False)
    # def index(self, **kw):
    #     return 'Hello World'


    @http.route('/hospital', auth='public', type='json', csrf=False)
    def index(self, **kw):
        #Kerkon nese perdoret apiKey
        api_key = request.httprequest.headers.get('Authorization')
        if not api_key:
            return {'Success': False, 'Message': 'Api key needed'}

        api_key = api_key.replace('Bearer ', '')

        #kontroollon nese ky api_key i perket doktorrit apo jo
        doctor = request.env['wb.doctor'].sudo().search([('api_key', '=', api_key)])
        if not doctor:
            return {'Success': False, 'Message': 'This page can only be accessed by doctors'}


        try:
            json_data = json.loads(request.httprequest.data)
        except json.JSONDecodeError:
            return {'Success': False, 'Message': 'Invalid JSON data'}


        patient_id = json_data.get('patient_id')
        room_id = json_data.get('room_id')

        if not patient_id:
            return {'Success': False, 'Message': 'Patient not found'}
        if not room_id:
            return {'Success': False, 'Message': 'Room not found'}

        Patient = request.env['wb.patient'].sudo()
        Room = request.env['wb.room']

        patient = Patient.browse(patient_id)
        room = Room.browse(room_id)

        if not patient.exists():
            return {'Success': False, 'Message': 'Patient does not exist'}
        if not room.exists():
            return {'Success': False, 'Message': 'Room does not exist'}

        room.patient_id = patient_id
        room_json = {
            'id': room.id,
            'name': patient.name
        }
        return {'Success': True, 'Message': 'Patient assigned successfully!', 'data': room_json}

    @http.route('/hospital/nurse', type='json', auth='public', csrf=False)
    def nurse(self, **kw):
        #kerkon nese perdoret apiKey
        api_key = request.httprequest.headers.get('Authorization')
        if not api_key:
            return {'Success': False, 'Message': 'Api Key needed'}

        api_key = api_key.replace('Bearer ', '')

        #verifikon nese eshte doktorr apo jo--> personi qe hyn n endpoint n baz te api_key
        doctor = request.env['wb.doctor'].sudo().search([('api_key', '=', api_key)])
        if not doctor:
            return {'Success': False, 'Message': 'This page can only be accessed by doctors'}

        try:
            json_data = json.loads(request.httprequest.data)
        except json.JSONDecodeError:
            return {'Success': False, 'Message': 'Invalid JSON data'}

        room_id = json_data.get('room_id')
        nurse_id = json_data.get('nurse_id')

        if not room_id:
            return {'Success': False, 'Message': 'Room id not found'}

        if not nurse_id:
            return {'Success': False, 'Message': 'Nurse id not found'}

        Room = request.env['wb.room'].sudo()
        Nurse = request.env['wb.nurse'].sudo()

        room = Room.browse(room_id)
        nurse = Nurse.browse(nurse_id)

        if not room.exists():
            return {'Success': False, 'Message': 'Room not found'}

        if not nurse.exists():
            return {'Success': False, 'Message': 'Nurse not found'}


        #sepse nurse_id esht M2O field te modeli wb.room
        room.nurse_id = nurse_id

        json_response = {
            'room_name': room.name,
            'nurse_name': nurse.name
        }
        return {'Success': True, 'Message': 'Nurse assigned successfully!!', 'data': json_response}



    @http.route('/blood', type='json', auth='public', csrf=False)
    def blood(self, **kw):
        #kerkojm apikey nese ka apo ska
        api_key = request.httprequest.headers.get('Authorization')
        if not api_key:
            return {'Success': False, 'Message': 'Api key needed'}

        api_key = api_key.replace('Bearer ','')

        #verifikojm nese apikey eshte  nje doktorri apo jo
        doctor = request.env['wb.doctor'].sudo().search([('api_key', '=', api_key)])
        if not doctor:
            return {'Success': False, 'Message':'This page can only be accessed by doctors'}

        try:
            json_data = json.loads(request.httprequest.data)
        except json.JSONDecodeError:
            return {'Success': False, 'Message': 'Invalid JSON data'}

        patient_id = json_data.get('patient_id')
        blood_id = json_data.get('blood_id')

        if not patient_id:
            return {'Success': False, 'Message': 'Patient id not found'}

        if not blood_id:
            return {'Success': False, 'Message': 'Blood id not found'}

        Patient = request.env['wb.patient'].sudo()
        Blood = request.env['wb.blood'].sudo()

        patient = Patient.browse(patient_id)
        blood = Blood.browse(blood_id)

        if not patient.exists():
            return {'Success': False, 'Message': 'Patient does not exists'}

        if not blood.exists():
            return {'Success': False, 'Message': 'Blood Bank does not exists'}

        blood.patient_id = patient_id

        json_response = {
            'patient_name': patient.name
        }

        return {'Success': True, 'Message': 'Patient assigned successfully', 'data': json_response}


    @http.route('/pharmacy', type='json', auth='public', csrf=False)
    def pharmacy(self, **kw):
        #verifikojme nese ka apo jo apiKey
        api_key = request.httprequest.headers.get('Authorization')
        if not api_key:
            return {'Success': False, 'Message': 'Api key needed'}

        api_key = api_key.replace('Bearer ', '')

        #verifikojme nese ky api_key esht i dokut apo jo
        doctor = request.env['wb.doctor'].sudo().search([('api_key', '=', api_key)])
        if not doctor:
            return {'Success': False, 'Message': 'This page can only be accessed by doctors'}

        try:
            json_data = json.loads(request.httprequest.data)
        except json.JSONDecodeError:
            return {'Success': False, 'Message': 'Invalid JSON data'}

        vaccine_id = json_data.get('vaccine_id')
        pharmacy_id = json_data.get('pharmacy_id')

        if not vaccine_id:
            return {'Success': False, 'Message': 'Vaccine id not found'}

        if not pharmacy_id:
            return {'Success': False, 'Message': 'Pharmacy id not found'}

        Vaccine = request.env['wb.vaccine'].sudo()
        Pharmacy = request.env['wb.pharmacy'].sudo()

        vaccine = Vaccine.browse(vaccine_id)
        pharmacy = Pharmacy.browse(pharmacy_id)

        if not vaccine.exists():
            return {'Success': False, 'Message': 'Vaccine does not exists'}

        if not pharmacy.exists():
            return {'Success': False, 'Message': 'Pharmacy does not exists'}

        vaccine.pharmacy_id = pharmacy_id

        json_response = {
            'pharmacy_name': f"Pharmacy: {pharmacy.name}",
            'vaccine_name': f"Vaccine: {vaccine.name}"
        }

        return {'Success': True, 'Message': 'Pharmacy assigned successfully!!!', 'data': json_response}
