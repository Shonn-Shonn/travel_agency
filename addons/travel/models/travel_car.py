from odoo import api, fields, models

class TravelCar(models.Model):
    _name = 'travel.car'
    _description = 'TravelCar'

    car_number = fields.Char()
    travel_agency_id = fields.Many2one('travel.agency',required=True)

    def name_get(self):
        return [(rec.id,f"{rec.car_number}({rec.travel_agency_id.name})")for rec in self]
