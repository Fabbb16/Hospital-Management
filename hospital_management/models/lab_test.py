from odoo import fields, models

class LabTest(models.Model):
    _name = 'wb.lab'
    _description = 'This is a lab model'

    test_name = fields.Char(string='Test', help='Test name')
    results = fields.Datetime(string='Results within')
    type = fields.Selection([
        ('1', 'Range'),
        ('2', 'Objective')
    ], string='Type')
    currency_id = fields.Many2one('res.currency', string='Currency')
    price = fields.Monetary(string='Price')
    lab_id = fields.Many2one('wb.labs',string='Lab')