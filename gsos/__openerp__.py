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
        'data/audit_report_noconformance_sequence.xml',
        'data/audit_report_question_sequence.xml',
        'data/audit_request_sequence.xml',
        'data/complaint_sequence.xml',
        'views/gsos_menu.xml',
        'views/supplier_profile_view_form.xml',
        'views/supplier_profile_view_tree.xml',
        'views/supplier_profile_product_view_tree.xml',
        'views/supplier_profile_contact_view_tree.xml',
        'views/supplier_profile_raw_material_view_tree.xml',
        'views/complaint_view_form.xml',
        'views/complaint_view_tree.xml',
        'views/complaint_view_graph.xml',
        'views/complaint_view_pivot.xml',
        'views/checklist_view_form.xml',
        'views/checklist_view_tree.xml',
        'views/audit_view_form.xml',
        'views/audit_view_tree.xml',
        'views/audit_view_calendar.xml',
        'views/audit_report_section_view_form.xml',
        'views/audit_report_section_view_tree.xml',
        'views/audit_report_section_view_graph.xml',
        'views/audit_report_section_view_pivot.xml',
        'views/audit_report_question_view_tree.xml',
        'views/audit_report_noconformance_view_form.xml',
        'views/audit_report_noconformance_view_tree.xml',
        'views/audit_final_report.xml',
        'views/configuration_view_form.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True
}
