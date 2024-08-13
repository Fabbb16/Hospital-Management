from odoo import fields, models

class ManagingDirector(models.Model):
    _name = 'wb.director'
    _description = 'This is a director model'

    name = fields.Char(string='Name')
    last_name = fields.Char(string='Last Name')
    b_day = fields.Date(string='Birth Day')
    department = fields.Selection([
        ('cardiology', 'Cardiology'),
        ('neurology', 'Neurology'),
        ('orthopedics', 'Orthopedics'),
        ('pediatrics', 'Pediatrics'),
        ('radiology', 'Radiology'),
        ('surgery', 'Surgery')
    ])
    doctor_id = fields.Many2many('wb.doctor', string='Dcotors', help='The list of the doctors who are managed by this director')
    api_key = fields.Char(string='Key')