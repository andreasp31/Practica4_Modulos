from odoo import models, fields, api
#Definimos el modelo de datos
class lista_tareas(models.Model):
#Nombre y descripcion del modelo de datos
    _name = 'lista_tareas.lista_tareas'
    _description = 'lista_tareas.lista_tareas'
    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son
    tarea = fields.Char(string="Tarea")
    prioridad = fields.Integer(string="Prioridad")
    urgente = fields.Boolean(compute="_value_urgente", store=True)
    realizada = fields.Boolean(string="Realizada")
    categoria = fields.Selection([
        ("estudio","Estudio"),
        ("trabajo","Trabajo"),
        ("ocio","Ocio"),
        ("cita","Citas")
    ],string="Categoría",default="cita")
    @api.depends('prioridad')
    def _value_urgente(self):
    #Para cada registro
        for record in self:
        #Si la prioridad es mayor que 10, se considera urgente, en otro caso no lo es
            if record.prioridad>10:
                record.urgente = True
            else:
                record.urgente = False