from odoo import fields, models , api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    product_type = fields.Selection([
        ('aircraft', 'Aircraft'),
        ('engine', 'Engine'),
    ], string='Machine Type')

