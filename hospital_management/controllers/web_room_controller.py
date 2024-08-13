from odoo import http
from odoo.http import request


class WebRoom(http.Controller):
    @http.route('/hospital/rooms', type='http', auth='user', website=True)
    def index(self):
        rooms = request.env['wb.room'].sudo().search([])
        return request.render('hospital_management.room_template', {'rooms':rooms})