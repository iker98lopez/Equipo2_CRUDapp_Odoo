# -*- coding: utf-8 -*-

from odoo import models, fields

class User(models.Model):
    _name = 'offer_stats.user'
    _inherit = 'res.users'
    
    wishlist = fields.One2many('offer_stats.wish','wish_id', ondelete = 'set null', string = "WishList");