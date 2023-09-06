import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

try:
    from num2words import num2words
except ImportError as err:
    _logger.debug(err)


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    kw_auto_carrier = fields.Char('Carrier')
    kw_driver = fields.Char('Driver')
    kw_consignor = fields.Char('Consignor')
    kw_get_baggage = fields.Char('Get baggage')
    kw_loading_point = fields.Char('Loading Point')

    kw_qty_seats = fields.Char('Qty Seats', compute='_compute_value_verbs')
    kw_total_qty_seats = fields.Float(compute='_compute_summ_line')

    kw_gross_weight = fields.Char(compute='_compute_value_verbs')
    kw_total_gross_weight = fields.Float(compute='_compute_summ_line')

    kw_got_driver = fields.Char()

    kw_total_summ_line = fields.Float(compute='_compute_summ_line')
    kw_total_verbs = fields.Char(compute='_compute_value_verbs')

    kw_pdv = fields.Char()
    kw_documents_for_baggage = fields.Char()
    kw_zdav = fields.Char()
    kw_priyniav = fields.Char()

    def _compute_value_verbs(self):
        for obj in self:
            self.kw_total_verbs = '{} {} {:0>2} {}'.format(
                num2words(int(obj.kw_total_summ_line), lang='uk'),
                'грн.',
                round(100 *
                      (obj.kw_total_summ_line -
                       int(obj.kw_total_summ_line))),
                'коп.', ).capitalize()
            self.kw_qty_seats = '{} {} {:0>2} {}'.format(
                num2words(int(obj.kw_total_qty_seats),
                          lang='uk'),
                ',',
                round(100 *
                      (obj.kw_total_qty_seats -
                       int(obj.kw_total_qty_seats))),
                '',
            ).capitalize()
            self.kw_gross_weight = '{} {} {:0>2} {}'.format(
                num2words(int(obj.kw_total_gross_weight),
                          lang='uk'),
                ',',
                round(100 *
                      (obj.kw_total_gross_weight -
                       int(obj.kw_total_gross_weight))),
                '',
            ).capitalize()

    @api.depends('move_ids_without_package.kw_summ',
                 'move_ids_without_package.kw_qty_seats_line',
                 'move_ids_without_package.kw_gross_weight_line')
    def _compute_summ_line(self):
        total_summ = 0
        qty_seats = 0
        total_gross_weight = 0
        for line in self.move_ids_without_package:
            total_summ += line.kw_summ
            qty_seats += line.kw_qty_seats_line
            total_gross_weight += line.kw_gross_weight_line
        self.kw_total_summ_line = total_summ
        self.kw_total_qty_seats = qty_seats
        self.kw_total_gross_weight = total_gross_weight


class StockMove(models.Model):
    _inherit = 'stock.move'

    def _get_default_product_uom_id(self):
        return self.env['uom.uom'].search([], limit=1, order='id').id

    kw_unit_line = fields.Many2one(
        'uom.uom', 'Product Unit of Measure',
        default=_get_default_product_uom_id)
    kw_qty_seats_line = fields.Float(string='Quantity seats')
    kw_price_line = fields.Float(string='Price')
    kw_summ = fields.Float(string='Total')
    kw_type_package_line = fields.Char(string='Type package')
    kw_documents_line = fields.Char(string='Documents')
    kw_gross_weight_line = fields.Float('Gross weight')
    kw_summ_line = fields.Float()
