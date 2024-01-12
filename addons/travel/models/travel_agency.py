from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class TravelAgency(models.Model):
    _name = 'travel.agency'
    _inherit = 'mail.thread'
    _description = 'TravelAgency'

    name = fields.Char(tracking=True)
    reference = fields.Char(tracking=True,default=lambda self:_("New"),copy=False)
    line_no = fields.Char(tracking=True)

    _sql_constraints = [
        ('line_no_uniq', 'CHECK(1=1)',
         'Liscense number must be unique.')
    ]

    @api.constrains('name')
    def _check_name(self):
        domain = [('id', '!=', self.id)]
        if self.name in self.search(domain).mapped('name'):
            raise ValidationError(_("Agency name is already created!"))
    
    @api.model
    def create(self, values):
        # Add code here
        if values.get('reference', _('New')) == _('New'):
            values['reference'] = self.env['ir.sequence'].next_by_code('travel.agency') or _('New')
        if not values.get('reference'):
            values['reference'] = 100
        return super(TravelAgency, self).create(values)
