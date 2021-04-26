# -*- coding: utf-8 -*-
import binascii

from odoo import fields, http, _
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo.addons.payment.controllers.portal import PaymentProcessing
from odoo.addons.portal.controllers.mail import _message_post_helper
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager, get_records_pager
from odoo.osv import expression

class PartnerPortal(http.Controller):
    @http.route(['/invoice/index_form'], type='http', auth="public", website=True)
    def invoice_index(self, **post):
        return request.render("web_page.invoice_website_form", {})

    @http.route(['/invoice/website/search/submit'], type='http', auth="public", website=True)
    def invoice_search(self, **post):

        order_id = request.env['sale.order'].sudo().search([['name','=',post.get('sale_number')]])
        solicitud_form = request.env['solicitud.factura'].sudo().create({
            'name': post.get('sale_number'),
            'code': post.get('code'),
            'pedido_id': order_id.id,
            'customer_id': order_id.partner_id,
        })
        vals = {
            'solicitud_form': solicitud_form,
        }

        return request.render("web_page.search_invoice_website_form_success", vals)
