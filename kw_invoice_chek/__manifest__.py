{
    'name': 'Tovarniy Chek Invoice for Ukraine',
    'summary': 'Tovarniy Chek Товарний чек',

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'category': 'Customizations',
    'license': 'LGPL-3',
    'version': '14.0.1.0.3',

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
