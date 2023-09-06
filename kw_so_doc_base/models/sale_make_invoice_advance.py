from odoo import models


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def _create_invoice(self, order, so_line, amount):
        invoice = super(SaleAdvancePaymentInv, self)._create_invoice(
            order, so_line, amount)
        if invoice:
            invoice.kw_contract = order.kw_contract
            invoice.kw_responsible_person = order.kw_responsible_person
        return invoice
