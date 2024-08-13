from odoo import http
from odoo.http import request

class WebBlood(http.Controller):
    @http.route('/blood/form', type='http', auth='user', website=True)
    def index(self):
        return request.render('hospital_management.blood_template')

    @http.route('/blood/create', type='http', auth='user', website=True)
    def create_blood_donation(self, **kw):

        name = request.params.get('name')
        date = request.params.get('date')
        blood_group = request.params.get('blood_group')

        if name and date and blood_group:
            request.env['wb.blood'].sudo().create({
                'name': name,
                'date': date,
                'blood_group': blood_group,
            })

        return request.redirect('/merci')
