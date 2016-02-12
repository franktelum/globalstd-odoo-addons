# -*- coding: utf-8 -*-

from openerp import api, fields, models

class GpsCertificacionTipo(models.Model):
    _name = 'gps.certificacion.tipo'
    _description = 'gps.certificacion.tipo'

    id_certificacion_tipo = fields.Char(string='ID Certificacion Tipo')
    name = fields.Char(string='Name')

class GpsHabilidades(models.Model):
    _name = 'gps.habilidades'
    _description = 'gps.habilidades'

    _rec_name = 'nombre'

    id_habilidad = fields.Integer(string='ID Habilidad')
    id_padre = fields.Integer(string='Id Padre')

    padre_id = fields.Many2one(comodel_name='gps.habilidades', string='Father')

    nombre = fields.Char(string='Nombre')
    tipo = fields.Integer(string='Tipo')
    description = fields.Char(string='Description')
    no_horas = fields.Integer(string='No Horas')
    costo_persona = fields.Float(string='Costo Persona')
    tipo_moneda = fields.Integer(string='Tipo Moneda')
    es_seminario = fields.Boolean(string='¿Es Seminario?')
    abrevacion = fields.Char(string='Abreviación')
    tipo_curso = fields.Char(string='Tipo Curso')
    manual = fields.Char(string='Manual')

class GpsFuente(models.Model):
    _name = 'gps.fuente'
    _description = 'gps.fuente'

    _rec_name = 'name'

    id_fuente = fields.Char(string='ID Fuente')

    name = fields.Char(string='Name')

class GpsRecommended(models.Model):
    _name = 'gps.recommended'
    _description = 'gps.recommended'

    _rec_name = 'name'

    id_recommended = fields.Char(string='ID Recommended')

    name = fields.Char(string='Name')

class GpsNaceCode(models.Model):
    _name = 'gps.nacecode'
    _description = 'gps.nacecode'

    _rec_name = 'nombre'

    id_nacecode = fields.Char(string='ID NaceCode')
    id_habilidad = fields.Integer(string='Id Habilidad')

    habilidad_id = fields.Many2one(comodel_name='gps.habilidades', string='Ability')

    #id_nace_code = fields.Integer(string='Id NaceCode')
    nombre = fields.Char(string='Nombre')
    description = fields.Char(string='Descripción')
    baja = fields.Integer(string='Baja')
    acreditado_por_anaf = fields.Boolean(string='Acreditado por ANAB')
    clase_riesgo = fields.Char(string='Clase Riesgo')
    iaf = fields.Integer(string='IAF')

class GpsNoConformidades(models.Model):
    _name = 'gps.noconformidades'
    _description = 'gps.noconformidades'

    _rec_name = 'id_numero_trabajo'

    id_noconformidad = fields.Char(string='ID NoConformidad')
    id_cliente = fields.Char(string='Id Cliente')
    id_numero_trabajo = fields.Char(string='Numero Trabajo')

    cliente_id = fields.Many2one(comodel_name='res.partner', string='Client')
    numero_trabajo_id = fields.Many2one(comodel_name='gps.eventos', string='Job Number')

    #id_no_conformidad = fields.Char(string='Id NoConformidad')
    sentencia = fields.Text(string='Sentencia')
    sentencia_archivo = fields.Char(string='Sentencia Archivo')
    tipo = fields.Integer(string='Tipo')
    contencion = fields.Text(string='Contencion')
    contencion_archivo = fields.Char(string='Contencion Archivo')
    causa_raiz = fields.Text(string='Causa Raiz')
    causa_raiz_archivo = fields.Char(string='Causa Raiz Archivo')
    implementacion = fields.Text(string='Implementacion')
    implementacion_archivo = fields.Char(string='Implementacion Archivo')
    status = fields.Integer(string='Status')
    notas = fields.Char(string='Notas')
    fecha_apertura = fields.Date(string='Fecha Apertura')
    fecha_cierre = fields.Date(string='Fecha Cierre')
    cierre_count = fields.Integer(string='Cierre Count')
    fecha_cambio = fields.Date(string='Fecha Cambio')
    in_site = fields.Boolean(string='In Site')

class GpsEventosFacturacion(models.Model):
    _name = 'gps.eventos.facturacion'
    _description = 'gps.eventos.facturacion'

    _rec_name = 'id_numero_trabajo'

    id_eventos_facturacion = fields.Char(string='Id Eventos Facturacion')
    id_usuario = fields.Char(string='Id Usuario')
    id_numero_trabajo = fields.Char(string='Id Numero Trabajo')

    usuario_id = fields.Many2one(comodel_name='res.users', string='User')
    numero_trabajo_id = fields.Many2one(comodel_name='gps.eventos', string='Job Number')

    estatus = fields.Selection(
        selection=[
          (0, 'Pendiente de Facturar'),
          (1, 'Facturado'),
          (2, 'NA'),
        ],
        string='Status')
    pagado = fields.Boolean(string='Pagado')
    fecha_pagado = fields.Date(string='Fecha Pagado')
    fecha_actualizacion = fields.Date(string='Fecha Actualizacion')
    fecha_facturado = fields.Date(string='Fecha Facturado')
    comentarios = fields.Text(string='Comentarios')

class GpsEventosConfirmacion(models.Model):
    _name = 'gps.eventos.confirmacion'
    _description = 'gps.eventos.confirmacion'

    _rec_name = 'id_numero_trabajo'

    id_eventos_confirmacion = fields.Char(string='Id Eventos Confirmacion')
    id_numero_trabajo = fields.Char(string='Id Numero Trabajo')

    numero_trabajo_id = fields.Many2one(comodel_name='gps.eventos', string='Job Number')

    confirmado = fields.Char(string='Confirmado')
    fecha = fields.Char(string='fecha')
    consultoria_previa = fields.Char(string='Consultoria Previa')
    comentarios = fields.Char(string='Comentarios')
    confirma_programacion = fields.Char(string='Confirma Programación')
    conflicto_intereses = fields.Char(string='Conflicto Intereses')

class GpsEventosContrato(models.Model):
    _name = 'gps.eventos.contrato'
    _description = 'gps.eventos.contrato'

    _rec_name = 'id_evento_contrato'

    id_evento_contrato = fields.Char(string='ID Eventos Contrato')
    id_contrato = fields.Char(string='Id Contrato')
    id_ubicacion = fields.Char(string='Id Ubicacion')

    contrato_id = fields.Many2one(comodel_name='gps.contratos', string='Contract')
    ubicacion_id = fields.Many2one(comodel_name='gps.ubicaciones', string='Location')

    #id_evento_contrato = fields.Char(string='Id Evento Contrato')
    tipo_evento_contrato = fields.Selection(
        selection=[
          (1, 'None'),
          (2, 'PreAuditoria'),
          (3, 'Etapa I'),
          (4, 'Etapa II'),
          (5, 'Seguimiento I'),
          (6, 'Cars'),
          (7, 'Recertificacion'),
          (8, 'Seguimiento II'),
          (9, 'Seguimiento III'),
          (10, 'Seguimiento IV'),
          (11, 'Seguimiento V'),
          (12, 'Transferencia'),
          (13, 'Recertificacionto'),
          (14, 'Takeover'),
          (15, 'Undefined'),
          (16, 'Auditoria Especial')
        ],
        string='Tipo Evento Contrato')
    dias = fields.Float(string='Dias')
    costo = fields.Float(string='Costo')

class GpsArchivos(models.Model):
    _name = 'gps.archivos'
    _description = 'gps.archivos'

    _rec_name = 'id_archivo'

    id_archivo = fields.Char(string='Id Archivo')
    id_propietario = fields.Char(string='Id Propietario')

    propietario_id = fields.Many2one(comodel_name='gps.noconformidades', string='Non Conformance')

    nombre = fields.Char(string='Nombre')
    fecha_registro = fields.Date(string='Fecha Registro')
    description = fields.Char(string='Description')

class GpsArchivosTracking(models.Model):
    _name = 'gps.archivos.tracking'
    _description = 'gps.archivos.tracking'

    _rec_name = 'id_archivo_tracking'

    id_archivo_tracking = fields.Char(string='Id Archivo Tracking')
    id_numero_trabajo = fields.Char(string='Numero Trabajo')

    numero_trabajo_id = fields.Many2one(comodel_name='gps.eventos', string='Job Number')

    nombre = fields.Char(string='Nombre')
    fecha_registro = fields.Date(string='Fecha Registro')
    tipo_archivo = fields.Selection(
        selection=[
          ('CliRepP', 'Client Report'),
          ('AudRep', 'Audit Report'),
          ('AudPlanP', 'Audit Plan'),
          ('OpeClos', 'Attendance/Opening and Closing Meeting'),
          ('ResShe', 'Results Sheet')
        ],
        string='Tipo Archivo')
    numero_archivo = fields.Integer(string='Número Archivo')

class GpsArchivosEvento(models.Model):
    _name = 'gps.archivos.evento'
    _description = 'gps.archivos.evento'

    _rec_name = 'id_archivo_evento'

    id_archivo_evento = fields.Char(string='Id Archivo Evento')
    id_numero_trabajo = fields.Char(string='Numero Trabajo')

    numero_trabajo_id = fields.Many2one(comodel_name='gps.eventos', string='Job Number')

    nombre_archivo = fields.Char(string='Nombre Archivo')

class GpsArchivosHistorial(models.Model):
    _name = 'gps.archivos.historial'
    _description = 'gps.archivos.historial'

    _rec_name = 'id_archivo_historial'

    id_archivo_historial = fields.Char(string='Id Archivo Historial')
    id_numero_trabajo = fields.Char(string='Numero Trabajo')

    numero_trabajo_id = fields.Many2one(comodel_name='gps.eventos', string='Job Number')

    fecha = fields.Date(string='Fecha')
    numero_archivo = fields.Integer(string='Número Archivo')

class GpsArchivosUsuarios(models.Model):
    _name = 'gps.archivos.usuarios'
    _description = 'gps.archivos.usuarios'

    _rec_name = 'nombre_archivo'

    id_archivos_usuario = fields.Char(string='ID Archivos Usuario')
    id_archivo = fields.Char(string='Id Archivo')
    id_nacecode_soporte = fields.Char(string='Id NaceCode Soporte')
    id_usuario = fields.Char(string='Id Usuario')
    id_nacecode = fields.Char(string='Id NaceCode')

    archivo_id = fields.Many2one(comodel_name='gps.archivos', string='File')
    nacecode_soporte_id = fields.Char(comodel_name='gps.nacecodes.usuario.soporte', string='NaceCode Support')
    usuario_id = fields.Many2one(comodel_name='res.users', string='User')
    nacecode_id = fields.Many2one(comodel_name='gps.nacecodes', string='NaceCode')

    tipo_archivo = fields.Char(string='Id Tipo Archivo')
    nombre_archivo = fields.Char(string='Nombre Archivo')

class GpsAuditorExpertoTecnico(models.Model):
    _name = 'gps.usuarios.auditorexpertotecnixo'
    _description = 'gps.archivos.auditorexpertotecnixo'

    _rec_name = 'id_auditor'

    id_auditor_expertotecnico = fields.Char(string='ID Auditor Experto Tecnico')
    id_cliente = fields.Char(string='Id Cliente')
    id_auditor = fields.Char(string='Id Auditor')

    cliente_id = fields.Many2one(comodel_name='res.partner', string='Client')
    auditor_id = fields.Many2one(comodel_name='res.users', string='Auditor')

    fecha = fields.Date(string='Fecha')

class GpsComentarioCliente(models.Model):
    _name = 'gps.clientes.comentario'
    _description = 'gps.clientes.comentario'

    _rec_name = 'id_cliente'

    id_comentario_cliente = fields.Char(string='ID Comentario Cliente')
    id_cliente = fields.Char(string='Id Cliente')
    id_oficina = fields.Char(string='Id Oficina')
    id_proceso = fields.Char(string='Id Proceso')
    id_user_connected = fields.Char(string='Id User Connected')

    cliente_id = fields.Many2one(comodel_name='res.partner', string='Client')
    oficina_id = fields.Many2one(comodel_name='gps.oficinas', string='Office')
    proceso_id = fields.Many2one(comodel_name='gps.procesos.global', string='Process')
    user_connected_id = fields.Many2one(comodel_name='res.users', string='User Connected')

    comentario = fields.Char(string='Comentario')
    fecha = fields.Date(string='Fecha')


class GpsComentariosTracking(models.Model):
    _name = 'gps.clientes.comentario.tracking'
    _description = 'gps.clientes.comentario.tracking'

    _rec_name = 'id_numero_trabajo'

    id_comentario_tracking = fields.Char(string='Id Comentario Tracking')
    id_numero_trabajo = fields.Char(string='Id Numero Trabajo')

    numero_trabajo_id = fields.Many2one(comodel_name='gps.eventos', string='Job Number')

    #comentarios_tracking_key = fields.Char(string='Comentarios Tracking Key')
    comentarios = fields.Char(string='Comentarios')

class GpsEncuestas(models.Model):
    _name = 'gps.encuestas'
    _description = 'gps.encuestas'

    _rec_name = 'fecha_creado'

    id_encuesta = fields.Char(string='ID Encuesta')

    revision = fields.Char(string='Revision')
    tipo_evento = fields.Integer(string='Tipo Evento')
    activo = fields.Boolean(string='Activo')
    fecha_creado = fields.Date(string='Fecha Creado')

class GpsEncuestasClientes(models.Model):
    _name = 'gps.encuestas.clientes'
    _description = 'gps.encuestas.clientes'

    _rec_name = 'id_numero_trabajo'

    id_encuesta_cliente = fields.Char(string='Id Encuesta Cliente')
    id_numero_trabajo = fields.Char(string='Id Numero Trabajo')
    id_md5 = fields.Char(string='Id MD5')
    id_encuesta = fields.Char(string='Encuesta Id')

    numero_trabajo_id = fields.Many2one(comodel_name='gps.eventos', string='Job Number')
    md5_id = fields.Many2one(comodel_name='gps.md5qms', string='MD5')
    encuesta_id = fields.Many2one(comodel_name='gps.encuestas', string='Quiz')

    fecha_enviado = fields.Date(string='Fecha Enviado')
    fecha_resuelto = fields.Date(string='Fecha Resuelto')
    acciones = fields.Char(string='Accionestring=s')
    quejas = fields.Char(string='Quejas')

class GpsEncuestasClientesRespuestas(models.Model):
    _name = 'gps.encuestas.clientes.respuestas'
    _description = 'gps.encuestas.clientes.respuestas'

    _rec_name = 'id_numero_trabajo'

    id_encuesta_cliente_respuesta = fields.Char(string='Id Encuesta Cliente Respuesta')
    id_numero_trabajo = fields.Char(string='Id Numero Trabajo')
    id_encuesta_respuesta = fields.Char(string='Encuestas Respuestas Id')

    numero_trabajo_id = fields.Many2one(comodel_name='gps.eventos', string='Job number')
    encuesta_respuesta_id = fields.Many2one(comodel_name='gps.encuestas.respuestas', string='Quiz Answer')

class GpsEncuestasClientesRespuestasComentarios(models.Model):
    _name = 'gps.encuestas.clientes.respuestas.comentarios'
    _description = 'gps.encuestas.clientes.respuestas.comentarios'

    _rec_name = 'id_numero_trabajo'

    id_encuesta_cliente_respuesta_comentario = fields.Char(string='Id Encuesta Cliente Respuesta Comentario')
    id_encuesta_respuesta = fields.Char(string='Encuestas Respuestas Id')
    id_numero_trabajo = fields.Char(string='Id Numero Trabajo')

    encuesta_respuesta_id = fields.Many2one(comodel_name='gps.encuestas.respuestas', string='Quiz Answer')
    numero_trabajo_id = fields.Many2one(comodel_name='gps.eventos', string='Jon Number')

    comentario = fields.Char(string='Comentario')

class GpsEncuestasPreguntas(models.Model):
    _name = 'gps.encuestas.preguntas'
    _description = 'gps.encuestas.preguntas'

    _rec_name = 'pregunta'

    id_encuesta_pregunta = fields.Char(string='ID Encuesta Pregunta')
    id_encuesta = fields.Char(string='Encuesta Id')

    encuesta_id = fields.Many2one(comodel_name='gps.encuestas', string='Quiz')

    idioma = fields.Char(string='Idioma')
    pregunta = fields.Char(string='Pregunta')
    orden = fields.Integer(string='Orden')

class GpsEncuestasRespuestas(models.Model):
    _name = 'gps.encuestas.preguntas'
    _description = 'gps.encuestas.preguntas'

    _rec_name = 'encuesta_pregunta_id'

    id_encuesta_respuesta = fields.Char(string='ID Encuesta Respuesta')
    id_encuesta_pregunta = fields.Char(string='Encuesta Pregunta Id')

    encuesta_pregunta_id = fields.Many2one(comodel_name='gps.encuestas.preguntas', string='Quiz Question')

    respuesta = fields.Char(string='Respuesta')
    valor = fields.Integer(string='Valor')
    orden = fields.Char(string='Orden')

class GpsLastNC(models.Model):
    _name = 'gps.lastnc'
    _description = 'gps.lastnc'

    _rec_name = 'id_numero_trabajo'

    id_lastnc = fields.Char(string='Id LastNC')
    id_no_conformidades = fields.Char(string='Id No Conformidades')
    id_numero_trabajo = fields.Char(string='Id Numero Trabajo')

    no_conformidades_id = fields.Many2one(comodel_name='gps.noconformidades', string='No Conformances')
    numero_trabajo_id = fields.Many2one(comodel_name='gps.eventos', string='Job Number')

    fecha_apertura = fields.Date(string='Fecha Apertura')

class GpsMD5QMS(models.Model):
    _name = 'gps.md5qms'
    _description = 'gps.md5qms'

    _rec_name = 'num_empleados'

    id_md5qms = fields.Char(string='ID MD5QMS')
    id_habilidad = fields.Char(string='Id Habilidad')

    num_empleados = fields.Char(string='Num Empleados')
    dias_auditor = fields.Float(string='Dias Auditor')

class GpsNaceCodesCliente(models.Model):
    _name = 'gps.nacecodes.cliente'
    _description = 'gps.nacecodes.cliente'

    _rec_name = 'id_nacecode'

    id_nacecode_cliente = fields.Char(string='ID NaceCode Cliente')
    id_nacecode = fields.Char(string='Id NaceCode')
    id_cliente = fields.Char(string='Id Cliente')

    nacecode_id = fields.Many2one(comodel_name='gps.nacecode', string='NaceCode')
    cliente_id = fields.Many2one(comodel_name='res.partner', string='Client')

class GpsNaceCodesUsuario(models.Model):
    _name = 'gps.nacecodes.usuario'
    _description = 'gps.nacecodes.usuario'

    _rec_name = 'id_usuario'

    id_nacecode_usuario = fields.Char(string='ID NaceCode Usuario')
    id_usuario = fields.Char(string='Id Usuario')
    id_nacecode = fields.Char(string='Id NaceCode')

    usuario_id = fields.Many2one(comodel_name='res.users', string='User')
    nacecode_id = fields.Many2one(comodel_name='gps.nacecodes', string='NaceCode')

    calificacion = fields.Integer(string='Calificacion')

class GpsNaceCodesUsuariosSoporte(models.Model):
    _name = 'gps.nacecodes.usuario.soporte'
    _description = 'gps.nacecodes.usuario.soporte'

    _rec_name = 'nombre_archivo'

    id_nacecode_usuario_soporte = fields.Char(string='ID NaceCode Usuario Soporte')
    id_usuario = fields.Char(string='Id Usuario')
    id_nacecode = fields.Char(string='Id NaceCode')

    usuario_id = fields.Many2one(comodel_name='res.users', string='User')
    nacecode_id = fields.Many2one(comodel_name='gps.nacecodes', string='NaceCode')

    tipo_archivo = fields.Char(string='Tipo Archivo')
    nombre_archivo = fields.Char(string='Nombre Archivo')
    extension = fields.Char(string='Extension')
    aprobado = fields.Boolean(string='Aprobado')
    calificacion = fields.Integer(string='Calificacion')
    comentarios_auditor = fields.Char(string='Comentarios Auditor')
    comentarios_admin = fields.Char(string='Comentarios Admin')
    fecha_creado = fields.Date(string='Fecha Creado')
    fecha_actualizado = fields.Date(string='Fecha Actualizado')
    fecha_aprobado = fields.Date(string='Fecha Aprobado')
    descripcion = fields.Char(string='Descripcion')

class GpsNaceCodesUsuariosSoporteArchivo(models.Model):
    _name = 'gps.nacecodes.usuario.soporte.archivo'
    _description = 'gps.nacecodes.usuario.soporte.archivo'

    _rec_name = 'id_nacecode_soporte'

    id_nacecode_usuario_soporte_archivo = fields.Char(string='ID NaceCode Usuario Soporte Archivo')
    id_nacecode_soporte = fields.Char(string='Id NaceCode Soporte')

    nacecode_soporte_id = fields.Many2one(comodel_name='gps.nacecodes.usuario.soporte', string='NaceCode Support')

class GpsNoConformidadesAcciones(models.Model):
    _name = 'gps.noconformidades.acciones'
    _description = 'gps.noconformidades.acciones'
    _inherit = ['mail.thread']

    _rec_name = 'id_numero_trabajo'

    id_noconformidades_archivo = fields.Char(string='Id NoConformidades Archivo')
    id_numero_trabajo = fields.Char(string='Id Numero Trabajo')

    numero_trabajo_id = fields.Many2one(comodel_name='gps.eventos', string='Job Number')

    seccion = fields.Integer(string='Seccion')
    nombre_archivo = fields.Char(string='Nombre Archivo')
    ocurrio_error = fields.Boolean(string='Ocurrio Error')
    descripcion_error = fields.Char(string='Descripcion Error')
    instante_accion = fields.Date(string='Instante Accion')

class GpsOficinas(models.Model):
    _name = 'gps.oficinas'
    _description = 'gps.oficinas'

    _rec_name = 'nombre'

    id_oficina = fields.Char(string='ID Oficina')
    id_ubicacion = fields.Char(string='Id Ubicacion')

    ubicacion_id = fields.Many2one(comodel_name='gps.ubicaciones', string='Location')

    codigo = fields.Integer(string='Codigo')
    nombre = fields.Char(string='Nombre')
    es_principal = fields.Boolean(string='Es Principal')

class GpsPersonas(models.Model):
    _name = 'gps.personas'
    _description = 'gps.personas'

    _rec_name = 'nombres'

    id_persona = fields.Char(string='ID Persona')
    id_oficina = fields.Char(string='Id Oficina')

    oficina_id = fields.Many2one(comodel_name='gps.oficinas', string='Office')

    nombres = fields.Char(string='Nombres')
    apellido_paterno = fields.Char(string='Apellido Paterno')
    apellido_materno = fields.Char(string='Apellido Materno')
    correo = fields.Char(string='Correo')
    telefono = fields.Char(string='Telegono')
    baja = fields.Boolean(string='baja')
    fecha_baja = fields.Date(string='Fecha Baja')
    comentarios_persona = fields.Char(string='Comentarios Persona')

class GpsPersonasEvento(models.Model):
    _name = 'gps.personas.evento'
    _description = 'gps.personas.evento'

    _rec_name = 'id_persona'

    id_persona_evento = fields.Char(string='ID Persona Evento')
    id_evento = fields.Char(string='Numero Trabajo')
    id_persona = fields.Char(string='Id Persona')

    evento_id = fields.Many2one(comodel_name='gps.eventos', string='Job Number')
    persona_id = fields.Many2one(comodel_name='gps.personas', string='Person')

    costo = fields.Float(string='Costo')
    tipo_moneda = fields.Char(string='Tipo Moneda')

class GpsProcesoGlobal(models.Model):
    _name = 'gps.proceso.global'
    _description = 'gps.proceso.global'

    _rec_name = 'nombre'

    id_proceso_global = fields.Char(string='ID Proceso Global')
    id_oficina = fields.Char(string='Id Oficina')

    oficina_id = fields.Many2one(comodel_name='gps.oficinas', string='Office')

    nombre = fields.Char(string='Nombre')
    fecha = fields.Date(string='Fecha')

class GpsRangoEstandaresCalidad(models.Model):
    _name = 'gps.rango.estandarescalidad'
    _description = 'gps.rango.estandarescalidad'

    _rec_name = 'cve_estandar'

    id_rango_estandares_calidad = fields.Char(string='ID Rango Estandares Calidad')
    cve_estandar = fields.Char(string='Cve Estandar')

    estandar_cve = fields.Many2one(comodel_name='gps.habilidades', string='Standard')

    rango_inicial = fields.Integer(string='Rango Inicial')
    rango_final = fields.Integer(string='Rango Final')
    descripcion = fields.Char(string='Descripcion')
    fecha_alta = fields.Date(string='Fecha Alta')
    fecha_baja = fields.Date(string='Fecha Baja')
    estatus = fields.Integer(string='Estatus')

class GpsRegistro(models.Model):
    _name = 'gps.registro'
    _description = 'gps.registro'

    _rec_name = 'fecha_reg'

    id_registro = fields.Char(string='ID Registro')
    id_usuario = fields.Char(string='Id Usuario')
    id_concepto = fields.Char(string='Id Concepto')
    id_cliente = fields.Char(string='Id Cliente')

    usuario_id = fields.Many2one(comodel_name='res.users', string='User')
    concepto_id = fields.Many2one(comodel_name='gps.concepto', string='Concept')
    cliente_id = fields.Many2one(comodel_name='res.partner', string='Client')

    fecha_reg = fields.Date(string='Fecha Reg')
    horas = fields.Float(string='Horas')
    certificacion = fields.Char(string='Certificacion')
    curso = fields.Char(string='Curso')
    observacion = fields.Char(string='Observacion')
    id_permiso = fields.Char(string='Id Permiso')

class GpsConcepto(models.Model):
    _name = 'gps.concepto'
    _description = 'gps.concepto'

    _rec_name = 'concepto'

    id_concepto = fields.Char(string='ID Concepto')

    concepto = fields.Char(string='Concepto')

class GpsTipoArchivo(models.Model):
    _name = 'gps.tipoarchivo'
    _description = 'gps.tipoarchivo'

    _rec_name = 'tipo_archivo'

    id_tipo_archivo = fields.Char(string='ID Tipo Archivo')

    tipo_archivo = fields.Char(string='Tipo Archivo')
    modulo = fields.Integer(string='Modulo')
    abrev = fields.Char(string='Abrev')

class GpsUbicaciones(models.Model):
    _name = 'gps.ubicaciones'
    _description = 'gps.ubicaciones'

    id_ubicacion = fields.Char(string='Id Ubicacion')
    id_ciudad = fields.Char(string='Id Ciudad')

    ciudad_id = fields.Many2one(comodel_name='gps.city', string='City')
    direccion = fields.Char(string='Direccion')

    @api.multi
    @api.depends('ciudad_id')
    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, 'ID: ' + str(record.id)))
        return result

class GpsUbicacionesCliente(models.Model):
    _name = 'gps.ubicaciones.cliente'
    _description = 'gps.ubicaciones.cliente'

    _rec_name = 'descripcion'

    id_ubicaciones_cliente = fields.Char(string='ID Ubicaciones Cliente')
    id_cliente = fields.Char(string='Id Cliente')
    id_ubicacion = fields.Char(string='Id Ubicacion')

    cliente_id = fields.Many2one(comodel_name='res.partner', string='Client')
    ubicacion_id = fields.Many2one(comodel_name='gps.ubicaciones', string='Location')
    descripcion = fields.Char(string='Descripcion')
    location = fields.Integer(string='Location')

class GpsUbicacionesContrato(models.Model):
    _name = 'gps.ubicaciones.contrato'
    _description = 'gps.ubicaciones.contrato'

    _rec_name = 'id_ubicacion'

    id_ubicaciones_contrato = fields.Char(string='ID Ubicaciones Contrato')
    id_contrato = fields.Char(string='Id Contrato')
    id_ubicacion = fields.Char(string='Id Ubicacion')

    contrato_id = fields.Many2one(comodel_name='gps.contratos', string='Agreement')
    ubicacion_id = fields.Many2one(comodel_name='gps.ubicaciones', string='Location')
    location = fields.Char(string='Location')

class GpsUsuariosPassword(models.Model):
    _name = 'gps.usuarios.password'
    _description = 'gps.usuarios.password'

    _rec_name = 'id_usuario'

    id_usuario_password = fields.Char(string='ID Usuario Password')
    id_usuario = fields.Char(string='Id Usuario')

    usuario_id = fields.Many2one(comodel_name='res.users', string='User')
    password_actualizado = fields.Char(string='Password Actualizado')

class GpsUsuariosEvento(models.Model):
    _name = 'gps.usuarios.evento'
    _description = 'gps.usuarios.evento'

    _rec_name = 'id_numero_trabajo'

    id_usuarios_evento = fields.Char(string='Id Usuarios Evento')
    id_numero_trabajo = fields.Char(string='Id Numero Trabajo')
    id_usuario = fields.Char(string='Id Usuario')

    numero_trabajo_id = fields.Many2one(comodel_name='gps.eventos', string='Job Number')
    usuario_id = fields.Many2one(comodel_name='res.users', string='User')
    lider = fields.Boolean(string='Lider')
    traductor = fields.Boolean(string='Traductor')

class GpsUsuariosFoto(models.Model):
    _name = 'gps.usuarios.foto'
    _description = 'gps.usuarios.foto'

    _rec_name = 'nombre_archivo'

    id_usuarios_foto = fields.Char(string='ID Usuarios Foto')
    id_usuario = fields.Char(string='Id Usuario')

    usuario_id = fields.Many2one(comodel_name='res.users', string='User')

    nombre_archivo = fields.Char(string='Nombre Archivo')

class GpsCiudades(models.Model):
    _name = 'gps.city'
    _description = 'gps.city'

    _rec_name = 'nombre'

    id_ciudad = fields.Char(string='ID Ciudad')
    id_estado = fields.Char(string="Id Estado")

    nombre = fields.Char(string='Nombre')
    no_estado = fields.Integer(string='NoEstado')
    estado = fields.Char(string='Estado')

class GpsConsultores(models.Model):
    _name = 'gps.consultores'
    _description = 'gps.consultores'

    _rec_name = 'nombre'

    id_consultor = fields.Char(string='ID Consultor')
    id_usuario = fields.Char(string='Id Usuario')

    usuario_id = fields.Many2one(comodel_name='res.users', string='User')

    nombre = fields.Char(string='Nombre')
    consultoria = fields.Char(string='Consultoria')
    telefono = fields.Char(string='Telefono')
    correo = fields.Char(string='Correo')
