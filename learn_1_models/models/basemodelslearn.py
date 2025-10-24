from odoo import models, fields, api



class BaseModelLearn(models.Model):
    _name = 'base.model.learn'
    _description = 'Base Model Learn'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(default=lambda self: self._default_name())
    syam_charan = fields.Char(string="Field Label")

    def _default_name(self):
        return "syam"

