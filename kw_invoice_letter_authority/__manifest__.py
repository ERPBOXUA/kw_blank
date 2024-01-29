{
    'name': 'Letter Authority Invoice for Ukraine',
    'summary': 'Letter Authority Довіреність',

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'category': 'Accounting',
    'license': 'LGPL-3',
    'version': '14.0.1.0.2',

    'depends': [
        'account',
        'kw_invoice_doc_base',
        'kw_account_partner_requisites',
        'kw_employee_requizites',
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
