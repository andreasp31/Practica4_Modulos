# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError


# Modelo base, creado como modelo abstracto 
# Este modelo lo heredarara el modelo HospitalPaciente
# Y se ha creado puramente con fin didáctico para ver herencia entre modelos
class BaseArchive(models.AbstractModel):
    #Nombre y descripcion del modelo
    _name = 'base.archive'
    _inherit = ['base.archive']
    _description = 'Fichero abstracto'

    #Introduce el atributo "Activo"
    activo = fields.Boolean(default=True)

    #Introducice metodo "archivar" que invierte el estado de "activo"
    #Recordamos se recive "self" como el modelo entero y no como un registro,
    #por ese motivo debemos iterar
    def archivar(self):
        #Por cada registro del modelo
        for record in self:
            #Cambiamos el valor de activo a su version negada
            record.activo = not record.activo


#Definir Modelo Biblioteca comic
class HospitalPaciente(models.Model):

    #Nombre y descripcion del modelo
    _name = 'hospital.paciente'
    #Hereda de "base.archive"
    _inherit = ['base.archive']

    _description = 'Paciente del Hospital'

    #ATRIBUTOS
    
    #Indicamos que atributo sera el que se usara para mostrar nombre.
    #Por defecto es "name", pero si no hay un atributo que se llama name, aqui lo indicamos
    #Aqui indicamos que se use el atributo "nombre"
    _rec_name = 'nombre'
    #Atributo nombre
    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Html('Apellidos', required=True)
    sintomas = fields.Html('Sintomas', required=True)
   