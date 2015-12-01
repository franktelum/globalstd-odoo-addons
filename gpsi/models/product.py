# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Product(models.Model):
    _name = 'gpsi.product'
    _description = 'Product'
    _inherit = ['mail.thread']

    name = fields.Char(string='Name',
        help=None,
        readonly=False,
        required=True,
        groups=[])

    price = fields.Float(string='Price',
        digits=(6,2),
        help=None,
        readonly=False,
        required=False,
        groups=[])

    description = fields.Text(string='Description',
        help=None,
        readonly=False,
        required=False,
        groups=[],
        translate=False)
