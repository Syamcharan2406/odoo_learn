from odoo import models, fields, api

class CommonMixin(models.AbstractModel):
    _name = 'common.mixin'
    _description = 'Common reusable logic for models'

    # Example fields that inheriting models will get
    active = fields.Boolean(default=True)
    notes = fields.Text(string='Notes')

    # Example method that can be used by other models
    def toggle_active(self):
        for record in self:
            record.active = not record.active

    # Example computed field method
    @api.depends('notes')
    def _compute_note_length(self):
        for record in self:
            record.note_length = len(record.notes) if record.notes else 0



class Student(models.Model):
    _name = 'school.student'
    _description = 'Student Information'
    _inherit = ['common.mixin','mail.thread', 'mail.activity.mixin']  # Inherit abstract model

    name = fields.Char(required=True)
    age = fields.Integer()