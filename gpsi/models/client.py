# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Client(models.Model):
    _inherit = ['res.partner']

    contract_ids = fields.One2many(comodel_name='gpsi.contract',
        inverse_name='client_id',
        string='Contracts',
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        auto_join=False)

    quotation_ids = fields.One2many(comodel_name='gpsi.quotation',
        inverse_name='client_id',
        string=None,
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        auto_join=False)
