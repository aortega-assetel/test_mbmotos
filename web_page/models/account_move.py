# -*- coding: utf-8 -*-
import logging

from odoo import models, api, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    solicitud_factura = fields.Many2one('solicitud.factura', string='Solicitud Factura')


