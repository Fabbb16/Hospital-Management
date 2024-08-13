from odoo import models, fields

class Analysis(models.Model):
    _name = 'wb.analysis'
    _description = 'This is an analysis model'

    patient_id = fields.Many2one('wb.patient', string='Patient')
    file = fields.Binary(string='Patient Analysis')
    file_name = fields.Char(string='Binary Field Name')
    date = fields.Date(string='Date')
    notes = fields.Text(string='Notes')