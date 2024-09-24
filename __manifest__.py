# -*- coding: utf-8 -*-
{
    'name': "custom_single_product_page",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',"product","RealEstateModule2"],# thêm product vào khi kế thừa 

    'application': True,

    # always loaded
    #css
        'assets': {
        'web.assets_frontend': [
            'custom_single_product_page/static/src/css/css.css', #đường dẫn file css
        ],
    },

    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/view_chitietsp.xml',
        'views/view_sp_ws.xml',
        'views/filter_ws.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

