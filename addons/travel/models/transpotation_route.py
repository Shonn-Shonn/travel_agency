from odoo import api, fields, models 
from odoo.exceptions import UserError

class TranspotationRoute(models.Model):
    _name = 'transpotation.route'
    _description = 'TranspotationRoute'
    
    travel_agency_id = fields.Many2one('travel.agency',required=True)
    logo = fields.Image(related='travel_agency_id.logo')
    transpotation_route_line_ids = fields.One2many('transpotation.route.line', 'transpotation_route_id')
    travel_car_id = fields.Many2one('travel.car',domain="[('travel_agency_id','=',travel_agency_id)]")
    avatar = fields.Image(related='travel_car_id.avatar')
    car_driver = fields.Many2one('res.partner',related="travel_car_id.car_driver")
    avatar = fields.Image(related="travel_car_id.avatar")
    seat = fields.Integer(related="travel_car_id.seat")
    company_id = fields.Many2one('res.company', default=lambda self: self.env.user.company_id.id)
    currency_id = fields.Many2one('res.currency',related="company_id.currency_id")
    per_seat = fields.Monetary()
    starting_date = fields.Datetime()
    starting_township = fields.Many2one('travel.township')
    starting_gate = fields.Many2one('travel.gate',domain="[('township_id','=',starting_township)]")
    arriving_date = fields.Datetime()
    arriving_township = fields.Many2one('travel.township')
    arriving_gate = fields.Many2one('travel.gate')
    state = fields.Selection([
        ('draft','Draft'),
        ('running','Running'),
        ('confirm','Confirm')
    ],default="running")


    def name_get(self):
        return [(rec.id,f"{rec.travel_car_id.car_number}({rec.travel_agency_id.name}-{rec.starting_date})")for rec in self]
    
    @api.onchange('travel_agency_id')
    def _change_travel_agency_id(self):
        if self.travel_agency_id:
            self.travel_car_id = False
            
    @api.onchange('starting_township')
    def _change_starting_township(self):
        if self.starting_township:
            self.starting_gate = False 
            
    @api.onchange('arriving_township')
    def _change_arriving_township(self):
        if self.arriving_township:
            self.arriving_gate = False

    @api.constrains('starting_date','arriving_date')
    def _change_date_time(self):
        if self.starting_date >= self.arriving_date:
            raise UserError('Starting date time must be less.')   
    
    
    def action_confirm(self):
        self.state = "confirm"

    def action_draft(self):
        self.state = "draft"

    def action_running(self):
        self.state = "running"

class TranspotationRouteLine(models.Model):
    _name = 'transpotation.route.line'
    _description = 'TranspotationRouteLine'

    transpotation_route_id = fields.Many2one('transpotation.route')
    partner_ids = fields.Many2many('res.partner')
    travel_booking_id = fields.Many2one('travel.booking')
    seat_number = fields.Integer()
    company_id = fields.Many2one('res.company', default=lambda self: self.env.user.company_id.id)
    currency_id = fields.Many2one('res.currency',related="company_id.currency_id")
    amount = fields.Monetary(related='travel_booking_id.per_seat')

    @api.constrains('seat_number')
    def _check_seat_number(self):
        seat_numbers = set(range(1,self.transpotation_route_id.seat))
        all_seat_numbers = set(self.transpotation_route_id.transpotation_route_line_ids.filtered(lambda x:x.id != self.id).mapped('seat_number'))
        results = all_seat_numbers - seat_numbers
        if self.seat_number not in results:
            raise  UserError('Seat Booking is already exit.')

