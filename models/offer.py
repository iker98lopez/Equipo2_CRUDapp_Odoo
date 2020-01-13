# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class Offer(models.Model):
    _name = 'offer_stats.offer'

    shop = fields.Char(string="Shop", required=True, help="The shop making the offer")
    basePrice = fields.Float(string="Base price", digits="6,2")
    discountedPrice = fields.Float(string="Discounted price", digits="6,2")
    discount = fields.Float(string="Discount %", digits="2,0")
    software = fields.ManyToOne("offer_stats.software", onDelete="cascade", String="Software")
    
    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100