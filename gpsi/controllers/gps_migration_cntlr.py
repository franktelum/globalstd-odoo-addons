# -*- coding: utf-8 -*-

import json
import logging
import werkzeug

from openerp import http
from openerp.http import request

_logger = logging.getLogger(__name__)

class GpsMigrationCntlr(http.Controller):
    @http.route(route="/gps/migration/fix_imports", auth="user", methods=['GET'])
    def fix_imports(self, **kw):
        # gps.habilidades
        habilidades = request.env['gps.habilidades'].search([])
        for habilidad in habilidades:
            padres = request.env['gps.habilidades'].search([('id_habilidad', '=', habilidad.id_padre)])
            habilidad.padre_id = padres and padres[0].id or False

        # gps.nacecode
        nacecodes = request.env['gps.nacecode'].search([])
        for nacecode in nacecodes:
            habilidades = request.env['gps.habilidades'].search([('id_habilidad', '=', nacecode.id_habilidad)])
            nacecode.habilidad_id = habilidades and habilidades[0].id or False

        # gps.contratos
        contratos = request.env['gps.contratos'].search([])
        for contrato in contratos:
            habilidades = request.env['gps.habilidades'].search([('id_habilidad', '=', contrato.id_habilidad)])
            contrato.habilidad_id = habilidades and habilidades[0].id or False

            clientes = request.env['res.partner'].search([('gpsi_id_cliente', '=', contrato.id_cliente)])
            contrato.cliente_id = clientes and clientes[0].id or False

            users = request.env['res.users'].search([('gpsi_id_user', '=', contrato.id_ventas)])
            contrato.ventas_id = users and users[0].id or False

            users = request.env['res.users'].search([('gpsi_id_user', '=', contrato.id_revisor)])
            contrato.revisor_id = users and users[0].id or False

            if contrato.id_archivo_contrato:
                contrato.archivo_contrato_id = request.env['ir.attachment'].create({
                    'res_model': 'gps.contratos',
                    'res_id': contrato.id,
                    'name': '%s' % (contrato.id_archivo_contrato or 'Sales Package'),
                    'type': 'url',
                    'url': 'http://gps.globalstd.com/documentos/%s/%s' % (contrato.no_contrato or '', contrato.id_archivo_contrato or '')})

            if contrato.id_archivo_rev_auditor:
                contrato.archivo_rev_auditor_id = request.env['ir.attachment'].create({
                    'res_model': 'gps.contratos',
                    'res_id': contrato.id,
                    'name': '%s' % (contrato.id_archivo_rev_auditor or 'Audit Review'),
                    'type': 'url',
                    'url': 'http://gps.globalstd.com/documentos/%s/%s' % (contrato.no_contrato or '', contrato.id_archivo_rev_auditor or '')})

            if contrato.id_archivo_certificado:
                contrato.archivo_certificado_id = request.env['ir.attachment'].create({
                    'res_model': 'gps.contratos',
                    'res_id': contrato.id,
                    'name': '%s' % (contrato.id_archivo_certificado or 'Certificate File'),
                    'type': 'url',
                    'url': 'http://gps.globalstd.com/documentos/%s' % (contrato.id_archivo_certificado or '')})

            if contrato.moneda_tipo < 4:
                contrato.moneda_tipo = contrato.moneda_tipo + 1

        # gps.eventos
        eventos = request.env['gps.eventos'].search([])
        for evento in eventos:
            habilidades = request.env['gps.habilidades'].search([('id_habilidad', '=', evento.id_habilidad)])
            evento.habilidad_id = habilidades and habilidades[0].id or False

            contratos = request.env['gps.contratos'].search([('id_contrato', '=', evento.id_contrato)])
            evento.contrato_id = contratos and contratos[0].id or False

            clientes = request.env['res.partner'].search([('gpsi_id_cliente', '=', evento.id_cliente)])
            evento.cliente_id = clientes and clientes[0].id or False

            users = request.env['res.users'].search([('gpsi_id_user', '=', evento.id_revisor)])
            evento.revisor_id = users and users[0].id or False

            users = request.env['res.users'].search([('gpsi_id_user', '=', evento.id_comite)])
            evento.comite_id = users and users[0].id or False

            users = request.env['res.users'].search([('gpsi_id_user', '=', evento.id_client_service)])
            evento.client_service_id = users and users[0].id or False

            ubicaciones = request.env['gps.ubicaciones'].search([('id_ubicacion', '=', evento.id_ubicacion)])
            evento.ubicacion_id = ubicaciones and ubicaciones[0].id or False

            no_contrato = contratos and contratos[0].no_contrato or False
            if evento.id_archivo_plan_auditoria:
                evento.archivo_plan_auditoria_id = request.env['ir.attachment'].create({
                    'res_model': 'gps.eventos',
                    'res_id': evento.id,
                    'name': '%s' % (evento.id_archivo_plan_auditoria or 'Plan de Auditoría'),
                    'type': 'url',
                    'url': 'http://gps.globalstd.com/documentos/%s/%s/%s' % (no_contrato or '', evento.numero_trabajo or '', evento.id_archivo_plan_auditoria or '')})

            if evento.id_archivo_reporte_auditoria:
                evento.archivo_reporte_auditoria_id = request.env['ir.attachment'].create({
                    'res_model': 'gps.eventos',
                    'res_id': evento.id,
                    'name': '%s' % (evento.id_archivo_reporte_auditoria or 'Reporte de auditoría'),
                    'type': 'url',
                    'url': 'http://gps.globalstd.com/documentos/%s/%s/%s' % (no_contrato or '', evento.numero_trabajo or '', evento.id_archivo_reporte_auditoria or '')})

        # gps.archivos
        archivos = request.env['gps.archivos'].search([])
        for archivo in archivos:
            non_conformances = request.env['gps.noconformidades'].search([('id_noconformidad', '=', archivo.id_propietario)])
            archivo.propietario_id = non_conformances and non_conformances[0].id or False

        # gps.archivos.tracking
        archivos_tracking = request.env['gps.archivos.tracking'].search([])
        for archivo_tracking in archivos_tracking:
            eventos = request.env['gps.eventos'].search([('numero_trabajo', '=', archivo_tracking.id_numero_trabajo)])
            archivo_tracking.numero_trabajo_id = eventos and eventos[0].id or False

        # gps.archivos.evento
        archivos_evento = request.env['gps.archivos.evento'].search([])
        for archivo_evento in archivos_evento:
            eventos = request.env['gps.eventos'].search([('numero_trabajo', '=', archivo_evento.id_numero_trabajo)])
            archivo_evento.numero_trabajo_id = eventos and eventos[0].id or False

        # gps.archivos.historial
        archivos_historial = request.env['gps.archivos.historial'].search([])
        for archivo_historial in archivos_historial:
            eventos = request.env['gps.eventos'].search([('numero_trabajo', '=', archivo_historial.id_numero_trabajo)])
            archivo_historial.numero_trabajo_id = eventos and eventos[0].id or False

        # gps.noconformidades
        no_conformidades = request.env['gps.noconformidades'].search([])
        for no_conformidad in no_conformidades:
            eventos = request.env['gps.eventos'].search([('numero_trabajo', '=', no_conformidad.id_numero_trabajo)])
            no_conformidad.numero_trabajo_id = eventos and eventos[0].id or False

            clientes = request.env['res.partner'].search([('gpsi_id_cliente', '=', no_conformidad.id_cliente)])
            no_conformidad.cliente_id = clientes and clientes[0].id or False

        # gps.ubicaciones.cliente
        ubicaciones_cliente = request.env['gps.ubicaciones.cliente'].search([])
        for ubicacion_cliente in ubicaciones_cliente:
            clientes = request.env['res.partner'].search([('gpsi_id_cliente', '=', ubicacion_cliente.id_cliente)])
            ubicacion_cliente.cliente_id = clientes and clientes[0].id or False

            ubicaciones = request.env['gps.ubicaciones'].search([('id_ubicacion', '=', ubicacion_cliente.id_ubicacion)])
            ubicacion_cliente.ubicacion_id = ubicaciones and ubicaciones[0].id or False

        # gps.eventos.contrato
        eventos_contrato = request.env['gps.eventos.contrato'].search([])
        for evento_contrato in eventos_contrato:
            contratos = request.env['gps.contratos'].search([('id_contrato', '=', evento_contrato.id_contrato)])
            evento_contrato.contrato_id = contratos and contratos[0].id or False

            ubicaciones = request.env['gps.ubicaciones'].search([('id_ubicacion', '=', evento_contrato.id_ubicacion)])
            evento_contrato.ubicacion_id = ubicaciones and ubicaciones[0].id or False

        # gps.eventos.facturacion
        eventos_facturacion = request.env['gps.eventos.facturacion'].search([])
        for evento_facturacion in eventos_facturacion:
            eventos = request.env['gps.eventos'].search([('numero_trabajo', '=', evento_facturacion.id_numero_trabajo)])
            evento_facturacion.numero_trabajo_id = eventos and eventos[0].id or False

            users = request.env['res.users'].search([('gpsi_id_user', '=', evento_facturacion.id_usuario)])
            evento_facturacion.usuario_id = users and users[0].id or False

        # gps.usuarios.eventos
        usuarios_evento = request.env['gps.usuarios.evento'].search([])
        for usuario_evento in usuarios_evento:
            eventos = request.env['gps.eventos'].search([('numero_trabajo', '=', usuario_evento.id_numero_trabajo)])
            usuario_evento.numero_trabajo_id = eventos and eventos[0].id or False

            users = request.env['res.users'].search([('gpsi_id_user', '=', usuario_evento.id_usuario)])
            usuario_evento.usuario_id = users and users[0].id or False

        # gps.nacecodes.cliente
        nacecodes_cliente = request.env['gps.nacecodes.cliente'].search([])
        for nacecode_cliente in nacecodes_cliente:
            nacecodes = request.env['gps.nacecode'].search([('id_nacecode', '=', nacecode_cliente.id_nacecode)])
            nacecode_cliente.nacecode_id = nacecodes and nacecodes[0].id or False

            clientes = request.env['res.partner'].search([('gpsi_id_cliente', '=', nacecode_cliente.id_cliente)])
            nacecode_cliente.cliente_id = clientes and clientes[0].id or False

        # res.partner
        clientes = request.env['res.partner'].search([])
        for cliente in clientes:
            ubicaciones_cliente = request.env['gps.ubicaciones.cliente'].search([('cliente_id', '=', cliente.id)])
            ubicaciones = []
            for ubicacion_cliente in ubicaciones_cliente:
                ubicaciones.append(ubicacion_cliente.ubicacion_id.id)
            cliente.gpsi_ubicaciones_cliente_ids = [(6, 0, ubicaciones)]

            nacecodes_cliente = request.env['gps.nacecodes.cliente'].search([('cliente_id', '=', cliente.id)])
            nacecodes = []
            for nacecode_cliente in nacecodes_cliente:
                nacecodes.append(nacecode_cliente.nacecode_id.id)
            cliente.gpsi_nacecode_cliente_ids = [(6, 0, nacecodes)]

        return "Done!!"

    @http.route(route="/gps/migration/clients/new", type="json", auth="none", methods=['POST'])
    def create_client(self, **args):
        newRecord = {
            'company_type': 'company',
            'customer': True,
            'gpsi_id_oficina': args['IdOficina'],
            'gpsi_cve_cliente': args['ClaveCliente'],
            'name': args['NombreCliente'],
            'street': args['Domicilio'],
            'phone': args['Telefonos'],
            'email': args['Correos'],
            'gpsi_rfc': args['Rfc'],
            'gpsi_domicilio_fiscal': args['DomicilioFiscal'],
            'city': args['Ciudad'],
            'zip': args['CP'],
            'website': args['SitioWeb'],
            'gpsi_no_empleados': args['NoEmpleados'],
            'gpsi_id_referencia': args['IdReferencia'],
            'active': args['Baja'],
            'gpsi_id_cliente': args['IdCliente'],
            'gpsi_perfil': args['Perfil'],
            'gpsi_archivo_perfil': args['archivoPerfil'],
            'gpsi_nick_name': args['NickName'],
            'gpsi_password': args['Password'],
            'gpsi_id_md5_qms': args['IdMD5QMS'],
            'gpsi_id_ref_prog': args['IdRefProg'],
            'gpsi_recommended': args['Recommended'],
            'gpsi_id_leader_sales': args['IdLeaderSales'],
            'gpsi_id_fuente': args['IdFuente']
        }
        request.env['res.partner'].sudo().create(newRecord)
        return 'Done'

    @http.route(route="/gps/migration/clients/update", type="json", auth="none", methods=['POST'])
    def update_client(self, **args):
        if 'name' not in args:
            return {'error': 'empty_name'}
        return args['name']
