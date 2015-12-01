# -*- coding: utf-8 -*-

from openerp import models, fields, api

class AuditEvent(models.Model):
    _name = 'gpsi.audit.event'
    _description = 'Audit Event'
    _inherit = 'mail.thread'

    name = fields.Char(string='Code',
        default='New',
        help=None,
        readonly=True,
        required=True,
        index=True,
        groups=[])

    contract_id = fields.Many2one(comodel_name='gpsi.contract',
        string='Contract',
        help=None,
        readonly=False,
        required=True,
        domain=None,
        context=None,
        ondelete=None)

    state = fields.Selection(
        selection=[
          ('scheduled', 'Scheduled'),
          ('confirmed', 'Confirmed'),
          ('execution', 'Execution'),
          ('review', 'Review'),
          ('cancelled', 'Cancelled'),
          ('closed', 'Closed')
        ],
        default='scheduled',
        string='State',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    event_type = fields.Selection(
        selection=[
          ('pre_audit', 'Pre-Audit'),
          ('stage1', 'Stage I'),
          ('stage2', 'Stage II'),
          ('takeover', 'Takeover'),
          ('recertification', 'Recertification'),
          ('surveillance1', 'Surveillance Annual 1'),
          ('surveillance2', 'Surveillance Annual 2'),
          ('surveillance3', 'Surveillance Annual 3'),
          ('surveillance4', 'Surveillance Annual 4'),
          ('surveillance5', 'Surveillance Annual 5'),
          ('special', 'Special'),
          ('cars', 'CARS')
        ],
        string='Event Type',
        help=None,
        readonly=False,
        required=True,
        groups=[])

    shift = fields.Selection(
        selection=[
          ('all_day', 'All Day'),
          ('day', 'Day'),
          ('afternoon', 'Afternoon')
        ],
        string='Shift',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    date_start = fields.Date(string='Start Date',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    date_end = fields.Date(string='End Date',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    validate_date_limit = fields.Boolean(string='Validate Date Limit',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    comments = fields.Text(string='Comments',
        help=None,
        readonly=False,
        required=False,
        groups=[],
        translate=False)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('gpsi.audit.event') or 'New'

        result = super(AuditEvent, self).create(vals)
        return result
