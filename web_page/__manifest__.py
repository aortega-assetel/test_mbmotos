# -*- coding: utf-8 -*-
{
    'name': "Pagina Web",

    'summary': """
        Modulo de pagina web""",

    'description': """
        Modulo de pagina web
    """,

    'author': "Assetel",
    'website': "http://www.assetel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management'],

    # always loaded
    'data': [
        'views/sale_order_report.xml',
    ],
    
}