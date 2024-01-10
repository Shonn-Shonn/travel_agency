from odoo import api, fields, models

class TownshipGate(models.Model):
    _name = 'travel.gate'
    _description = 'TownshipGate'

    name = fields.Char()
    travel_id = fields.Many2one('travel.township')

