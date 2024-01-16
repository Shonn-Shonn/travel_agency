from odoo import api, fields, models 
from odoo.exceptions import UserError

class ChangeDriverWizard(models.TransientModel):
    _name = 'change.driver.wizard'
    _description = 'Change Driver Wizard'

    car_driver = fields.Many2one('res.partner',required=True,string="Driver Name")
    join_date = fields.Date(string="Joining Date",default= lambda self:fields.Date.today())

    def change_driver(self):
        context =  self.env.context
        active_model = context.get('active_model')
        active_id = context.get('active_id')
        travel_card_id = self.env[active_model].browse(active_id)
        if self.car_driver == travel_card_id.car_driver:
            raise UserError('Change Driver should not be the same!')
        values = {
              "travel_car_id" : travel_card_id.id,
              "car_driver" : travel_card_id.car_driver.id,
              "join_date" : travel_card_id.join_date,
              "fired_date" : fields.Date.today(),

        }
        self.env['travel.driver.history'].create(values)
        travel_card_id.car_driver = self.car_driver
        travel_card_id.join_date = self.join_date
    
        

    
    
