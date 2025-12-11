# -*- coding: utf-8 -*-
{
    'name': "Gestión del Colegio Princesa de España",
    'summary': """Gestión de ciclos formativos, módulos, alumnos y profesores""",
    'description': """Módulo para la gestión completa de un instituto educativo:""",
    'author': "Andrea Sofía Pais Dos Santos",
    'application': True,
    'category': 'Education',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        # primero seguridad, luego vistas, luego menús
        'security/group.xml',
        'security/ir.model.access.csv',
        
        # Vistas en orden alfabético para claridad
        'views/colegio_ciclo.xml',
        'views/colegio_modulo.xml',
        'views/colegio_alumno.xml',
        'views/colegio_profesor.xml',
        
        # Menús al final
        'views/colegio_menu.xml',
    ],
}