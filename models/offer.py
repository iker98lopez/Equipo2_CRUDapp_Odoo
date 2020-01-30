# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError 
class Offer(models.Model):
    _name = 'offer_stats.offer'

    shop = fields.Char(string="Shop", required=True, help="The shop making the offer")
    basePrice = fields.Float(string="Base price", digits=(5,2))
    discountedPrice = fields.Float(string="Discounted Price", digits=(5,2))
    discount = fields.Float(string="Discount", digits=(3,0))
    software = fields.Many2one("offer_stats.software", string="Software", required=True)
    
    #@api.constrains('basePrice')
    #def _check_baseprice_range(self):
     #   for record in self:
    #        if record.basePrice < 0 or record.basePrice > 999:
    #            raise ValidationError("Base price must be bigger than 0 and lower than 1000")
            
    #@api.constrains('discount')
    #def _check_discount_range(self):
    #    for record in self:
    #        if record.discount < 0 or record.discount > 100:
    #            raise ValidationError("Discount % must be bigger than 0 and lower than 100")
            
    #@api.constrains('software')
    #def _check_software_exists(self):
    #    for record in self:
    #        if record.software is None:
    #            raise ValidationError("Offer software must exist")