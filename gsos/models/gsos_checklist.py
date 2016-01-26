# -*- coding: utf-8 -*-

from openerp import api, fields, models

class GsosChecklist(models.Model):
    _name = 'gsos.checklist'
    _description = 'Checklist'
    _inherit = ['mail.thread']

    name = fields.Char(string='Name')
    template_url = fields.Char(string='Template')
    revision = fields.Integer(string='Revision')
