# -*- coding: utf-8 -*-
# from odoo import http


# class CustomSingleProductPage(http.Controller):
#     @http.route('/custom_single_product_page/custom_single_product_page', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_single_product_page/custom_single_product_page/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_single_product_page.listing', {
#             'root': '/custom_single_product_page/custom_single_product_page',
#             'objects': http.request.env['custom_single_product_page.custom_single_product_page'].search([]),
#         })

#     @http.route('/custom_single_product_page/custom_single_product_page/objects/<model("custom_single_product_page.custom_single_product_page"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_single_product_page.object', {
#             'object': obj
#         })

from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)

class WebsiteSaleCustomFilter(WebsiteSale):
    @http.route(['/shop'], type='http', auth="public", website=True)
    def shop(self, page=0, category=None, search='', **post):

        city_filter = post.get('city_filter', '')
        direction_filter = post.get('direction_filter', '')
        
        # Tạo domain để lọc sản phẩm dựa trên thành phố
        domain = [('sale_ok', '=', True)]
        if city_filter:
            domain.append(('state_id', '=', int(city_filter)))

        # domain_1 = [('sale_ok_1', '=', True)]
        # if direction_filter:
        #     domain_1.append(('direction_id', '=', int(direction_filter)))
        
        response = super(WebsiteSaleCustomFilter, self).shop(page=page, category=category, search="", **post)
        products = request.env['product.template'].search(domain)

        city_values = request.env['res.country.state'].search([])

        # direction = request.env['product.direction'].search(domain_1)
        response.qcontext.update({
                'city_values': city_values,
                'products': products,
                # 'direction': direction,
            })


        _logger.info(f" response.qcontext + { response.qcontext}")
        return response