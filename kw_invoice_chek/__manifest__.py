{
    'name': 'Tovarniy Chek Invoice for Ukraine',
    'summary': 'Tovarniy Chek Товарний чек Бланк "Товарний чек Invoice" '
               'Друк/форми бухгалтерського документу/для України/'
               'Рахунок клієнту /Товарний чек/ Invoice',

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'category': 'Customizations',
    'license': 'LGPL-3',
    'version': '16.0.0.0.1',

    'depends': ['account', 'kw_invoice_doc_base', 'kw_discount_sum'],

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
