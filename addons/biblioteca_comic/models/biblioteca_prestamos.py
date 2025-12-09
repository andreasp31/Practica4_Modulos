# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import timedelta
from odoo.exceptions import ValidationError

#Definir Modelo Biblioteca comic
class BibliotecaPrestamos(models.Model):

    #Nombre y descripcion del modelo
    _name = 'biblioteca.prestamos'
    _description = 'Ejempleares de los prestamos'

    ejemplar_id = fields.Many2one('biblioteca.comic',string='Comic',required=True)
    codigo = fields.Char('Ejemplar código',required=True)

    estado = fields.Selection(
        [('prestado', 'No disponible'),
         ('disponible', 'Disponible'),
         ('perdido', 'Perdido')],
        string='Estado', default="disponible")

    id_socio = fields.Many2one('biblioteca.socio', string='Socio', required=True)

    fecha_inicio = fields.Date(string='Fecha de inicio del prestamo')
    fecha_final = fields.Date(string='Fecha de final del prestamo')

    _rec_name = 'codigo'

    @api.constrains('fecha_inicio')
    def _check_release_inicio(self):
        for record in self:
            #Comprobar de cada registro haya una fecha de inicio y que la fecha no sea posterior a la actual.
            if record.fecha_inicio and record.fecha_inicio > fields.Date.today():
    
                raise models.ValidationError('La fecha de inicio del préstamo debe ser anterior a la actual')
    
    @api.constrains('fecha_final')
    def _check_release_final(self):
        for record in self:
            #Comprobar de cada registo haya una fecha final y que la fecha tiene que ser posterior a la fecha actual.
            if record.fecha_final and record.fecha_final < fields.Date.today():
                #Si procede, lanzamos una excepcion
                raise models.ValidationError('La fecha de final del préstamo debe ser posterior a la actual')

