{
    'name': 'Vydatkova Nakladna Invoice for Ukraine',
    'summary': 'Vydatkova Nakladna Видаткова накладна',

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'category': 'Accounting',
    'license': 'LGPL-3',
    'version': '14.0.1.0.4',

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
