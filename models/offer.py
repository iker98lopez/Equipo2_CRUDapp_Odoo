# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError 
class Offer(models.Model):
    _name = 'offer_stats.offer'

    shop = fields.Char(string="Shop", required=True, help="The shop making the offer")
    basePrice = fields.Float(string="Base price", digits="6,2")
    discountedPrice = fields.Float(string="Discounted price", digits="6,2")
    discount = fields.Float(string="Discount %", digits="2,0")
    software = fields.Many2one("offer_stats.software", String="Software")
    
    @api.constrains('basePrice')
    def _check_basePrice_range(self):
        for record in self:
            if record.basePrice < 0 or record.basePrice > 999:
                raise ValidationError("Base price must be bigger than 0 and lower than 1000")
            
    @api.constrains('discount')
    def _check_discount_range(self):
        for record in self:
            if record.discount < 0 or record.discount > 100:
                raise ValidationError("Discount % must be bigger than 0 and lower than 100")
            
    @api.constrains('software')
    def _check_basePrice_range(self):
        for record in self:
            if record.software is not None:
                raise ValidationError("Offer software must exist")
    #@api.depends('value')
    #def _value_pc(self):
    #    self.value2 = float(self.value) / 100