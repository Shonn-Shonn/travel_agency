from odoo import api, fields, models 


class Township(models.Model):
    _name = 'travel.township'
    _description = 'Township'

    name = fields.Char()
    

    
