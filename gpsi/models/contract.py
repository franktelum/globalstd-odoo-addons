# -*- coding: utf-8 -*-

import logging
from openerp import models, fields, api

_logger = logging.getLogger(__name__)

class ContractOrderLine(models.Model):
    _name = 'gpsi.contract.order.line'
    _description = 'Contract Order Line'
    _inherit = ['gpsi.order.line']

    contract_id = fields.Many2one(comodel_name='gpsi.contract',
        string='Contract',
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        ondelete=None)

class Contract(models.Model):
    _name = 'gpsi.contract'
    _description = 'Contract'
    _inherit = 'mail.thread'

    name = fields.Char(string='Code',
        default='New',
        help=None,
        readonly=True,
        required=True,
        index=True,
        groups=[])

    client_id = fields.Many2one(comodel_name='res.partner', string='Client',
        help=None,
        readonly=False,
        required=True,
        domain=[('customer', '=', True)],
        context=None,
        ondelete=None)

    audit_event_ids = fields.One2many(comodel_name='gpsi.audit.event',
        inverse_name='contract_id',
        string='Audit Events',
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        auto_join=False)

    audit_event_count = fields.Integer(compute='_compute_audit_event_count',
        string='Number audit events attached',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    state = fields.Selection(
        selection=[
          ('draft', 'Draft'),
          ('negotiation', 'Negotiation'),
          ('review', 'Review'),
          ('cancelled', 'Cancelled'),
          ('closed', 'Closed')
        ],
        default='draft',
        string='State',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    cycle = fields.Integer(string='Cycle',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    standard = fields.Many2one(comodel_name='gpsi.audit.standard',
        string='Standard',
        help=None,
        readonly=False,
        required=True,
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
        default=1,
        string='Employees Range',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    apply_design = fields.Boolean(string='Apply Design',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    is_multisite = fields.Boolean(string='Multisite',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    need_bilingual_auditor = fields.Boolean(string='Bilingual Auditor',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    block_contract = fields.Boolean(string='Block Contract',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    risk_level = fields.Integer(string='Risk Level',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    special_notes = fields.Text(string='Special Notes',
        help=None,
        readonly=False,
        required=False,
        groups=[],
        translate=False)

    date_sign = fields.Date(string='Date',
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
        default='initial',
        string='Certification Type',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    scheme = fields.Selection(
        selection=[
          ('mixed', 'Mixed'),
          ('annual', 'Annual'),
          ('semestral', 'Semestral')
        ],
        default='annual',
        string='Scheme',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    duration = fields.Selection(
        selection=[
          (1, '1 year'),
          (2, '2 year'),
          (3, '3 year')
        ],
        default=1,
        string='Duration',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    report_time = fields.Integer(string='Report Time',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    expenses_invoice = fields.Selection(
        selection=[
          ('apply', 'Apply'),
          ('not_applicable', 'Not Applicable'),
          ('special', 'Special')
        ],
        string='Expenses Invoice',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    order_line_ids = fields.One2many(comodel_name='gpsi.contract.order.line',
        inverse_name='contract_id',
        string='Order Line',
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        auto_join=False)

    scope = fields.Text(string='Scope',
        help=None,
        readonly=False,
        required=False,
        groups=[],
        translate=False)

    date_certificate_issue = fields.Date(string="Certificate Issue's Date",
        help=None,
        readonly=False,
        required=False,
        groups=[])

    date_certificate_expiration = fields.Date(string='Expiration Date',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    certificate_status = fields.Selection(
        selection=[
          ('active', 'Active'),
          ('expired', 'Expired'),
          ('suspended', 'Suspended'),
          ('canceled', 'Canceled')
        ],
        string='Certificate Status',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('gpsi.contract') or 'New'

        result = super(Contract, self).create(vals)
        return result

    @api.multi
    @api.depends('audit_event_ids')
    def _compute_audit_event_count(self):
        for contract in self:
            contract.audit_event_count = len(self.audit_event_ids);
