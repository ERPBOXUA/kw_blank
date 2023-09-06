{
    'name': 'Akt Vikonanih Robit SO for Ukraine',
    'summary': 'Akt Vikonanih Robit Акт виконаних робіт Бланк "Акт виконаних робіт Sale Order" '
               'Друк форми бухгалтерського документу для України'
               'Замовлення на продаж Sale order',

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'category': 'Accounting',
    'license': 'LGPL-3',
    'version': '16.0.0.0.1',

    'depends': ['sale', 'kw_so_doc_base', 'kw_discount_sum'],

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
