from odoo import fields, models

class Nurse(models.Model):
    _name = 'wb.nurse'
    _description = 'This is a nurse model'

    name = fields.Char(string='Name')
    last_name = fields.Char(string='Last Name')
    day_of_birth = fields.Date(string='Date of Birth')
    gender = fields.Selection([
        ('1', 'Female'),
        ('2', 'Male')
    ])
    emergency_number = fields.Char(string='Emergency Number')
    doctor_id = fields.Many2one('wb.doctor', string='Doctor', help='Doctor who is responsible for this nurse')