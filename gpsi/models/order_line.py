# -*- coding: utf-8 -*-

from openerp import models, fields, api

class OrderLine(models.TransientModel):
    _name = 'gpsi.order.line'
    _description = 'gpsi.order.line'

    product_id = fields.Many2one(comodel_name='gpsi.product',
        string='Product',
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        ondelete=None)

    qty = fields.Float(string='Quantity',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    unit_price = fields.Float(string='Price',
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
