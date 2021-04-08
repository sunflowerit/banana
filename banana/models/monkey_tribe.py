from odoo import fields, models


class MonkeyTribe(models.Model):
    _name = "monkey.tribe"
    _description = "Monkey tribe"

    name = fields.Char()
    description = fields.Text()
    member_ids = fields.Many2many("res.users")
