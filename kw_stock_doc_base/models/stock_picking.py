import logging
from odoo import models

_logger = logging.getLogger(__name__)


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def get_formatted_date(self, date):
        lang = self.env.lang or 'en_US'
        formatted_date = date.strftime('%d %B %Y')
        if lang != 'en_US':
            formatted_date = self._translate_date(formatted_date, lang)
        return formatted_date

    def _translate_date(self, formatted_date, lang):
        lang_code = lang.split('_')[0]
        translations = {
            'uk': {
                'January': 'січня',
                'February': 'лютого',
                'March': 'березня',
                'April': 'квітня',
                'May': 'травня',
                'June': 'червня',
                'July': 'липня',
                'August': 'серпня',
                'September': 'вересня',
                'October': 'жовтня',
                'November': 'листопада',
                'December': 'грудня',
            },
        }
        for month_en, month_translated in translations.get(lang_code,
                                                           {}).items():
            formatted_date = formatted_date.replace(month_en, month_translated)
        return formatted_date
