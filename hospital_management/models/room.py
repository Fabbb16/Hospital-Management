from odoo import fields, models

class Room(models.Model):
    _name = 'wb.room'
    _description = 'This is a room model'

    name = fields.Char(string='Name', help='Name of the room')
    patient_id = fields.Many2one('wb.patient', string='Patient')
    bed_type = fields.Selection([
        ('1', 'Gatch Bed'),
        ('2', 'Electric'),
        ('3', 'Stretcher'),
        ('4', 'Low Bed'),
        ('5', 'Low Air Loss'),
        ('6', 'Clinitron')
    ], string='Bed Type')
    currency_id = fields.Many2one('res.currency', string='Currency')
    rent = fields.Monetary(string='Rent', help='Rent for the room')
    floor_number = fields.Integer(string='Floor No')
    nurse_id = fields.Many2one('wb.nurse',string='Nurse', help='Nurse who is responsible for this room')
    state = fields.Selection([
        ('free', 'Free'),
        ('taken', 'Taken')
    ])