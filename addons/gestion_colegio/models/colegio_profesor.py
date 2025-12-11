from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ColegioProfesor(models.Model):
    _name = 'colegio.profesor'
    _description = 'Profesor del colegio'

    nombre = fields.Char(string='Nombre',required=True)
    apellidos = fields.Char(string='Apellidos',required=True)
    dni = fields.Char(string='DNI del profesor/a',required=True)
    email = fields.Char(string='Email del colegio',required=True)
    telefono = fields.Char(string='Teléfono')
    fecha_contratacion = fields.Date('Fecha de contratación',default=fields.Date.today)
    # relaciones que se necesitan 
    id_modulo = fields.One2many('colegio.modulo','id_profesor',string='Módulos que imparte')

    # restriccion del dni unico
    _sql_constraints = [
        ('dni_uniq', 'UNIQUE(dni)', 'El DNI ya existe'),
        ('email_uniq','UNIQUE(email)','El email ya existe')
    ]

    @api.constrains('dni')
    def _check_dni(self):
        for colegio_alumno in self:
            if colegio_alumno.dni and len(colegio_alumno.dni) != 9:
                raise ValidationError('El DNI debe tener 9 caracteres')