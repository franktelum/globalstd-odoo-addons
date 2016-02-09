# -*- coding: utf-8 -*-

from openerp import api, fields, models

# Contrato
class ResPartner(models.Model):
    _inherit = ['res.partner']

    type = fields.Selection(selection_add=[('site', 'Site address')])

    # Campos pertenecientes a la tabla clientes de GPS
    gpsi_id_leader_sales = fields.Integer(string='Id Leader Sales')
    gpsi_id_auditor = fields.Integer(string='Id Auditor Rec')
    gpsi_id_consultor = fields.Char(string='Id Consultor Rec')
    gpsi_id_fuente = fields.Integer(string='Id Fuente')
    gpsi_id_referencia = fields.Integer(string='Id Referencia')
    gpsi_id_ref_prog = fields.Integer(string='Id Coordinador Logistica')
    gpsi_id_oficina = fields.Char(string='Id Oficina')
    gpsi_id_md5_qms = fields.Char(string='Id Md5QMS')
    gpsi_id_cliente = fields.Char(string='Id Cliente')

    gpsi_recommended = fields.Char(string='Id Recomendado')
    gpsi_cve_cliente = fields.Char(string='Clave Cliente')
    gpsi_rfc = fields.Char(string='RFC')
    gpsi_domicilio_fiscal = fields.Char(string='Domicilio Fiscal')
    gpsi_perfil = fields.Char(string='Perfil')
    gpsi_archivo_perfil = fields.Char(string='Archivo Perfil')
    gpsi_nick_name = fields.Char(string='Nick Name')
    gpsi_password = fields.Char(string='Password')
    gpsi_no_empleados = fields.Char(string='No Empleados')

    gpsi_contract_ids = fields.One2many(comodel_name='gps.contratos', inverse_name='cliente_id', string='Contracts')
    gpsi_ubicaciones_cliente_ids = fields.Many2many(comodel_name='gps.ubicaciones', column1='cliente_id', column2='ubicacion_id', string='Locations')
    gpsi_nacecode_cliente_ids = fields.Many2many(comodel_name='gps.nacecode', column1='cliente_id', column2='nacecode_id', string='NACE Codes')

    gpsi_contract_count = fields.Integer(compute='_compute_contract_count', string='Number contracts attached')

    @api.multi
    @api.depends('gpsi_contract_ids')
    def _compute_contract_count(self):
        for partner in self:
            partner.gpsi_contract_count = len(partner.gpsi_contract_ids)
