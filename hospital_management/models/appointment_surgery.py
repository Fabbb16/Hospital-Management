from odoo import fields, models

class SurgeryAppointment(models.Model):
    _name = 'wb.surgery'
    _description = 'This is a surgery model'

    name_of_the_surgery = fields.Char(string='Name', help='Name of the surgery')
    operating_doctor = fields.Many2one('wb.doctor', string='Doctor', help='Operating Docotr')
    operating_date = fields.Date(string='Operating Date')
    duration = fields.Float(string='Duration (Hours)', help="Duration of the appointment in hours")
    patient = fields.Many2one('wb.patient', string='Patient')
