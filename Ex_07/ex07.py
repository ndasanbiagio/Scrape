from flask import Flask, jsonify


from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
  url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
  content = requests.get(url).text
  soup = BeautifulSoup(content, 'html.parser')
  rate = soup.find("span", class_="ccOutputRslt").get_text()
  rate = float(rate[:-4])
  
  return rate


app = Flask(__name__)

@app.route('/')
def home():
  return '<h1>Currency Rate API</h1> <p>Example URL: /api/v1/usd-eur</p>'

@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur, out_cur):
  rate = get_currency(in_cur, out_cur)
  result_dictionary = {'input_currency':in_cur, 'output_currency':out_cur, 'rate':rate}
  return jsonify(result_dictionary)

app.run(host='0.0.0.0')


# Este código es una aplicación web simple escrita en Flask que actúa como una API para obtener tasas de 
# conversión de moneda. Permite a los usuarios obtener la tasa de cambio entre dos monedas específicas
# haciendo una solicitud a la ruta correspondiente en el servidor.

# Aquí está el desglose del código:

# Importación de bibliotecas:

# from flask import Flask, jsonify: Importa la clase Flask y la función jsonify de la biblioteca Flask. 
# Flask es un framework de desarrollo web para Python que facilita la creación de aplicaciones web, mientras 
# que jsonify se utiliza para devolver respuestas JSON en Flask.
# from bs4 import BeautifulSoup: Importa la clase BeautifulSoup de la biblioteca BeautifulSoup. BeautifulSoup 
# es una biblioteca de Python utilizada para analizar y extraer datos de documentos HTML y XML.
# import requests: Importa la biblioteca requests, que se utiliza para enviar solicitudes HTTP en Python.
# Definición de la función get_currency():

# Esta función toma dos parámetros: in_currency (la moneda de entrada) y out_currency (la moneda de salida).
# Hace una solicitud HTTP a una página web que proporciona tasas de cambio entre las dos monedas especificadas.
# Utiliza BeautifulSoup para analizar el contenido HTML de la página y extraer la tasa de cambio.
# Devuelve la tasa de cambio como un número flotante.
# Creación de una instancia de la aplicación Flask:

# app = Flask(__name__): Crea una instancia de la clase Flask y la almacena en la variable app.
# Definición de rutas de la aplicación:

# @app.route('/') y @app.route('/api/v1/<in_cur>-<out_cur>'): Estas son decoraciones de ruta en Flask que definen 
# las rutas a las que la aplicación responderá.
# La función home() devuelve una página de inicio simple con instrucciones sobre cómo utilizar la API.
# La función api(in_cur, out_cur) toma dos parámetros de ruta (in_cur y out_cur) que representan las monedas de entrada y salida.
# Dentro de la función api(), se llama a la función get_currency() para obtener la tasa de cambio entre las monedas especificadas.
# Se crea un diccionario de resultados que contiene las monedas de entrada y salida, así como la tasa de cambio.
# Se devuelve una respuesta JSON utilizando jsonify() con el diccionario de resultados.
# Ejecución de la aplicación Flask:

# app.run(host='0.0.0.0'): Inicia el servidor Flask y lo hace accesible en todas las interfaces de red (0.0.0.0). 
# Esto hace que la aplicación sea visible desde cualquier máquina en la red local.
# En resumen, este código define una aplicación web simple que proporciona una API para obtener tasas de conversión 
# de moneda utilizando Flask y BeautifulSoup. Los usuarios pueden acceder a la API haciendo solicitudes a las rutas especificadas 
# y recibirán respuestas JSON con las tasas de cambio correspondientes.