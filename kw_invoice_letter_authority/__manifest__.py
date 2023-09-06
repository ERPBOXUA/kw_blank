{
    'name': 'Letter Authority Invoice for Ukraine',
    'summary': 'Letter Authority Довіреність Бланк "Довіреність" Друк/Довіреність/ для України',

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'category': 'Accounting',
    'license': 'LGPL-3',
    'version': '16.0.0.0.1',

    'depends': [
        'account',
        'kw_invoice_doc_base',
        'kw_account_partner_requisites',
    ],

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
