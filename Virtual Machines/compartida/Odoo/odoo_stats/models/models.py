# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class odoo_stats(models.Model):
#     _name = 'odoo_stats.odoo_stats'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
class Wish(models.Model):
    _name = 'offer_stats.wish'
    wish_id= fields.Integer(string="Wish_ID")
    software_id = fields.Many2one('offer_stats.software', string="Software_ID", required=True)
    min_price = fields.Float(digits=(5, 2), help='Minimum price to be notified')