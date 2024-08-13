from odoo import fields, models

class Doctor(models.Model):
    _name = 'wb.doctor'
    _description = 'This is a doctor model'

    name = fields.Char(string='Name')
    last_name = fields.Char(string='Last Name')
    date_of_birth = fields.Date(string='Date of Birth')
    department = fields.Selection([
        ('cardiology', 'Cardiology'),
        ('neurology', 'Neurology'),
        ('orthopedics', 'Orthopedics'),
        ('pediatrics', 'Pediatrics'),
        ('radiology', 'Radiology'),
        ('surgery', 'Surgery')
    ])
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')

    #Profession info

    qualification = fields.Char(string='Qualification')
    specialization = fields.Char(string='Specialization')
    years_of_experience = fields.Char(string='Years of Experience')

    #Work schedue

    working_days = fields.Selection([
        ('1-3', '1-3 Days'),
        ('2-5', '3-5 Days'),
        ('7', '7 Days')
    ], string='Working Days')
    working_hours = fields.Integer(string='Working Hours', help='per day')


    #Additional Info
    photo = fields.Binary(string='Photo')
    gender = fields.Selection([
        ('1', 'Female'),
        ('2', 'Male')
    ])
    notes = fields.Text(string='Notes')

    api_key = fields.Char(string='Key')
