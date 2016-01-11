# -*- coding: utf-8 -*-

from openerp import api, fields, models

class GsosComplaint(models.Model):
    _name = 'gsos.complaint'
    _description = 'Complaint'
    _inherit = ['mail.thread']

    name = fields.Char(string='Code', default='New', readonly=True)
    user_id = fields.Many2one(comodel_name='res.users', string='User')
    supplier_id = fields.Many2one(comodel_name='res.partner', string='Supplier')
    monitor = fields.Char(string='Monitor')
    reason = fields.Text(string='Reason')

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


    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('gsos.complaint') or 'New'
        result = super(GsosComplaint, self).create(vals)
        return result
