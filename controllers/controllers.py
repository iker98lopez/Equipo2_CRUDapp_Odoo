# -*- coding: utf-8 -*-
from odoo import http

# class OfferStats(http.Controller):
#     @http.route('/offer_stats/offer_stats/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/offer_stats/offer_stats/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('offer_stats.listing', {
#             'root': '/offer_stats/offer_stats',
#             'objects': http.request.env['offer_stats.offer_stats'].search([]),
#         })

#     @http.route('/offer_stats/offer_stats/objects/<model("offer_stats.offer_stats"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('offer_stats.object', {
#             'object': obj
#         })