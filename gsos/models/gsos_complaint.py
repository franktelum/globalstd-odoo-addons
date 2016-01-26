# -*- coding: utf-8 -*-

from openerp import api, fields, models

class GsosComplaint(models.Model):
    _name = 'gsos.complaint'
    _description = 'Complaint'
    _inherit = ['mail.thread']

    name = fields.Char(string='Code', default='New', readonly=True)
    supplier_id = fields.Many2one(comodel_name='gsos.supplier.profile', string='Supplier')
    monitor = fields.Char(string='Monitor')
    reason = fields.Text(string='Reason')
    corrective_action = fields.Text(string='Corrective Action')
    auditor_comments = fields.Text(string='Auditor Comments')
    document_count = fields.Integer(compute='_get_document_count', string='Number documents attached')

    severity = fields.Selection(
        selection=[
          ('low', 'Low'),
          ('medium', 'Medium'),
          ('high', 'High')
        ],
        string='Severity')

    state = fields.Selection(
        selection=[
          ('open', 'Open'),
          ('closed', 'Closed')
        ],
        string='State',
        default='open')

    def _get_document_count(self):
        self.ensure_one()
        attachments = self.env['ir.attachment'].search([['res_id', '=', self.id]])
        self.document_count = len(attachments)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('gsos.complaint') or 'New'
        result = super(GsosComplaint, self).create(vals)
        return result
