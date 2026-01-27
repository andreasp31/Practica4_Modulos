# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class LigaPartido(models.Model):
    #Nombre y descripcion del modelo
    _name = 'liga.partido'
    _description = 'Un partido de la liga'


    #Atributos del modelo


    #PARA CUANDO NO HAY UN ATRIBUTO LLAMADO NAME PARA MOSTRAR LOS Many2One en Vistas
    # https://www.odoo.com/es_ES/forum/ayuda-1/how-defined-display-name-in-custom-many2one-91657
    
   

    #Nombre del equipo que juega en casa casa
    equipo_casa = fields.Many2one(
        'liga.equipo',
        string='Equipo local',
    )
    #Goles equipo de casa
    goles_casa= fields.Integer()

    #Nombre del equipo que juega fuera
    equipo_fuera = fields.Many2one(
        'liga.equipo',
        string='Equipo visitante',
    )
    #Goles equipo de casa
    goles_fuera= fields.Integer()
    
    #Constraints de atributos
    @api.constrains('equipo_casa')
    def _check_mismo_equipo_casa(self):
        for record in self:
            if not record.equipo_casa:
                raise models.ValidationError('Debe seleccionarse un equipo local.')
            if record.equipo_casa == record.equipo_fuera:
                raise models.ValidationError('Los equipos del partido deben ser diferentes.')


     #Constraints de atributos
    @api.constrains('equipo_fuera')
    def _check_mismo_equipo_fuera(self):
        for record in self:
            if not record.equipo_fuera:
                raise models.ValidationError('Debe seleccionarse un equipo visitante.')
            if record.equipo_fuera and record.equipo_casa == record.equipo_fuera:
                raise models.ValidationError('Los equipos del partido deben ser diferentes.')

    '''
    Funcion para actualizar la clasificacion de los equipos, re-calculandola entera
    '''
    def actualizoRegistrosEquipo(self):
        #Recorremos partidos y equipos
        for recordEquipo in self.env['liga.equipo'].search([]):
            #Como recalculamos todo, ponemos de cada equipo todo a cero
            recordEquipo.victorias=0
            recordEquipo.empates=0
            recordEquipo.derrotas=0
            recordEquipo.goles_a_favor=0
            recordEquipo.goles_en_contra=0
            recordEquipo.puntos= 0
            
            for recordPartido in self.env['liga.partido'].search([]):  
        
                #Si es el equipo de CASA
                if recordPartido.equipo_casa.nombre == recordEquipo.nombre:
                    
                    #Miramos si es victoria o derrota
                    if recordPartido.goles_casa > recordPartido.goles_fuera:
                        recordEquipo.victorias=recordEquipo.victorias + 1
                        # Si los goles marcados por el equipo de casa es mas de 4 goles por encima del equipo visitante
                        if recordPartido.goles_casa - recordPartido.goles_fuera >= 4:
                            #Se suman los 4 puntos
                            recordEquipo.puntos = recordEquipo.puntos + 4
                        else:
                            #Si no hay esa diferencia se le suma al equipo de casa 3 puntos por victoria
                            recordEquipo.puntos = recordEquipo.puntos + 3
                    elif recordPartido.goles_casa < recordPartido.goles_fuera:
                        recordEquipo.derrotas = recordEquipo.derrotas + 1
                        #Si los goles marcados por el equipo de fuera es mas de 4 goles que el otro equipo, al equipo de casa
                        if recordPartido.goles_fuera - recordPartido.goles_casa >= 4:
                            #Se le resta 1 punto 
                            recordEquipo.puntos = recordEquipo.puntos - 1
                    else:
                        recordEquipo.empates = recordEquipo.empates + 1
                        #Un punto por empate 
                        recordEquipo.puntos = recordEquipo.puntos + 1
                        
                    #Sumamos goles a favor y en contra
                    recordEquipo.goles_a_favor = recordEquipo.goles_a_favor+recordPartido.goles_casa
                    recordEquipo.goles_en_contra = recordEquipo.goles_en_contra+recordPartido.goles_fuera

                #Si es el equipo de FUERA
                if recordPartido.equipo_fuera.nombre==recordEquipo.nombre:
                
                    #Miramos si es victoria o derrota
                    if recordPartido.goles_casa < recordPartido.goles_fuera:
                        recordEquipo.victorias = recordEquipo.victorias + 1
                        # Si los goles marcados por el equipo de fuera es mas de 4 goles por encima del equipo en casa
                        if recordPartido.goles_fuera - recordPartido.goles_casa >= 4:
                            #Se suman los 4 puntos
                            recordEquipo.puntos = recordEquipo.puntos + 4
                        else:
                            #Si no hay esa diferencia se le suma al equipo de casa 3 puntos por victoria
                            recordEquipo.puntos = recordEquipo.puntos + 3
                    elif recordPartido.goles_casa > recordPartido.goles_fuera:
                        recordEquipo.derrotas = recordEquipo.derrotas + 1
                        # Si los goles marcados por el equipo de casa es mas de 4 goles por encima del equipo de fuera
                        if recordPartido.goles_casa - recordPartido.goles_fuera >= 4:
                            # Se le resta 1 punto
                            recordEquipo.puntos = recordEquipo.puntos - 1 
                    else:
                        recordEquipo.empates = recordEquipo.empates + 1
                        #Uno por empate
                        recordEquipo.puntos = recordEquipo.puntos + 1
                    
                    #Sumamos goles a favor y en contra
                    recordEquipo.goles_a_favor = recordEquipo.goles_a_favor + recordPartido.goles_fuera
                    recordEquipo.goles_en_contra = recordEquipo.goles_en_contra + recordPartido.goles_casa

    # Sumar los 2 goles a los equipos locales
    def sumar_goles_locales(self):
        #Buscar todos los partidos
        partidos = self.search([])
        for partido in partidos:
            partido.goles_casa += 2
        self.actualizoRegistrosEquipo()
        return True
    
    # Sumar los 2 goles a los equipos visitantes
    def sumar_goles_visitantes(self):
        #Buscar todos los partidos
        partidos = self.search([])
        for partido in partidos:
            partido.goles_fuera += 2
        self.actualizoRegistrosEquipo()
        return True

    #Sobrescribo el borrado (unlink)
    def unlink(self):
        #Borro el registro, que es lo que hace el metodo normalmente
        result=super(LigaPartido,self).unlink()
        #Añado que llame a actualizoRegistroEquipo()
        self.env['liga.partido'].actualizoRegistrosEquipo()
        return result

    #Sobreescribo el metodo crear
    @api.model
    def create(self, values):
        #hago lo normal del metodo create
        result = super().create(values)
        #Añado esto: llamo a la funcion que actualiza la clasificacion
        self.actualizoRegistrosEquipo()
        #hago lo normal del metodo create
        return result
    
    # Se sobrescribe el método write de Odoo, los partidos que se están modificando
    def write(self, values):
        # Guarda los cambios en la base de datos y actualizar le partido
        result = super(LigaPartido, self).write(values)
        # Recalcula todo y así queda actualizada 
        self.actualizoRegistrosEquipo()
        return result
