from odoo import models, fields, api

class CicloFormativo(models.Model):
    _name = 'colegio.ciclo'
    _description = 'Ciclo Formativo'

    nombre = fields.Char(string='Nombre del ciclo',required=True)
    codigo_ciclo = fields.Char(string='Código',required=True)
    descripcion = fields.Html(string='Descripción')
    id_modulos = fields.One2many('colegio.modulo','id_ciclo',string='Módulos')