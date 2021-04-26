# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import AccessError

class SolicitudFactura(models.Model):
    _name = 'solicitud.factura'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char("Solicitud")
    code = fields.Char("Código")
    pedido_id = fields.Many2one('sale.order',string='Pedido')
    customer_id = fields.Many2one('res.partner',string='Cliente')
    factura = fields.One2many('account.move','solicitud_factura', string='Factura')


    @api.model
    def create(self, vals):
        result = super(SolicitudFactura, self).create(vals)
        order = self.sudo().env['sale.order'].search([('id', '=', result.pedido_id.id)])
        for line in order.order_line:
            move_lines = [
                        (0, 0, {
                            'account_id' : line.product_id.categ_id.property_stock_valuation_account_id.id,
                            'name': self.name +  ' - ' + line.product_id.name,
                            'credit': line.product_uom_qty * line.price_unit,
                        }),
                        (0, 0, {
                            'account_id' : line.product_id.property_stock_production.valuation_in_account_id.id,
                            'name': self.name +  ' - ' + line.product_id.name,
                            'debit': line.product_uom_qty * line.price_unit,
                        })
                    ]
            values = {
                'ref' : self.name +  ' - ' + line.product_id.name,
                'date' : line.date_order,
                'journal_id' : line.product_id.categ_id.property_stock_journal.id,
                'line_ids' : move_lines
                }
            asiento = self.env['account.move'].create(values)
                

        return result


