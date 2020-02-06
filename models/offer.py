# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError 

class Offer(models.Model):
    _name = 'offer_stats.offer'

    software = fields.Many2one("offer_stats.software", string="Software", required=True, help="Software being offered")
    shop = fields.Char(string="Shop", required=True, help="The shop making the offer")
    base_price = fields.Float(string="Base price", digits=(5,2), help="Base price of the offer")
    discounted_price = fields.Float(String="Discounted price", compute='_compute_discounted_price', help="Discounted price of the offer")
    discount = fields.Float(string="Discount", digits=(3,0), help="Discount percentage of the offer")
    description = fields.Char(string="Description", help="Brief description of the offer")
    
    @api.depends('base_price', 'discount')
    def _compute_discounted_price(self):
        for record in self:
            record.discounted_price = record.base_price - (record.base_price * record.discount / 100)
    
    @api.constrains('base_price')
    def _check_baseprice_range(self):
       for record in self:
            if record.base_price < 0 or record.base_price > 999:
                raise ValidationError("Base price must be between 0 and 1000")
            
    @api.constrains('discount')
    def _check_discount_range(self):
        for record in self:
            if record.discount < 0 or record.discount > 100:
                raise ValidationError("Discount % must be between 0 and 100")
            
    @api.constrains('software')
    def _check_software_exists(self):
        for record in self:
            if record.software is None:
                raise ValidationError("Offer software must exist")