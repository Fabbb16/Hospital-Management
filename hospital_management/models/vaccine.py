from odoo import fields, models

class Vaccine(models.Model):
    _name = 'wb.vaccine'
    _description = 'THis is a vaccine model'

    name = fields.Char(string='Name', help='Name of the vaccine')
    pharmacy_id = fields.Many2one('wb.pharmacy', string='Pharmacy')
    expiration_date = fields.Date(string='Expiration Date')