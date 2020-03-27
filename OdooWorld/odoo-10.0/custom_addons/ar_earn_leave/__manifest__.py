{
    'name': "Earn Leave Request Management",
    'version': '10.0.0.0',
    'author': "A R SHAKIL",
    'category': 'Extra Tools',
    'summary':'Module for managing the Earn Leave Request',
    'maintainer':'Metamorphosis',
    'website':'metamorphosis.com',
    'sequence':'-1',
    'license': 'AGPL-3',
    'depends': ['mail','sale','base'],
    'data': [
        'security/ir.model.access.csv',
        'views/earn_leave.xml',
        'views/employee_inherited_view.xml',

    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
