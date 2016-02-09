# -*- coding: utf-8 -*-

{
    'name' : 'GPSI',
    'version' : '1.0',
    'summary': 'Soporte para procesos internos de GlobalSTD',
    'sequence': 30,
    'description': """
    """,
    'category' : 'GlobalSTD',
    'website': 'https://www.globalstd.com',
    'images' : [],
    'depends' : ['mail'],
    'data': [
        'security/gpsi_security.xml',
        'views/gpsi_menu.xml',
        'views/gps_contratos_view_form.xml',
        'views/gps_contratos_view_tree.xml',
        'views/gps_contratos_search_form.xml',
        'views/gps_eventos_view_form.xml',
        'views/gps_eventos_view_tree.xml',
        'views/gps_eventos_view_calendar.xml',
        'views/gps_eventos_facturacion_view_tree.xml',
        'views/gps_misc_view_tree.xml',
        'views/gps_misc_view_form.xml',
        'data/gps_eventos_sequence.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True
}
