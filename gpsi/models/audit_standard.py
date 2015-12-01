# -*- coding: utf-8 -*-

from openerp import models, fields, api

class AuditStandard(models.Model):
    _name = 'gpsi.audit.standard'
    _description = 'gpsi.audit.standard'

    name = fields.Char(string='Name',
        help=None,
        readonly=False,
        required=True,
        groups=[])

    abbreviation = fields.Char(string='Abbreviation',
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

    iaf_ids = fields.One2many(comodel_name='gpsi.audit.iaf',
        inverse_name='standard_id',
        string=None,
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        auto_join=False)


class AuditIaf(models.Model):
    _name = 'gpsi.audit.iaf'
    _description = 'gpsi.audit.iaf'

    name = fields.Char(string='Name',
        help=None,
        readonly=False,
        required=True,
        groups=[])

    description = fields.Text(string='Description',
        help=None,
        readonly=False,
        required=False,
        groups=[],
        translate=False)

    standard_id = fields.Many2one(comodel_name='gpsi.audit.standard',
        string='Standard',
        help=None,
        readonly=False,
        required=True,
        domain=None,
        context=None,
        ondelete=None)

    nace_code_ids = fields.One2many(comodel_name='gpsi.audit.nacecode',
        inverse_name='iaf_id',
        string='NACE Codes',
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        auto_join=False)

class AuditNaceCode(models.Model):
    _name = 'gpsi.audit.nacecode'
    _description = 'gpsi.audit.nacecode'

    name = fields.Char(string='Name',
        help=None,
        readonly=False,
        required=True,
        groups=[])

    accredited_by_anab = fields.Boolean(string='Accredited by ANAB',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    risk_class = fields.Integer(string='Risk Class',
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

    iaf_id = fields.Many2one(comodel_name='gpsi.audit.iaf',
        string='IAF',
        help=None,
        readonly=False,
        required=True,
        domain=None,
        context=None,
        ondelete=None)
