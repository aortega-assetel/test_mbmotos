# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import AccessError

class AccountMove(models.Model):
    _name = 'account.move'
    solicitud_factura = fields.Many2one('solicitud.factura', string='Solicitud Factura')


