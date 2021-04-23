# -*- coding: utf-8 -*-
from odoo import models, api, fields
import random

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    code = fields.Integer("Código")


    @api.model
    def create(self, vals):
        result = super(SaleOrder, self).create(vals)
        while True:
            ran_number = random.randint(1000000000,9999999999)
            repetido = self.env['sale.order'].search_count([['code','=',ran_number]])
            if repetido == 0:
                result['code'] = ran_number
                break
                

        return result

