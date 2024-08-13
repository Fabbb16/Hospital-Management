from odoo import fields, models

class PatientAppointment(models.Model):
    _name = 'wb.app'
    _description = 'This is an appointment model'

    patient_id = fields.Many2one('wb.patient', string='Patient')
    date = fields.Date(string='Date')
    reason = fields.Text(string='Reason')
    doctor_id = fields.Many2one('wb.doctor', string='Doctor')
    room_id = fields.Many2one('wb.room', string='Room')
    file = fields.Binary(string='Patient Analysis')