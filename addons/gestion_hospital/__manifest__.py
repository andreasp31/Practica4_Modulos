# -*- coding: utf-8 -*-
{
    'name': "Módulo Hospital",
    'summary': """Gestión de un Hospital""",
    'description': """Gestión de pacientes, medicos y consultas""",
    'author': "Andrea Sofía Pais Dos Santos",
    'application': True,
    'category': 'Productivity',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'views/hospital_medico.xml', # ponemos las nuevas vistas que vamos creando
        'views/hospital_paciente.xml', # y ahora la vista del modelo medico
        'views/hospital_consulta.xml', # y por ultimo la vista de las consultas
        'views/hospital_menu.xml', # un nuevo archivo del menu porque me daba error al crearlo desde la visa paciente
        'security/ir.model.access.csv',
        'security/groups.xml',
    ],
}