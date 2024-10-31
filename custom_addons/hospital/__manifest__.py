{
    'name': 'Hospital Management System',
    'version': '1.0',
    'summary': 'Just a simple Hospital Management System',
    'sequence': 1,
    'description': 'A simple hospital management system for Odoo',
    'author': 'Andrew Antwi',
    'website': 'https://www.hospital_management.com',
    'category': 'Healthcare',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/patient_readonly_views.xml',
        'views/patient_views.xml',
        'views/patient_tag_views.xml',
        'views/appointment_views.xml',
        'views/menu.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': True,  # Change to False unless this should auto-install with dependencies
}
