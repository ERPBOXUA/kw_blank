{
    'name': 'Tovarno Transportna Nakladna for Ukraine',
    'summary': 'Tovarno Transportna Nakladna Товарно-транспортна накладна Бланк "Товарно транспортна накладна" '
               'друк/ документ/ Товарно транспортна накладна/ТТН/Товаро-транспортна',

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'category': 'Accounting',
    'license': 'LGPL-3',
    'version': '16.0.1.0.5',

    'depends': ['sale', 'stock', 'kw_stock_doc_base'],

    'data': [
        'report/report.xml',
        'report/templates.xml',
        'views/stock_picking_views.xml',
    ],

    'installable': True,

    'images': [
        'static/description/cover.png',
        'static/description/icon.png',
    ],

}
