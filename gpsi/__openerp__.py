{
    'name': 'GlobalSTD',
    'version': '1.0',
    'summary': 'Gestiona procesos de GlobalSTD',
    'description': 'Gestiona procesos de GlobalSTD',
    'application': True,
    'depends': ['mail'],
    'data': [
        'views/gpsi_menu.xml',
        'views/audit_event_view_form.xml',
        'views/audit_event_view_tree.xml',
        'views/audit_event_view_calendar.xml',
        'views/audit_event_view_search.xml',
        'views/audit_standard_view_form.xml',
        'views/audit_iaf_view_form.xml',
        'views/audit_nace_code_view_form.xml',
        'views/contract_view_form.xml',
        'views/contract_view_tree.xml',
        'views/partner_view_form.xml',
        'views/product_view_form.xml',
        'data/contract_sequence.xml',
        'data/quotation_sequence.xml',
        'data/audit_event_sequence.xml'
    ]
}
