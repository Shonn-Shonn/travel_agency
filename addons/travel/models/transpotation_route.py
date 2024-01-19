from odoo import api, fields, models 

class TranspotationRoute(models.Model):
    _name = 'transpotation.route'
    _description = 'TranspotationRoute'
    
    travel_agency_id = fields.Many2one('travel.agency',required=True)
    travel_car_id = fields.Many2one('travel.car')
    avatar = fields.Image(related='travel_car_id.avatar')
    car_driver = fields.Many2one('res.partner',related="travel_car_id.car_driver")
    start_datetime = fields.Datetime()
    start_township = fields.Many2one('travel.township')
    start_gate = fields.Many2one('travel.gate')
    arrive_datetime = fields.Datetime()
    arrive_township = fields.Many2one('travel.township')
    arrive_gate = fields.Many2one('travel.gate')
