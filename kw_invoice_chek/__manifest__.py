{
    'name': 'Tovarniy Chek Invoice for Ukraine',
    'summary': 'Tovarniy Chek Товарний чек Бланк "Товарний чек Invoice" '
               'Друк/форми бухгалтерського документу/для України/'
               'Рахунок клієнту /Товарний чек/ Invoice',

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'category': 'Customizations',
    'license': 'LGPL-3',
    'version': '17.0.0.1.1',

    'depends': ['account', 'kw_invoice_doc_base'],

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
