# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

#Clase del controlador web
class Main(http.Controller):
    #Decorador que indica que la url "/ligafutbol/equipo/json" atendera por HTTP, sin autentificacion
    #Devolvera texto que estará en formato JSON
    #Se puede probar accediendo a http://localhost:8069/ligafutbol/equipo/json
    @http.route('/ligafutbol/equipo/json', type='http', auth='none')
    def obtenerDatosEquiposJSON(self):
        #Obtenemos la referencia al modelo de Equipo
        equipos = request.env['liga.equipo'].sudo().search([])
        
        #Generamos una lista con informacion que queremos sacar en JSON
        listaDatosEquipos=[]
        for equipo in equipos:
             listaDatosEquipos.append([equipo.nombre,str(equipo.fecha_fundacion),equipo.jugados,equipo.puntos,equipo.victorias,equipo.empates,equipo.derrotas])
        #Convertimos la lista generada a JSON
        json_result=json.dumps(listaDatosEquipos)

        return json_result

    #Al acceder a http://localhost:8069/eliminarempates borra los partidos empatados
    @http.route("/eliminarempates",type="http",auth="public", website=True)
    def eliminar_empates(self,**kw):
        #Buscamos los partidos
        partidos = request.env["liga.partido"].sudo().search([])
        #Empezamos un contador
        contador = 0
        #Buscamos que partidos tiene los goles iguales
        for partido in partidos:
            if partido.goles_casa == partido.goles_fuera:
                #Borrar los registros
                partido.unlink()
                #Vamos sumando los partidos empatados borrados
                contador += 1
        request.env["liga.partido"].sudo().actualizoRegistrosEquipo()
        #Nos devuelve unos textos que nos dice cuantos partidos se borrar con empates
        return "<h1>Operación realizada</h1><p>Se han borrado un total de partidos con empate: %s</p>" % contador