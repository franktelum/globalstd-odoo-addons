# -*- coding: utf-8 -*-

from openerp import api, fields, models

class GpsEventos(models.Model):
    _name = 'gps.eventos'
    _description = 'Event'
    _inherit = ['mail.thread']

    _rec_name = 'numero_trabajo'

    id_habilidad = fields.Integer(string='Id Habilidad')
    id_contrato = fields.Char(string='Id Contrato')
    id_cliente = fields.Char(string='Id Cliente')
    id_revisor = fields.Integer(string='Id Revisor')
    id_comite = fields.Integer(string='Id Comite')
    id_ubicacion = fields.Char(string='Id Ubicación')
    id_client_service = fields.Integer(string='Id Cliente Service')
    id_oficina = fields.Char(string='Id Oficina')
    id_eventos_facturacion = fields.Char(string='Id Eventos Facturacion')
    id_archivo_plan_auditoria = fields.Char(string='Archivo Plan Auditoría')
    id_archivo_reporte_auditoria = fields.Char(string='Archivo Reporte Auditoría')

    habilidad_id = fields.Many2one(comodel_name='gps.habilidades', string='Standard')
    contrato_id = fields.Many2one(comodel_name='gps.contratos', string='Agreement')
    cliente_id = fields.Many2one(comodel_name='res.partner', string='Client')
    revisor_id = fields.Many2one(comodel_name='res.users', string='Review')
    comite_id = fields.Many2one(comodel_name='res.users', string='Committe')
    ubicacion_id = fields.Many2one(comodel_name='gps.ubicaciones', string='Location')
    client_service_id = fields.Many2one(comodel_name='res.users', string='Client Service')
    oficina_id = fields.Many2one(comodel_name='gps.oficinas', string='Office')
    eventos_facturacion_id = fields.One2many(comodel_name='gps.eventos.facturacion', inverse_name='numero_trabajo_id', string='Event Billing')
    archivo_plan_auditoria_id = fields.Many2one(comodel_name='ir.attachment', string='Audit Plan')
    archivo_reporte_auditoria_id = fields.Many2one(comodel_name='ir.attachment', string='Audit Report')

    usuarios_evento_ids = fields.One2many(comodel_name='gps.usuarios.evento', inverse_name='numero_trabajo_id', string='Auditors')
    no_conformidades_ids = fields.One2many(comodel_name='gps.noconformidades', inverse_name='numero_trabajo_id', string='Non Conformances')
    no_conformidades_count = fields.Integer(compute='_compute_no_conformidades', string='Number non conformances attached')
    archivos_revisor_ids = fields.One2many(comodel_name='gps.archivos.tracking', inverse_name='numero_trabajo_id', string='Documents')

    numero_trabajo = fields.Char(string='Número de Trabajo')
    domicilio = fields.Char(string='Domicilio')
    fecha_inicio = fields.Date(string='Fecha Inicio')
    fecha_termino = fields.Date(string='Fecha Termino')
    estado_evento = fields.Selection(
        selection=[
          (1, 'Scheduled'),
          (2, 'Confirmed'),
          (3, 'Executed'),
          (4, 'Review'),
          (5, 'Committee'),
          (6, 'Closed')
        ],
        default=1, string='Estado Evento')
    tipo_evento = fields.Selection(
        selection=[
          (0, 'Todos'),
          (1, 'Ninguno'),
          (2, 'Pre-Auditoria'),
          (3, 'Etapa I'),
          (4, 'Etapa II'),
          (5, 'Seguimiento 1'),
          (6, 'CARS'),
          (7, 'Recertificacion'),
          (8, 'Seguimiento 2'),
          (9, 'Seguimiento 3'),
          (10, 'Seguimiento 4'),
          (11, 'Seguimiento 5'),
          (12, 'Transferencia'),
          (13, 'Recertificacion'),
          (14, 'Takeover'),
          (16, 'Auditoria Especial'),
          (17, 'RR Prior to Expiration')
        ],
        string='Tipo Evento')
    introduccion = fields.Char(string='Introducción')
    pago = fields.Float(string='Pago')
    fecha_aviso = fields.Date(string='Fecha Aviso')
    comentarios = fields.Text(string='Comentarios')
    estado_revisor = fields.Selection(
        selection=[
          (0, 'None'),
          (1, 'Approved'),
          (2, 'Hold'),
          (3, 'Review')
        ],
        string='Estado Revisor')
    nota_revisor = fields.Text(string='Nota Revisor')
    estado_comite = fields.Selection(
        selection=[
          (0, 'None'),
          (1, 'Approved'),
          (2, 'Hold'),
          (3, 'Review')
        ],
        string='Estado Comite')
    nota_comite = fields.Text(string='Nota Comite')
    no_seguimiento_trans = fields.Integer(string='No Seguimiento Trans')
    estado_republica = fields.Char(string='Estado Republica')
    discapacidad = fields.Boolean(string='¿Discapacidad?')
    es_conferencia = fields.Boolean(string='¿Es Conferencia?')
    ciudad = fields.Char(string='Ciudad')
    nota_auditor = fields.Text(string='Nota Auditor')
    estatus = fields.Selection(
        selection=[
          (0, 'Created'),
          (1, 'Rejected'),
          (2, 'Approved')
        ],
        string='Estatus')
    fecha_envio_fssc = fields.Date(string='Fecha Envio FSSC')

    def _compute_no_conformidades(self):
        self.ensure_one()
        non_conformances = self.env['gps.noconformidades'].search([['numero_trabajo_id', '=', self.id]])
        self.no_conformidades_count = len(non_conformances)

    @api.model
    def create(self, vals):
        if vals.get('numero_trabajo', 'New') == 'New':
            vals['numero_trabajo'] = self.env['ir.sequence'].next_by_code('gps.eventos') or 'New'
        return super(GpsEventos, self).create(vals)
