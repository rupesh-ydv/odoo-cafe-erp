from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ProductAccessoryLine(models.Model):
    _name = "product.accessory.line"
    _description = "Product Accessory"
    _order = "sequence, id"

    product_tmpl_id = fields.Many2one(
        "product.template", string="Main Product",
        required=True, ondelete="cascade", index=True,
    )
    accessory_product_id = fields.Many2one(
        "product.product", string="Accessory Product",
        required=True, ondelete="restrict", index=True,
        domain="[('sale_ok', '=', True), ('active', '=', True)]",
    )
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)
    required = fields.Boolean(
        string="Required",
        help="Select this accessory automatically on the website.",
    )
    max_qty = fields.Float(
        string="Maximum Quantity", default=1.0,
        help="Maximum quantity added with the main product. Use 0 for no limit.",
    )
    website_published = fields.Boolean(
        string="Show on Website", default=True,
    )
    note = fields.Char(string="Website Label")

    _sql_constraints = [
        (
            "unique_product_accessory",
            "unique(product_tmpl_id, accessory_product_id)",
            "The same accessory cannot be configured twice for the same product.",
        ),
    ]

    @api.constrains("product_tmpl_id", "accessory_product_id")
    def _check_not_self(self):
        for line in self:
            if (
                line.product_tmpl_id
                and line.accessory_product_id
                and line.product_tmpl_id == line.accessory_product_id.product_tmpl_id
            ):
                raise ValidationError(
                    _("A product cannot be configured as its own accessory.")
                )

    @api.constrains("max_qty")
    def _check_max_qty(self):
        for line in self:
            if line.max_qty < 0:
                raise ValidationError(_("Maximum quantity cannot be negative."))

    @api.onchange("accessory_product_id")
    def _onchange_accessory_product_id(self):
        for line in self:
            if line.accessory_product_id:
                line.note = line.accessory_product_id.display_name
