{
    "name": "Product Accessories",
    "version": "19.0.1.0.0",
    "category": "Website/eCommerce",
    "summary": "Configure and sell product accessories on Odoo eCommerce",
    "description": "Configure accessory products per product template and add selected accessories with the main product to the eCommerce cart.",
    "author": "Custom Odoo Module",
    "license": "LGPL-3",
    "depends": ["website_sale"],
    "data": [
        "security/ir.model.access.csv",
        "views/product_accessory_views.xml",
        "views/product_template_views.xml",
        "views/website_sale_templates.xml"
    ],
    "assets": {
        "web.assets_frontend": [
            "product_accessories/static/src/js/product_accessories.js",
            "product_accessories/static/src/scss/product_accessories.scss"
        ]
    },
    "installable": True,
    "application": True
}