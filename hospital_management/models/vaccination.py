from odoo import fields, models

class Vaccination(models.Model):
    _name = 'wb.vaccination'
    _description = 'This is a vaccination model'

    patient_id = fields.Many2one('wb.patient', string='Patient')
    vaccine_id = fields.Many2one('wb.vaccine', string='Vaccine')
    currency_id = fields.Many2one('res.currency', string='Currency')
    price = fields.Monetary(string='Price')
    dose = fields.Float(string='Dose', help='Dose of the vaccine')
    date = fields.Date(string='Date')
    certificate = fields.Binary(string='Certificate')
    recurring_vaccine = fields.Boolean(string='Recurring Vaccine')

