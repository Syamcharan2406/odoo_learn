{
    'name': 'Base Model Learn',
    'version': '1.0',
    'category': 'Syam',
    'summary': 'Simple model example for learning',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/base_model_learn_views.xml',
        'views/students_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
