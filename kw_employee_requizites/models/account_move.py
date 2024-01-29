import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = 'account.move'

    hr_employee_id = fields.Many2one(
        comodel_name='hr.employee', )
    number_document = fields.Char()

    date_issue = fields.Date(
        string='Date of issue', )

    valid_until = fields.Date()

    head_enterprise_id = fields.Many2one(
        comodel_name='hr.employee', )
    chief_accountant_id = fields.Many2one(
        comodel_name='hr.employee', )
