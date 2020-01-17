# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class Software(models.Model):
    _name = 'offer_stats.software'

    name = fields.Char(string="Software", required=True, help="The name of the software")
    sw_type = fields.Selection(string="Software Type", required=True, 
                                help="The type of software. Possible values are: Program, Game or Extension", 
                                selection=[('program', 'Program'), 
                                            ('game', 'Game'), 
                                            ('extension', 'Extension')])
    offers = fields.One2many("offer_stats.offer", "software")

    #@api.depends('value')
    #def _value_pc(self):
    #    self.value2 = float(self.value) / 100