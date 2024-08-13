from odoo import fields, models

class PatientTest(models.Model):
    _name = 'patient.test'
    _description = 'This is a patient.test model'

    patient_id = fields.Many2one('wb.patient',string='Patient')
    doctor_id = fields.Many2one('wb.doctor',string='Doctor')
    date = fields.Date(string="Date")
    lab_test_id = fields.Many2many('wb.lab',string='Lab Test')
