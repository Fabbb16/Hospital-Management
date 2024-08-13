from odoo import fields, models

class BloodBank(models.Model):
    _name = 'wb.blood'
    _description = 'THis a blood model'

    name = fields.Char(string='Donor Name')
    last_name = fields.Char(string='Donor Last Name')
    date = fields.Date(string='Date')
    blood_group = fields.Selection([
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-')
    ], string='Blood Group')
    patient_id = fields.Many2one('wb.patient', string='Receiver')
    lab_id = fields.Many2one('wb.labs', string='Lab')