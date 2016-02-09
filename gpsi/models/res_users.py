# -*- coding: utf-8 -*-

from openerp import api, fields, models

# Contrato
class ResUsers(models.Model):
    _inherit = ['res.users']

    gpsi_id_user = fields.Integer(string='Id User')
    gpsi_id_oficina = fields.Char(string='Id Oficina')
    gpsi_cuota_pago = fields.Float(string='Cuota Pago')
    gpsi_auditor_lider = fields.Boolean(string='Auditor Lider')
