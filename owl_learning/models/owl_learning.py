from odoo import models, fields, api

class BaseModelLearn(models.Model):
    _name = 'owl.model.learn'
    _description = 'Owl Model Learn'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(default=lambda self: self._default_name())
    notes = fields.Html(string="Notes")

    def _default_name(self):
        return "Owl Learn"
