import requests

def get_weather(city, units='metric', api_key='835b6471ff413f257a0183767779a91e'):
  url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
  r = requests.get(url)
  content = r.json()
  with open('data.txt', 'a') as file:
    for dicty in content['list']:
      file.write(f"{dicty['dt_txt']}, {dicty['main']['temp']}, {dicty['weather'][0]['description']}\n")

print(get_weather(city='Washington'))

# 835b6471ff413f257a0183767779a91e
# 26631f0f41b95fb9f5ac0df9a8f43c92

# Este código es una función de Python que utiliza la biblioteca requests para hacer una solicitud a la API de OpenWeatherMap
# y obtener el pronóstico del tiempo para una ciudad específica.

# Aquí está el desglose del código:

# Importación de la biblioteca requests: La primera línea del código importa la biblioteca requests, 
# que se utiliza para hacer solicitudes HTTP en Python.

# Definición de la función get_weather(): Se define una función llamada get_weather() que acepta 
# tres parámetros: city (la ciudad para la que se desea obtener el pronóstico del tiempo), units 
# (las unidades en las que se desea obtener el pronóstico del tiempo, con un valor predeterminado 
# de 'metric' para unidades métricas), y api_key (la clave de API para acceder a la API de OpenWeatherMap, 
# con un valor predeterminado proporcionado).

# Construcción de la URL de la solicitud: La URL se construye utilizando los parámetros proporcionados en la 
# función. Se incluye la ciudad (city), la clave de API (api_key) y las unidades (units).

# Realización de la solicitud GET: Se utiliza requests.get() para hacer una solicitud GET a la URL construida.

# Obtención del contenido de la respuesta como JSON: Se utiliza el método .json() en el objeto de respuesta (r) 
# para convertir el contenido de la respuesta en un objeto JSON de Python.

# Escritura de los datos en un archivo de texto: Se abre un archivo de texto llamado 'data.txt' en modo de apertura 
# append (agregar) y se itera sobre cada elemento de la lista 'list' en el objeto JSON obtenido. Para cada elemento, 
# se escribe en el archivo una línea que contiene la fecha y hora ('dt_txt'), la temperatura ('main'['temp']) y la descripción del clima ('weather'[0]['description']).

# Llamada a la función get_weather(): Se llama a la función get_weather() con el valor de la ciudad ('Washington') y 
# no se imprime el resultado. En su lugar, la función escribe los datos en el archivo de texto 'data.txt'.

# En resumen, esta función permite obtener el pronóstico del tiempo para una ciudad específica utilizando la API de 
# OpenWeatherMap y escribir los datos en un archivo de texto.

