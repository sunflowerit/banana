from odoo import fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    tribe_ids = fields.Many2many(
        "monkey.tribe",
        "tribe_users_rel",
        "user_id",
        "tribe_id",
        "Tribe memberships",
    )
