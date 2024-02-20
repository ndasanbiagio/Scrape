import requests
import json

url = 'https://languagetool.org/v2/check'
data = {
    'text': 'Tis is a nixe day!',
    'language': 'auto'
}

response = requests.post(url, data=data)
result = json.loads(response.text)
print(result)



# Este código utiliza la biblioteca requests para hacer una solicitud HTTP POST a la API de LanguageTool, un servicio 
# en línea que proporciona verificación gramatical y ortográfica en varios idiomas. Aquí está la explicación paso a paso:

# Se importan las bibliotecas requests y json, que se utilizarán para realizar la solicitud HTTP y 
# manejar la respuesta JSON, respectivamente.

# Se define la variable url que contiene la URL a la que se enviará la solicitud POST. En este caso, la URL es 
# 'https://languagetool.org/v2/check', que es la URL de la API de LanguageTool.

# Se define un diccionario llamado data que contiene los datos que se enviarán en la solicitud POST. 
# Este diccionario tiene dos claves:

# La clave 'text' contiene el texto que se va a verificar gramaticalmente. En este caso, el texto es 
# 'Tis is a nixe day!'.
# La clave 'language' especifica el idioma del texto que se va a verificar. Aquí se ha establecido como 
# 'auto', lo que significa que LanguageTool intentará detectar automáticamente el idioma del texto.
# Se realiza la solicitud HTTP POST a la URL especificada (url) utilizando requests.post(). 
# Se pasa la URL y los datos (data) como argumentos. Esto enviará los datos al servidor.

# La respuesta del servidor se almacena en la variable response.

# Se utiliza json.loads() para cargar el contenido de la respuesta (que está en formato JSON) 
# en un diccionario de Python. Esto convierte el texto JSON en un objeto Python.

# El resultado se almacena en la variable result.

# Finalmente, se imprime el resultado. Dependiendo de la respuesta de la API, el resultado 
# podría contener información sobre errores gramaticales u ortográficos encontrados en el texto proporcionado.

# En resumen, este código envía un texto a la API de LanguageTool para verificar su gramática 
# y ortografía, y luego imprime el resultado.