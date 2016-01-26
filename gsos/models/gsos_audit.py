# -*- coding: utf-8 -*-

from openerp import api, fields, models

class GsosAudit(models.Model):
    _name = 'gsos.audit'
    _description = 'Audit'
    _inherit = ['mail.thread']

    name = fields.Char(string='Code', default='New', readonly=True)
    supplier_id = fields.Many2one(comodel_name='gsos.supplier.profile', string='Supplier')
    checklist_id = fields.Many2one(comodel_name='gsos.checklist', string='Checklist')
    date_start = fields.Date(string='Assessment Date')
    auditor_id = fields.Many2one(comodel_name='res.users', string='Conduced By')
    date_cap_due = fields.Date(string='CAP Due Date')
    material_scope = fields.Many2one(comodel_name='gsos.supplier.profile.product', string='Material Type/Scope')
    report_score = fields.Float(string='Total Score')
    report_file_url = fields.Char(string='File')
    report_section_ids = fields.One2many(comodel_name='gsos.audit.report.section',
        inverse_name='audit_id', string='Sections')
    report_comment_ids = fields.One2many(comodel_name='gsos.audit.report.comment',
        inverse_name='audit_id', string='Auditor Comments')
    noconformance_count = fields.Integer(compute='_get_noconformance_count', string='Number noconformances attached')

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

    document_count = fields.Integer(compute='_get_document_count', string='Number documents attached')

    # Compute and search fields
    def _get_noconformance_count(self):
        self.ensure_one()
        noconformances = self.env['gsos.audit.report.noconformance'].search([['audit_id', '=', self.id]])
        self.noconformance_count = len(noconformances)

    def _get_document_count(self):
        self.ensure_one()

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('gsos.audit') or 'New'
        result = super(GsosAudit, self).create(vals)
        return result

class GsosAuditReportSection(models.Model):
    _name = 'gsos.audit.report.section'
    _description = 'Audit Report Section'
    _inherit = ['mail.thread']

    audit_id = fields.Many2one(comodel_name='gsos.audit', string='Audit')
    name = fields.Char(string='Name')
    score = fields.Float(string='Score')
    question_ids = fields.One2many(comodel_name='gsos.audit.report.question',
        inverse_name='section_id', string='Questions')
    supplier_id = fields.Many2one(comodel_name='gsos.supplier.profile',
        compute='_get_supplier_id', search='_search_supplier',
        string='Supplier')

    @api.depends('audit_id')
    def _get_supplier_id(self):
        self.ensure_one()
        self.supplier_id = self.audit_id.supplier_id

    def _search_supplier(self, operator, value):
        return [('name', operator, value)]

class GsosAuditReportQuestion(models.Model):
    _name = 'gsos.audit.report.question'
    _description = 'Audit Report Question'
    _inherit = ['mail.thread']

    name = fields.Char(string='Code', default='New', readonly=True)
    section_id = fields.Many2one(comodel_name='gsos.audit.report.section', string='Section')
    question = fields.Text(string='Text')
    rating = fields.Char(string='Rating')
    nonconformance_description = fields.Text(string='Nonconformance Description')
    objective_evidence = fields.Text(string='Objective Evidence')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('gsos.audit.report.question') or 'New'
        result = super(GsosAuditReportQuestion, self).create(vals)
        return result

class GsosAuditReportNoConformance(models.Model):
    _name = 'gsos.audit.report.noconformance'
    _description = 'Audit Report Noconformance'
    _inherit = ['mail.thread']

    name = fields.Char(string='Code', default='New', readonly=True)
    audit_id = fields.Many2one(comodel_name='gsos.audit', string='Audit')
    question_id = fields.Many2one(comodel_name='gsos.audit.report.question', string='Question')
    question_text = fields.Text(compute='_get_question_text', string='Requirement')
    question_rating = fields.Char(compute='_get_question_rating', string='Rating')
    noconformance_description = fields.Text(compute='_get_noconformance_description', string='Noconformance Description')
    corrective_action_plan = fields.Text(string='Corrective Action Plan')
    date_target = fields.Date(string='Target Date')
    action_ids = fields.One2many(comodel_name='gsos.audit.report.noconformance.action',
        inverse_name='noconformance_id', string='Actions')

    status = fields.Selection(
        selection=[
          ('open', 'Open'),
          ('closed', 'Closed')
        ],
        string='State',
        default='open')

    @api.depends('question_id')
    def _get_question_text(self):
        self.ensure_one()
        self.question_text = self.question_id.question

    @api.depends('question_id')
    def _get_question_rating(self):
        self.ensure_one()
        self.question_rating = self.question_id.rating

    @api.depends('question_id')
    def _get_noconformance_description(self):
        self.ensure_one()
        self.noconformance_description = self.question_id.nonconformance_description

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('gsos.audit.report.noconformance') or 'New'
        result = super(GsosAuditReportNoConformance, self).create(vals)
        return result

class GsosAuditReportNoConformanceAction(models.Model):
    _name = 'gsos.audit.report.noconformance.action'
    _description = 'Audit Report Noconformance Action'

    noconformance_id = fields.Many2one(comodel_name='gsos.audit.report.noconformance', string='Noconformance')
    action = fields.Text(string='Action')
    responsible = fields.Char(strng='Responsible')
    date_target = fields.Date(string='Target Date')

class GsosAuditReportComment(models.Model):
    _name = 'gsos.audit.report.comment'
    _description = 'Audit Report Comments'
    _inherit = ['mail.thread']

    audit_id = fields.Many2one(comodel_name='gsos.audit', string='Audit')
    name = fields.Char(string='Title')
    comment = fields.Text(string='Comments')
