from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ColegioAlumno(models.Model):
    _name = 'colegio.alumno'
    _description = 'Alumno del colegio'

    nombre = fields.Char(string='Nombre',required=True)
    apellidos = fields.Char(string='Apellidos',required=True)
    dni = fields.Char(string='DNI del alumno/a',required=True)
    fecha_nacimiento = fields.Date(string='Fecha de nacimiento',required=True)
    telefono = fields.Char(string='Teléfono del familiar')
    fecha_matriculacion = fields.Date('Fecha de matriculación',default=fields.Date.today)
    # relaciones que se necesitan 
    id_ciclo = fields.Many2one('colegio.ciclo',string='Ciclo matriculado')
    id_modulo = fields.Many2many('colegio.modulo',string='Módulos matriculados')

    # restriccion del dni unico
    _sql_constraints = [
        ('dni_uniq', 'UNIQUE(dni)', 'El DNI ya existe')
    ]

    @api.constrains('dni')
    def _check_dni(self):
        for colegio_alumno in self:
            if colegio_alumno.dni and len(colegio_alumno.dni) != 9:
                raise ValidationError('El DNI debe tener 9 caracteres')