{
    'name': 'Vydatkova Nakladna SO for Ukraine',
    'summary': 'Vydatkova Nakladna Видаткова накладна \
                Бланк "Видаткова накладна Sale Order" '
               'Друк форми бухгалтерського документу для України'
               'Видаткова накладна Замовлення на продаж Sale order',

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'category': 'Accounting',
    'license': 'LGPL-3',
    'version': '17.0.0.1.1',

    'depends': ['sale', 'kw_so_doc_base'],

    'data': [
        'report/report.xml',
        'report/templates.xml',
    ],

    'installable': True,

    'images': [
        'static/description/cover.png',
        'static/description/icon.png',
    ],

}
