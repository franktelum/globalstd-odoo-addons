# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ApplicationForm(models.Model):
    _name = 'gpsi.application.form'
    _description = 'Application Form'
    _inherit = 'mail.thread'

    name = fields.Char(string='Code',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    client_id = fields.Many2one(comodel_name='res.partner',
        string='Client',
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        ondelete=None)

    status = fields.Selection(
        selection=[
          ('draft', 'Draft'),
          ('sent', 'Sent'),
          ('cancelled', 'Cancelled'),
          ('closed', 'Closed')
        ],
        string='Status',
        help=None,
        readonly=False,
        required=False,
        groups=[])
