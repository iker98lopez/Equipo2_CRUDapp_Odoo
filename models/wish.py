# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError 
class Wish(models.Model):
    _name = 'offer_stats.wish'
    wish_id= fields.Integer(string="Wish_ID")
    software_id = fields.Many2one('offer_stats.software', string="Software_ID", required=True)
    min_price = fields.Float(digits=(5, 2), help='Minimum price to be notified')
    
    @api.constrains('min_price')
    def _check_min_price_range(self):
        for record in self:
            if record.min_price < 0 or record.min_price > 999:
                raise ValidationError("Minimum price must be bigger than 0 and lower than 1000")
            
    @api.constrains('software_id')
    def _check_software_exists(self):
        for record in self:
            exist = false
            for record2 in record.software_id:
                if record.software_id == record2:
                    exist = true
                    break
            if not exist:
                raise ValidationError("Software must exist")
            
    @api.constrains('wish_id')
    def _check_wish_id(self):
        for record in self:
            if record.wish_id <= 0:
                raise ValidationError("Base price must be bigger than 0 and lower than 1000")
            else:
                for record2 in self:
                    if record2.wish_id == record.wish_id:
                        raise ValidationError("Wish id must not exist")
    #@api.depends('value')
    #def _value_pc(self):
    #    self.value2 = float(self.value) / 100