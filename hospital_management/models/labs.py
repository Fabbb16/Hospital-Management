from odoo import fields, models

class Labs(models.Model):
    _name = 'wb.labs'
    _description = 'This is a lab model'

    name = fields.Char(string='Name')
    mobile = fields.Char(string='Mobile')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    notes = fields.Text(string='Notes')
    type_of_lab = fields.Selection([
        ('1', 'Clinical Chemistry Laboratory'),
        ('2', 'Hematology Laboratory'),
        ('3', 'Microbiology Laboratory'),
        ('4' , 'Pathology Laboratory'),
        ('5', 'Parasitology Laboratory'),
        ('6', 'Virology Laboratory'),
        ('7', 'Blood Bank and Transfusion Services')
    ], string='Type')