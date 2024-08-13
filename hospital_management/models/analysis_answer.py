from odoo import fields, models

class AnalysisAnswer(models.Model):
    _name = 'wb.answer'
    _description = 'This is an answer model'

    file = fields.Binary(string='Analysis Answer')
    file_name = fields.Char(string='Binary File Name')
    patient_id = fields.Many2one('wb.patient', string='Patient')
    description = fields.Text(string='Description')
    partner_id = fields.Many2one('res.partner', string='Partner')
