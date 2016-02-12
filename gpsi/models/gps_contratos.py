# -*- coding: utf-8 -*-

import logging
from openerp import api, fields, models

_logger = logging.getLogger(__name__)

class GpsContratos(models.Model):
    _name = 'gps.contratos'
    _description = 'Contract'
    _inherit = ['mail.thread']

    _rec_name = 'no_contrato'

    id_cliente = fields.Char(string='Id Cliente')
    id_habilidad = fields.Integer(string='Id Habilidad')
    id_revisor = fields.Integer(string='Id Revisor')
    id_ventas = fields.Integer(string='Id Ventas')
    id_md5_qms = fields.Integer(string='Id MD5QMS')
    id_archivo_contrato = fields.Char(string='Archivo Contrato')
    id_archivo_cuestionario = fields.Char(string='Archivo Cuestionario')
    id_archivo_carta = fields.Char(string='Archivo Carta')
    id_archivo_cotizacion = fields.Char(string='Archivo Cotización')
    id_archivo_transferencia = fields.Char(string='Archivo Transferencia')
    id_archivo_rev_auditor = fields.Char(string='Archivo Rev. Auditor')
    id_archivo_certificado = fields.Char(string='Archivo Certificado')

    cliente_id = fields.Many2one(comodel_name='res.partner', string='Client')
    habilidad_id = fields.Many2one(comodel_name='gps.habilidades', string='Standard')
    revisor_id = fields.Many2one(comodel_name='res.users', string='Review')
    ventas_id = fields.Many2one(comodel_name='res.users', string='Salesperson')
    md5_qms_id = fields.Many2one(comodel_name='gps.md5qms', string='MD5QMS')
    archivo_contrato_id = fields.Many2one(comodel_name='ir.attachment', string='Contract File')
    archivo_cuestionario_id = fields.Many2one(comodel_name='ir.attachment', string='Questionary File')
    archivo_carta_id = fields.Many2one(comodel_name='ir.attachment', string='Letter File')
    archivo_cotizacion_id = fields.Many2one(comodel_name='ir.attachment', string='Quotation File')
    archivo_transferencia_id = fields.Many2one(comodel_name='ir.attachment', string='Transfer File')
    archivo_rev_auditor_id = fields.Many2one(comodel_name='ir.attachment', string='Audit Review File')
    archivo_certificado_id = fields.Many2one(comodel_name='ir.attachment', string='Certificate File')
    eventos_contrato_ids = fields.One2many(comodel_name='gps.eventos.contrato', inverse_name='contrato_id', string='Order Lines')
    ubicaciones_contrato_ids = fields.One2many(comodel_name='gps.ubicaciones.contrato', inverse_name='contrato_id', string='Locations')
    ubicaciones_cliente_ids = fields.Many2many(related='cliente_id.gpsi_ubicaciones_cliente_ids', string='Locations')
    nacecodes_cliente_ids = fields.Many2many(related='cliente_id.gpsi_nacecode_cliente_ids', string='NACE Codes')

    id_contrato = fields.Char(string='Id Contrato')
    no_contrato = fields.Char(string='No Contrato', default='New')
    esquema = fields.Selection(
        selection=[
          (0, 'Biannual'),
          (1, 'Annual')
        ],
        default=1,
        string='Esquema')
    ap_diseno = fields.Boolean(string='¿Aplica Diseño?')
    multisitio = fields.Boolean(string='¿Es Multisitio?')
    multilocate = fields.Boolean(string='¿Es Multilocalidad?')
    bilingue = fields.Boolean(string='¿Necesita Auditor Bilingüe?')
    nivel_riesgo = fields.Char(string='Nivel Riesgo')
    duracion = fields.Selection(
        selection=[
          (1, '1 Year'),
          (2, '2 Year'),
          (3, '3 Year')
        ],
        default=1,
        string='Duracion')
    fecha_contrato = fields.Date(string='Fecha Contrato')
    notas = fields.Text(string='Notas')
    cancelado = fields.Boolean(string='¿Cancelado?')
    transferencia = fields.Boolean(string='¿Transferencia?')

    #Mapeado a external id
    estado_revisor = fields.Selection(
        selection=[
          (0, 'Draft'),
          (1, 'Approved'),
          (2, 'Hold'),
          (3, 'Review')
        ],
        default=0,
        string='Estado Revisor')
    nota_revisor = fields.Char(string='Nota Revisor')
    fee01 = fields.Float(string='Fee01')
    fee02 = fields.Float(string='Fee02')
    fee03 = fields.Float(string='Fee03')
    ciclo_contrato = fields.Integer(string='Ciclo Contrato', required=True, default=1)
    moneda_tipo = fields.Selection(
        selection=[
          (0, 'Otro'),
          (1, 'Peso'),
          (2, 'Dollar'),
          (3, 'Euro'),
          (4, 'Canadian dollar')
        ],
        default=1,
        string='Tipo Moneda')
    moneda_tipo_cambio = fields.Float(string='Tipo de Cambio')
    recertificacion = fields.Boolean(string='¿Recertificación?')
    finalizado = fields.Boolean(string='¿Finalizado?')
    informacion_avance = fields.Text(string='Información Avance')
    fechainicio = fields.Date(string='Fecha Inicio')
    fechafin = fields.Date(string='Fecha Fin')
    tipocertificacion = fields.Selection(
        selection=[
          (1, 'Initial'),
          (2, 'Recertification'),
          (3, 'Takeover')
        ],
        default=1,
        string='Tipo Certificación')
    mostrarnace = fields.Boolean(string='¿Mostrar NACE?')
    tipoesquema = fields.Char(string='Tipo Esquema', required=True)
    bloquearcontrato = fields.Boolean(string='¿Bloquear Contrato?')
    estatus_certificado = fields.Selection(
        selection=[
          (0, 'Active'),
          (1, 'Expired'),
          (2, 'Suspended'),
          (3, 'Canceled')
        ],
        string='Estatus Certificado')
    haccp = fields.Integer(string='HACCP')
    aplica_viaticos = fields.Selection(
        selection=[
          (0, 'No Aplica'),
          (1, 'Aplica'),
          (2, 'Especial')
        ],
        string='Aplica Viaticos')
    observaciones_viaticos = fields.Char(string='Observaciones Viaticos')
    report_time = fields.Float(string='Report Time')
    event_count = fields.Integer(compute='_compute_event_count', string='Number events attached')
    amount_total = fields.Float(compute='_get_amount_total', string='Total')
    no_empleados_compute = fields.Char(compute='_get_no_empleados', inverse='_set_no_empleados', string='Number employees')
    no_empleados = fields.Char()
    vigente = fields.Boolean(compute='_compute_vigente', string='Currently active')

    # Compute and search fields
    def _compute_event_count(self):
        self.ensure_one()
        events = self.env['gps.eventos'].search([['contrato_id', '=', self.id]])
        self.event_count = len(events)

    @api.depends('no_empleados','cliente_id')
    def _get_no_empleados(self):
        self.ensure_one()
        if not self.no_empleados:
            clients = self.env['res.partner'].browse([self.cliente_id.id])
            self.no_empleados_compute = clients[0].gpsi_no_empleados
        else:
            self.no_empleados_compute = self.no_empleados

    @api.depends('no_empleados')
    def _set_no_empleados(self):
        self.ensure_one()
        self.no_empleados = self.no_empleados_compute

    @api.depends('cancelado','finalizado')
    def _compute_vigente(self):
        for contrato in self:
            if (contrato.finalizado or contrato.cancelado):
                contrato.vigente = False
            else:
                contrato.vigente = True

    @api.depends('archivo_certificado')
    def _get_archivo_certificado_url(self):
        self.ensure_one()
        if self.archivo_certificado:
            self.archivo_certificado_url = 'http://gps.globalstd.com/gps/Documentos/' + self.archivo_certificado

    @api.depends('eventos_contrato_ids')
    def _get_amount_total(self):
        self.ensure_one()
        amount_total = 0;
        for evento_contrato in self.eventos_contrato_ids:
            amount_total += evento_contrato.costo
        self.amount_total = amount_total

    # CRUD methods
    @api.model
    def create(self, vals):
        if vals.get('no_contrato', 'New') == 'New':
            vals['no_contrato'] = self.env['ir.sequence'].next_by_code('gps.contratos') or 'New'
        return super(GpsContratos, self).create(vals)
