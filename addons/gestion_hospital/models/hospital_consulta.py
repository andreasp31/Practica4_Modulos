# -*- coding: utf-8 -*-
from odoo import models, fields, api

#Definimos modelo hospital consulta
class HospitalConsulta(models.Model):

    #Nombre y descripcion del modelo
    _name = 'hospital.consulta'
    #Hereda de "base.archive"
    _inherit = ['base.archive']
    _description = 'Consultas del hospital'

    #ATRIBUTOS
    id_medico = fields.Many2one('hospital.medico',string='Medico',required=True)
    id_paciente = fields.Many2one('hospital.paciente',string='Paciente',required=True)
    nombre_medico = fields.Char(string='Medico',related='id_medico.nombre',store=True)
    nombre_paciente = fields.Char(string='Paciente',related='id_paciente.nombre',store=True)

    sintoma = fields.Text(string='Sintomas',required=True)
    fecha = fields.Datetime(string='Fecha de la consulta',default=fields.Datetime.now,required=True)

    _rec_name = 'nombre_medico' 