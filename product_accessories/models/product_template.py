from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    accessory_line_ids = fields.One2many(
        "product.accessory.line",
        "product_tmpl_id",
        string="Accessories",
        copy=True,
    )
    accessory_count = fields.Integer(
        string="Accessories",
        compute="_compute_accessory_count",
    )

    def _compute_accessory_count(self):
        for product in self:
            product.accessory_count = len(
                product.accessory_line_ids.filtered("active")
            )
