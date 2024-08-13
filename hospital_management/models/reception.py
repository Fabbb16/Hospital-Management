from odoo import fields, models

class Reception(models.Model):
    _name = 'wb.reception'
    _description = 'This is a reception model'

    name = fields.Char(string='Name')
    last_name = fields.Char(string='Last Name')
    b_day = fields.Date(string='Birthday')
    gender = fields.Selection([
        ('female', 'Female'),
        ('male', 'Male')
    ])
    rec_number = fields.Char(string='Number', help='THis is the receptionist number')
    work_shift = fields.Selection([
        ('day', 'Day'),
        ('night', 'Night')
    ])
    api_key = fields.Char(string='Key')