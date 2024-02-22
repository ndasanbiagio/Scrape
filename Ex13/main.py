from pathlib import Path

root_dir = Path('files')

for path in root_dir.glob("**/*"):
    if path.is_file():
        path_parts = path.parts
        subfolders = path.parts[1:-1]
        
        new_filename = "-".join(subfolders) + '-' + path.name
        print(new_filename)
        new_filename = path.with_name(new_filename)
        path.rename(new_filename) 
        
        
        

# Este código parece estar diseñado para renombrar archivos en función 
# de sus subcarpetas. Aquí está lo que hace:

# Itera sobre todos los archivos y directorios (incluidos los anidados) 
# dentro del directorio root_dir.
# Para cada archivo, extrae las partes del camino.
# Extrae las partes del camino que representan las subcarpetas.
# Crea un nuevo nombre de archivo concatenando el nombre de las subcarpetas 
# con el nombre del archivo original, usando un guion como separador.
# Imprime el nuevo nombre de archivo.
# Crea un nuevo objeto Path con el nuevo nombre de archivo.
# Renombra el archivo original con el nuevo nombre.
# Este enfoque reemplaza el nombre del archivo con una cadena que contiene 
# el nombre de todas las subcarpetas, seguido de un guion y el nombre del archivo original.

# Si este es el comportamiento que deseas, el código debería funcionar bien. 
# Sin embargo, ten en cuenta que este enfoque puede llevar a nombres de archivo muy largos 
# o potencialmente conflictivos, dependiendo de la estructura de tus subcarpetas y 
# los nombres de archivo originales. Asegúrate de que este es el comportamiento deseado antes de usar este código en un 
# entorno de producción.