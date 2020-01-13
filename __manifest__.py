# -*- coding: utf-8 -*-
{
    'name': "offerStats",

    'summary': """
        This module will be used to offers stats about the most desired and 
        commented softwares of our app
    """,

    'description': """
        Module that calculates stats of out app based on the number of comments 
        each software has and the number of users that have wishlisted the same 
        software and creates a new stat called "most popular software"
    """,

    'author': "My Company",
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
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}