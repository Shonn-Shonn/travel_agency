from odoo import api, fields, models

class TownshipGate(models.Model):
    _name = 'travel.gate'
    _description = 'TownshipGate'

    name = fields.Char(required=True)
    township_id = fields.Many2one('travel.township')
