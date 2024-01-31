from odoo import api, fields, models

class TravelBooking(models.Model):
    _name = 'travel.booking'
    _description = 'TravelBooking'

    partner_ids = fields.Many2many('res.partner')
    transpotation_route_id = fields.Many2one('transpotation.route', domain="[('state','=','confirm')]")
    travel_agency_id = fields.Many2one('travel.agency')
    travel_car_id = fields.Many2one('travel.car', domain="[('travel_agency_id','=',travel_agency_id)]")
    company_id  = fields.Many2one('res.company', default= lambda self: self.env.user.company_id.id)
    currency_id = fields.Many2one('res.currency',related='company_id.currency_id')
    total_amount = fields.Monetary(compute="_compute_total_amount")
    seat = fields.Integer(related="travel_car_id.seat")
    per_seat = fields.Monetary(related="transpotation_route_id.per_seat")

    @api.depends('partner_ids', 'per_seat')
    def _compute_total_amount(self):
        for rec in self:
            rec.total_amount = len(rec.partner_ids) * rec.per_seat


