from odoo import fields, models

class Family(models.Model):
    _name = 'wb.family'
    _description = 'This is a family model'

    name = fields.Char(string='Name')
    relation = fields.Char(string='Relation')
    age = fields.Integer(string='Age')
    diseased = fields.Boolean(string='Diseased')

    # Define a Many2one field pointing to itself
    family_id = fields.Many2one('wb.patient', string='Family')
