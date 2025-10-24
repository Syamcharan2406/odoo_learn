from odoo import fields, models , api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    machine_type = fields.Selection([
        ('aircraft', 'Aircraft'),
        ('engine', 'Engine'),
    ], string='Machine Type')

    def action_filter_machine_ac(self):
        """Return an action to filter sale orders where machine_type = 'AC'"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'AirCraft Machine Orders',
            'res_model': 'sale.order',
            'view_mode': 'list',
            'domain': [('machine_type', '=', 'aircraft')],
            'context': dict(self.env.context),
        }

    def action_filter_machine_eng(self):
        """Return an action to filter sale orders where machine_type = 'AC'"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Engine Machine Orders',
            'res_model': 'sale.order',
            'view_mode': 'list',
            'domain': [('machine_type', '=', 'engine')],
            'context': dict(self.env.context),
        }
