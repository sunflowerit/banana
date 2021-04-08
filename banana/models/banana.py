from odoo import fields, models


class Banana(models.Model):
    _name = 'banana'
    _description = 'Banana'
    _inherit = ['mail.thread']

    tribe_id = fields.Many2one('monkey.tribe', 'Tribe')
    description = fields.Text()
    name = fields.Char()
