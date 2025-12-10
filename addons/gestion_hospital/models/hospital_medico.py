# -*- coding: utf-8 -*-
from odoo import models, fields, api

#Definimos modelo Biblioteca socio
class HospitalMedico(models.Model):

    #Nombre y descripcion del modelo
    _name = 'hospital.medico'
    #Hereda de "base.archive"
    _inherit = ['base.archive']
    _description = 'Medicos del hospital'

    #ATRIBUTOS

    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos',required=True)
    num_colegiado = fields.Char('Numero colegiado',required=True)
    #Indicamos que atributo sera el que se usara para mostrar nombre.
    #Aqui indicamos que se use el atributo "nombre"
    _rec_name = 'nombre'
  
    _sql_constraints = [
        ('num_colegiado_uniq','UNIQUE(num_colegiado)','El identificador ya existe')
    ]