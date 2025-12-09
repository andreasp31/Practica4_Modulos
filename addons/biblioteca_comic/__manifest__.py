# -*- coding: utf-8 -*-
{
    'name': "Biblioteca comics",
    'summary': """Biblioteca de comics""",
    'description': """Gestión de ejemplares y socios""",
    'author': "Andrea Sofía Pais Dos Santos",
    'application': True,
    'category': 'Productivity',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/groups.xml',
        'views/biblioteca_socio.xml', # ponemos las nuevas vistas que vamos creando
        'views/biblioteca_prestamos.xml', # la nueva vista de los ejemplares y prestamos
        'views/biblioteca_comic_views.xml',
    ],
}