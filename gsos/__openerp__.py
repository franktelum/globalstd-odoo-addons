# -*- coding: utf-8 -*-

{
    'name' : 'Gsos',
    'category': 'GlobalSTD',
    'version' : '1.0',
    'summary': 'Gestiona procesos de auditoría para segundas partes',
    'sequence': 30,
    'description': """
    Gestiona procesos de auditoría para segundas partes
    """,
    'category' : 'GlobalSTD',
    'website': 'https://www.globalstd.com',
    'images' : [],
    'depends' : ['mail'],
    'data': [
        'security/gsos_security.xml',
        'data/audit_request_sequence.xml',
        'data/complaint_sequence.xml',
        'views/gsos_menu.xml',
        'views/audit_view_tree.xml',
        'views/audit_view_form.xml',
        'views/audit_view_calendar.xml',
        'views/audit_view_graph.xml',
        'views/audit_report_section_view_tree.xml',
        'views/audit_report_section_view_graph.xml',
        'views/complaint_view_form.xml',
        'views/complaint_view_tree.xml',
        'views/complaint_view_graph.xml',
        'views/checklist_view_form.xml',
        'views/checklist_view_tree.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True
}
