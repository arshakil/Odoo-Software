{
    'name': "Purchase Request Management",
    'version': '13.0.0.0',
    'author': "A R SHAKIL",
    'category': 'Extra Tools',
    'summary':'Module for managing the Purchase Request',
    'maintainer':'Odoo Mates',
    'website':'metamorphosis.com',
    'sequence':'20', 
    'license': 'AGPL-3',
    'depends': ['mail','product',],
    'data': [
        'security/ir.model.access.csv',
        'views/ar_purchase_request.xml',

    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
