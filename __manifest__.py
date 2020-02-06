# -*- coding: utf-8 -*-
{
    'name': "offerStats",

    'summary': """
        This module will be used to offer stats about the most desired and
        commented softwares of our app.""",

    'description': """
        Module that calculates stats of our app based on the number of comments
        each software has and the number of users that have wishlisted the same
        software, and creates a new stat called "most popular softwares".
    """,

    'author': "Equipo 2",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/offer_stats.xml',
        'views/offer_form_view.xml',
        'views/offer_tree_view.xml',
        'views/software_form_view.xml',
        'views/software_tree_view.xml',
        'views/wish_form_view.xml',
        'views/wish_tree_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
