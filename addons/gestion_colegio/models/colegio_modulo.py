from odoo import models, fields, api

class ColegioModulo(models.Model):
    _name = 'colegio.modulo'
    _description = 'Módulo'

    nombre = fields.Char(string='Nombre',required=True)
    codigo_modulo = fields.Char(string='Código',required=True)
    horas = fields.Integer(string='Horas')
    creditos = fields.Integer(string='Créditos')
    curso = fields.Selection([
        ('1',"Primero"),
        ('2','Segundo')
    ], string = 'Curso',required=True)
    # relaciones que se necesitan 
    id_ciclo = fields.Many2one('colegio.ciclo',string='Ciclo Formativo',required=True)
    id_profesor = fields.Many2one('colegio.profesor',string='Profesor que imparte')
    id_alumno = fields.Many2many('colegio.alumno',string='Alumnos matriculados')

    # restriccion del codigo unico
    _sql_constraints = [
        ('codigo_modulo_uniq','UNIQUE(codigo_modulo,id_ciclo)','El codigo del modulo debe de ser unico')
    ]