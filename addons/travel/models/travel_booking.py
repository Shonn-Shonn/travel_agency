from odoo import api, fields, models

class TravelBooking(models.Model):
    _name = 'travel.booking'
    _description = 'TravelBooking'

    partner_ids = fields.Many2many('res.partner')
    travel_agency_id = fields.Many2one('travel.agency')
    travel_car_id = fields.Many2one('travel.car', domain="[('travel_agency_id','=',travel_agency_id)]")


