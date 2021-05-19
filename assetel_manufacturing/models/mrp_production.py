# -*- coding: utf-8 -*-

from odoo import models, api, fields

class MrpProduction(models.Model):
    _inherit = 'mrp.production'
    
    def button_mark_done(self):
        result = super(MrpProduction, self).button_mark_done()
        if self.state == 'done':
            for line in self.workorder_ids:
                
                if line.product_id.categ_id.property_valuation == 'real_time':
                    move_lines = [
                                (0, 0, {
                                    'account_id' : line.workcenter_id.cuenta_abono.id,
                                    'name': self.name +  ' - ' + line.product_id.name,
                                    'credit': line.duration * (line.workcenter_id.costs_hour/60),
                                    
                                }),
                                (0, 0, {
                                    'account_id' : line.workcenter_id.cuenta_cargo.id,
                                    'name': self.name +  ' - ' + line.product_id.name,
                                    'debit': line.duration * (line.workcenter_id.costs_hour/60),
                                })
                            ]
                    values = {
                        'ref' : self.name +  ' - ' + line.product_id.name,
                        'date' : self.write_date,
                        'journal_id' : line.product_id.categ_id.property_stock_journal.id,
                        'line_ids' : move_lines
                        }
                    asiento = self.env['account.move'].create(values)
                    asiento.action_post()
            
        return result

