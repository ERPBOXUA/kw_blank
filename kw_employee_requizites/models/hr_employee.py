import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HrEmployeePrivate(models.Model):
    _inherit = 'hr.employee'

    type_document = fields.Char()

    serial_document = fields.Char()

    number_document = fields.Char()

    issued_date = fields.Date(
        string='issuance date', )
    issued = fields.Char()
