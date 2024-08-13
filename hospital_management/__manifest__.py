# -*- coding: utf-8 -*-
{
    'name': "hospital_management",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'installable': True,
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/access_doc.xml',
        'views/patient_views.xml',
        'views/family_views.xml',
        'views/doctor_views.xml',
        'views/appointment_patient_views.xml',
        'views/appointment_surgery_views.xml',
        'views/nurse_views.xml',
        'views/room_views.xml',
        'views/lab_test_views.xml',
        'views/patient_test_views.xml',
        'views/pharmacy_views.xml',
        'views/vaccine_views.xml',
        'views/vaccination_views.xml',
        'views/director_views.xml',
        'views/reception_views.xml',
        'views/labs_views.xml',
        'views/blood_bank_views.xml',
        'views/analysis_views.xml',
        'views/analysis_answer_views.xml',
        'views/doctor_templates.xml',
        'views/pharmacy_template.xml',
        'views/rooms_template.xml',
        'views/nurse_template.xml',
        'views/appointment_template.xml',
        'views/blood_template.xml',
        'views/vaccine_template.xml',
        'views/patients_templates.xml',
        'views/lab_template.xml',
        'views/vaccination_appointment_template.xml',
        'views/analysis_template.xml',
        'views/analysis_answer_template.xml',
        'views/patient_analysis_template.xml',
        'views/patients_info_template.xml'

    ]
}

