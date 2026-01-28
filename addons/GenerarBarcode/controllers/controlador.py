# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import io
import random

# Intentar importar Pillow de forma segura
try:
    from PIL import Image
except ImportError:
    Image = None

class ImagenAleatoriaController(http.Controller):

    @http.route('/generar_imagen_aleatoria', type='http', auth='public', website=True)
    def crear_imagen(self, w=200, h=200, **kwargs):
        # Si Pillow no está, se devuelve texto para no dar Error 500
        if Image is None:
            return "Error: La libreria Pillow no esta instalada en el contenedor Odoo."

        try:
            ancho = int(w)
            alto = int(h)
        except:
            ancho, alto = 200, 200

        # Crear la imagen aleatoria
        img = Image.new('RGB', (ancho, alto))
        pixeles = img.load()
        for x in range(ancho):
            for y in range(alto):
                pixeles[x, y] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Guardar imagen en buffer
        output = io.BytesIO()
        img.save(output, format="PNG")
        contenido = output.getvalue()
        output.close()

        # Retornar respuesta simple para evitar descargas
        return request.make_response(contenido, [
            ('Content-Type', 'image/png'),
            ('Content-Disposition', 'inline')
        ])