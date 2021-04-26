# -*- coding: utf-8 -*-
from odoo import models, api, fields
import random

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    code = fields.Char("Código")


    @api.model
    def create(self, vals):
        result = super(SaleOrder, self).create(vals)
        self.ensure_one()
                

        return result

