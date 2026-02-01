import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters

# configuración
TOKEN = '8015889789:AAFCr7XlIZwv2hPzWNobqKH8ScA10LdoQh4'
URL = 'http://localhost:8069/gestion/apirest/socio'

async def manejar_mensaje(update: Update, context):
    # Cogemos el texto y lo separamos por comas (la orden, nombre, apellidos, número)
    texto = update.message.text
    partes = [parte.strip() for parte in texto.split(',')]
    orden = partes[0] # esta es la orden

    try:
        # si la orden es igual a crear
        if orden == "Crear":
            # pasamos los datos (nombre, apellidos, numero socio)
            datos = {"nombre": partes[1], "apellidos": partes[2], "num_socio": partes[3]}
            # Envia la información a la url
            r = requests.post(URL, json=datos)
            # Nos devuelve el contenido del mensaje, el f"" se usa para crear frase combinando texto normal con variables
            respuesta = f"Socio creado: {r.text}"

        # si la orden es igual a consultar
        elif orden == "Consultar":
            # los datos ( orden y el número de socio)
            params = {"data": '{"num_socio": "' + partes[1] + '"}'}
            # Envia la información a la url
            r = requests.get(URL, params=params)
            # Nos devuelve el contenido del mensaje
            respuesta = f"Datos: {r.text}"

        # si la orden es igual a borrar
        elif orden == "Borrar":
            # datos (orden y número de socio)
            params = {"data": '{"num_socio": "' + partes[1] + '"}'}
            # Envia la información a la url
            r = requests.delete(URL, params=params)
            # Nos devuelve el contenido del mensaje
            respuesta = f"Borrado: {r.text}"
        # si la orden es igual a modificar
        elif orden == "Modificar":
            # datos(orden,nombre,apellidos,número de socio)
            datos = {"nombre": partes[1], "apellidos": partes[2], "num_socio": partes[3]}
            # Envia la información a la url
            r = requests.put(URL, json=datos)
            # Nos devuelve el contenido del mensaje
            respuesta = f"Socio modificado: {r.text}"
        else:
            # Si no es ninguna de las ordenes devuelve el mensaje
            respuesta = "Orden no soportada"

    except Exception as error:
        respuesta = f"Error, igual faltan comas ({error})"

    # ordena al bor enviar un mensake de vuelta al chat de telegram
    await update.message.reply_text(respuesta)

# arrancar Bot, usa el token para conectarse al servidor de telegram
app = ApplicationBuilder().token(TOKEN).build()
# tiene que estar atento a los mensajes y que solo quiere texto y llamamos a la función
app.add_handler(MessageHandler(filters.TEXT, manejar_mensaje))
print("Bot funcionando...")
# el bot se queda escuchando constantemente
app.run_polling()