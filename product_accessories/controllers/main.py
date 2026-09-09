from odoo import http
from odoo.http import request


class ProductAccessoriesController(http.Controller):

    @http.route(
        "/shop/product/add_with_accessories",
        type="http",
        auth="public",
        website=True,
        methods=["POST"],
        csrf=True,
    )
    def add_with_accessories(self, product_id=None, accessory_ids=None, **post):
        try:
            product_id = int(product_id or 0)
        except (TypeError, ValueError):
            return request.redirect("/shop")

        main_product = request.env["product.product"].sudo().browse(product_id)
        if not main_product.exists() or not main_product.active or not main_product.sale_ok:
            return request.redirect("/shop")

        template = main_product.product_tmpl_id

        if accessory_ids is None:
            accessory_ids = []
        elif isinstance(accessory_ids, str):
            accessory_ids = [accessory_ids]

        try:
            accessory_ids = [int(value) for value in accessory_ids]
        except (TypeError, ValueError):
            accessory_ids = []

        configured_lines = template.accessory_line_ids.filtered(
            lambda line:
                line.active
                and line.website_published
                and line.accessory_product_id.active
                and line.accessory_product_id.sale_ok
        )
        configured_by_product = {
            line.accessory_product_id.id: line for line in configured_lines
        }

        selected_ids = set(accessory_ids)
        selected_ids.update(
            line.accessory_product_id.id
            for line in configured_lines
            if line.required
        )

        order = request.website.sale_get_order(force_create=True)
        if not order:
            return request.redirect("/shop")

        order._cart_update(product_id=main_product.id, add_qty=1)

        for accessory_id in selected_ids:
            line = configured_by_product.get(accessory_id)
            if not line:
                continue

            quantity = 1.0
            if line.max_qty > 0:
                quantity = min(quantity, line.max_qty)

            order._cart_update(
                product_id=line.accessory_product_id.id,
                add_qty=quantity,
            )

        return request.redirect("/shop/cart")
