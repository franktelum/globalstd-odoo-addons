# -*- coding: utf-8 -*-

from openerp import api, fields, models

class GsosAuditReportSection(models.Model):
    _name = 'gsos.audit.report.section'
    _description = 'Audit Report Summary Section'

    name = fields.Char(string='Name')
    audit_id = fields.Many2one(comodel_name='gsos.audit', string="Audit")
    supplier_id = fields.Many2one(comodel_name='res.partner', compute='_compute_supplier',
        string='Supplier', store=True)
    checklist_id = fields.Many2one(comodel_name='gsos.checklist', compute='_compute_checklist',
        string='Checklist', store=True)
    score = fields.Float(string='Score')

    @api.depends('audit_id')
    def _compute_checklist(self):
        for record in self:
            record.checklist_id = record.audit_id.checklist_id

    @api.depends('audit_id')
    def _compute_supplier(self):
        for record in self:
            record.supplier_id = record.audit_id.supplier_id


class GsosAudit(models.Model):
    _name = 'gsos.audit'
    _description = 'Audit'
    _inherit = ['mail.thread']

    name = fields.Char(string='Code', default='New', readonly=True)
    user_id = fields.Many2one(comodel_name='res.users', string='User')
    supplier_id = fields.Many2one(comodel_name='res.partner', string='Supplier')
    checklist_id = fields.Many2one(comodel_name='gsos.checklist', string='Checklist')
    date_start = fields.Date(string='Start Date')
    report_score = fields.Float(string='Score')
    report_file_url = fields.Char(string='Report File')
    report_sections = fields.One2many(comodel_name='gsos.audit.report.section',
        inverse_name='audit_id', string='Report Lines')

    state = fields.Selection(
        selection=[
          ('draft', 'Draft'),
          ('sent', 'Sent'),
          ('scheduled', 'Scheduled'),
          ('cancelled', 'Cancelled'),
          ('done', 'Done')
        ],
        string='State',
        default='draft')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('gsos.audit') or 'New'
        result = super(GsosAudit, self).create(vals)
        return result
