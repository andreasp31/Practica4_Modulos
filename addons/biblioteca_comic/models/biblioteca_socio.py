# -*- coding: utf-8 -*-
from odoo import models, fields, api

#Definimos modelo Biblioteca socio
class BibliotecaComic(models.Model):

    #Nombre y descripcion del modelo
    _name = 'biblioteca.socio'
    #Hereda de "base.archive"
    _inherit = ['base.archive']
    _description = 'Socios de la biblioteca'

    #ATRIBUTOS

    nombre = fields.Char('Nombre', required=True)
    apellido = fields.Char('Apellido',required=True)
    identificacion = fields.Char('Identificador',required=True)
    #Indicamos que atributo sera el que se usara para mostrar nombre.
    #Aqui indicamos que se use el atributo "nombre"
    _rec_name = 'nombre'
  
    _sql_constraints = [
        ('identificacion_uniq','UNIQUE(identificacion)','El identificador ya existe')
    ]