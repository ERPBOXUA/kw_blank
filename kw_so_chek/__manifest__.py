{
    'name': 'Tovarniy Chek SO for Ukraine',
    'summary': 'Tovarniy Chek Товарний чек Бланк "Товарний чек Sale Order" '
               'Друк/форми бухгалтерського документу/для України/ '
               'Замовлення на продаж /Товарний чек/Sale order ',

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
