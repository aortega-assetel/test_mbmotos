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





