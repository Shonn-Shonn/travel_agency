from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"
    _description = "ResPartner"

    date_of_birth = fields.Date()    