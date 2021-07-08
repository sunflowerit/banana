from odoo import fields, models


class BananaDinnerEvent(models.Model):
    _name = 'banana.dinner.event'
    _description = 'Dinner event'

    name = fields.Char()
    date = fields.Date('Date')
    banana_id = fields.Many2one('banana', 'Banana')
    user_id = fields.Many2one('res.users', 'Monkey')
    tribe_id = fields.Many2one('monkey.tribe', 'Tribe')
