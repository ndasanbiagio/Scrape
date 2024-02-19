import requests


def get_news(topic, from_date, to_date, language='en',
            api_key='890603a55bfa47048e4490069ebee18c'):
  url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}8&sortBy=popularity&language={language}&apiKey={api_key}'
  r = requests.get(url)
  content = r.json()
  articles = content['articles']
  results = []
  for article in articles:
    results.append(f"TITLE\n'{article['title']}, '\nDESCRIPTION\n', {article['description']}")
  return results

# NOTE: Change the from_date and to_date below to reflect recent dates
# Otherwise, you will get an error.
print(get_news(topic='space', from_date='2022-11-25', to_date='2022-11-28'))



# Este código es una función de Python que utiliza la biblioteca requests para hacer una solicitud a la API de News API y recuperar noticias sobre un tema específico en un rango de fechas determinado.

# Aquí está el desglose del código:

# Importación de la biblioteca requests: La primera línea del código importa la biblioteca requests, que se utiliza para hacer solicitudes HTTP en Python.

# Definición de la función get_news(): Se define una función llamada get_news() que acepta varios parámetros: topic (el tema sobre el que se desean noticias), 
# from_date (la fecha de inicio del rango de fechas), to_date (la fecha de finalización del rango de fechas), language (el idioma en el que se desean las noticias, 
# con un valor predeterminado de 'en' para inglés), y api_key (la clave de API para acceder a la API de News API, con un valor predeterminado proporcionado).

# Construcción de la URL de la solicitud: La URL se construye utilizando los parámetros proporcionados en la función. Se incluye el tema (topic), las fechas de
# inicio y finalización (from_date y to_date), el idioma (language), y la clave de API (api_key).

# Realización de la solicitud GET: Se utiliza requests.get() para hacer una solicitud GET a la URL construida.

# Obtención del contenido de la respuesta como JSON: Se utiliza el método .json() en el objeto de respuesta (r) para convertir el contenido de la respuesta en un objeto JSON de Python.

# Extracción de los artículos de las noticias: Del objeto JSON obtenido, se extraen los artículos de las noticias, que generalmente están contenidos en la clave 'articles'.

# Procesamiento de los artículos de las noticias: Se itera sobre cada artículo en la lista de artículos y se construye una cadena de texto formateada para cada uno, 
# que contiene el título y la descripción del artículo. Estas cadenas se agregan a una lista llamada results.

# Retorno de los resultados: Se devuelve la lista results, que contiene las cadenas de texto formateadas para cada artículo de las noticias.

# Llamada a la función get_news() e impresión de los resultados: Se llama a la función get_news() con algunos valores de ejemplo para el tema, la fecha de inicio y 
# la fecha de finalización, y se imprime el resultado.

# En resumen, esta función permite obtener noticias sobre un tema específico en un rango de fechas determinado utilizando la API de News API y devuelve los títulos
# y descripciones de los artículos de noticias encontrados.