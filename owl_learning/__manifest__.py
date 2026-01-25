{
    'name': 'OWL.js Learning',
    'version': '1.0.0',
    'summary': 'Learn OWL.js Framework in Odoo',
    'description': """
OWL.js Learning Module for Odoo

This module provides structured learning materials, demos, and examples
to understand and master OWL.js framework used in modern Odoo frontend.

Features:
- OWL.js tutorials
- Example components
- Interactive demos
- Practice exercises
- Developer learning tools
    """,
    'category': 'Syam',
    'author': 'Syamcharan R',
    'website': 'https://www.odoo.com',
    'license': 'LGPL-3',
    'depends': [
            'base',
            'web',
            'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/owl_model_learn_views.xml',
        'views/menus.xml',
    ],
    'assets': {
        'web.assets_backend': [

        ],
    },
    'images': ['static/description/icon.png'],
    'application': True,
    'installable': True,
    'auto_install': False,
}
