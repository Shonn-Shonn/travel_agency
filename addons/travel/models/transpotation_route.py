from odoo import api, fields, models 

class TranspotationRoute(models.Model):
    _name = 'transpotation.route'
    _description = 'TranspotationRoute'
    
    travel_agency_id = fields.Many2one('travel.agency',required=True)
    travel_car_id = fields.Many2one('travel.car')
    car_driver = fields.Many2one('res.partner',related="travel_car_id.car_driver")
