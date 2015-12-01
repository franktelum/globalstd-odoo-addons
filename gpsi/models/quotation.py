# -*- coding: utf-8 -*-

from openerp import models, fields, api

class QuotationOrderLine(models.Model):
    _name = 'gpsi.quotation.order.line'
    _description = 'Quotation'
    _inherit = ['gpsi.order.line']

    quotation_id = fields.Many2one(comodel_name='gpsi.quotation',
        string='Quotation',
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        ondelete=None)

class Quotation(models.Model):
    _name = 'gpsi.quotation'
    _description = 'gpsi.quotation'
    _inherit = ['mail.thread']

    name = fields.Char(string='Code',
        default='New',
        help=None,
        readonly=True,
        required=True,
        index=True,
        groups=[])

    client_id = fields.Many2one(comodel_name='res.partner',
        string='Contact',
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        ondelete=None)

    state = fields.Selection(
        selection=[
          ('draft', 'Draft'),
          ('negotiation', 'Negotiation'),
          ('cancelled', 'Cancelled'),
          ('closed', 'Closed')
        ],
        string='State',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    quotation_type = fields.Selection(
        selection=[
          ('fssc_22000', 'FSSC 22000'),
          ('9001', '9001')
        ],
        string='Type',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    standard = fields.Many2one(comodel_name='gpsi.audit.standard',
        string='Standard',
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        ondelete=None)

    range_employees = fields.Selection(
        selection=[
          (1, '1 to 9'),
          (2, '10 to 19'),
          (3, '20 to 49'),
          (4, '50 to 99')
        ],
        string='Employees Range',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    category = fields.Selection(
        selection=[
          ('m', 'M')
        ],
        string='Category',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    num_haccp = fields.Integer(string='No. HACCP',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    is_multisite = fields.Boolean(string='Multisite?',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    certification_type = fields.Selection(
        selection=[
          ('initial', 'Initial'),
          ('recertification', 'Recertification'),
          ('takeover', 'Takeover'),
          ('transfer', 'Transfer'),
          ('special', 'Special')
        ],
        string='Certification Type',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    order_line_ids = fields.One2many(comodel_name='gpsi.quotation.order.line',
        inverse_name='quotation_id',
        string=None,
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        auto_join=False)

    scope = fields.Char(string='Scope',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    comments = fields.Text(string='Additional Comments',
        help=None,
        readonly=False,
        required=False,
        groups=[],
        translate=False)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('gpsi.quotation') or 'New'

        result = super(Quotation, self).create(vals)
        return result
