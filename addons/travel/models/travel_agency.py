from odoo import api, fields, models

class TravelAgency(models.Model):
    _name = 'travel.agency'
    _description = 'TravelAgency'

    name = fields.Char()
    reference = fields.Char()
    line_no = fields.Char()

