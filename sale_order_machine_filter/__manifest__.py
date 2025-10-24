{
    'name': "Sale Order Machine Filter",
    'summary': "Adds AC/ENG filter buttons to Sales Orders list view",
    'version': '1.0',
    'author': "Syam",
    'depends': ['web', 'sale_management'],
    'data': [
        'views/sale_order_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'sale_order_machine_filter/static/src/js/machine_filter_list_controller.js',
            'sale_order_machine_filter/static/src/xml/machine_filter_list_buttons.xml',
        ],
    },
    'installable': True,
    'application': False,
}
