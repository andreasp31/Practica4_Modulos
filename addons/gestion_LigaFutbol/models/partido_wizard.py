# -*- coding: utf-8 -*-
from odoo import models, fields

class PartidoWizard(models.TransientModel):
    #Nombre de la tabla temporal que se va a crear
    _name = 'liga.partido.wizard'
    _description = 'Wizard para crear partidos'
    #Campos del formulario 
    equipo_casa = fields.Many2one('liga.equipo', string="Equipo Local", required=True)
    equipo_fuera = fields.Many2one('liga.equipo', string="Equipo Visitante", required=True)
    goles_casa = fields.Integer(string="Goles Local", default=0)
    goles_fuera = fields.Integer(string="Goles Visitante", default=0)

    def crear_partido(self):
        # Esta función crea el registro permanente en el modelo liga.partido
        self.env['liga.partido'].create({
            'equipo_casa': self.equipo_casa.id,
            'equipo_fuera': self.equipo_fuera.id,
            'goles_casa': self.goles_casa,
            'goles_fuera': self.goles_fuera,
        })
        # Recalcular la clasificación tras añadir el partido nuevo
        self.env['liga.partido'].actualizarRegistrosEquipo()
        return {'type': 'ir.actions.act_window_close'} # Cierra la ventana emergente