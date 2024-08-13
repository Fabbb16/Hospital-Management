from odoo import fields, models

class Pharmacy(models.Model):
    _name = 'wb.pharmacy'
    _description = 'This is a pharmacy model'

    name = fields.Char(string='Name', help='Name of the pharmacy')
    ph_name = fields.Char(string="Pharmacist")
    mobile = fields.Char(string='Mobile')
    phone = fields.Char(sttring='Phone')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')