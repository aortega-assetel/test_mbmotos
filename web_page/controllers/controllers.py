# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class PartnerPortal(http.Controller):
    @http.route(['/invoice/index_form'], type='http', auth="public", website=True)
    def wisp_sign_in_form(self, **post):
        return request.render("web_page.invoice_website_form", {})

    @http.route(['/invoice/website/search/submit'], type='http', auth="public", website=True)
    def wisp_sign_in_form_submit(self, **post):
        wisp_form = request.env['wisp.sign.in'].sudo().create({
            'partner_name': post.get('partner_name'),
            'email': post.get('email'),
            'phone': post.get('phone')
        })
        vals = {
            'wisp_form': wisp_form,
        }
        return request.render("wisp_sign_in.wisp_sign_in_website_form_success", vals)
        