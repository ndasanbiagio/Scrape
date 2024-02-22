from pathlib import Path

root_dir = Path('files')  # Define el directorio raíz
file_paths = root_dir.glob("**/*")  # Obtiene todos los archivos dentro de 'files' y sus subdirectorios

for path in file_paths:  # Itera sobre todas las rutas de los archivos y carpetas
    if path.is_file():  # Comprueba si la ruta es un archivo
        parent_folder = path.parts[-2]  # Obtiene el nombre de la carpeta principal (el penúltimo componente de la ruta)
        new_filename = parent_folder + '-' + path.name  # Crea un nuevo nombre de archivo
        print(new_filename)  # Imprime el nuevo nombre de archivo
        new_filepath = path.with_name(new_filename)  # Crea una nueva ruta de archivo con el nuevo nombre
        path.rename(new_filepath)  # Renombra el archivo con el nuevo nombre


# Importación de la clase Path: El script utiliza la clase Path de la biblioteca pathlib de Python. 
# Esta clase proporciona una manera fácil y eficiente de trabajar con rutas de archivos y directorios 
# en Python.

# Definición del directorio raíz: Se establece el directorio raíz como "files" utilizando la clase Path.

# Obtención de rutas de archivos: Se utiliza el método glob("**/*") para obtener todas las rutas de 
# archivos dentro del directorio raíz y sus subdirectorios. Este método realiza una búsqueda recursiva,
# por lo que incluirá todas las subcarpetas y sus archivos.

# Bucle para cada ruta de archivo: Se itera sobre cada una de las rutas de archivo obtenidas en el 
# paso anterior.

# Comprobación si es un archivo: Se verifica si la ruta actual corresponde a un archivo, en lugar 
# de a un directorio, utilizando el método is_file().

# Obtención del nombre de la carpeta principal: Se extrae el nombre de la carpeta principal 
# (el penúltimo componente de la ruta) donde se encuentra el archivo. Esto se hace dividiendo 
# la ruta en partes (parts) y seleccionando el penúltimo elemento (parts[-2]).

# Creación de un nuevo nombre de archivo: Se genera un nuevo nombre de archivo combinando el 
# nombre de la carpeta principal con el nombre original del archivo, separados por un guion.

# Impresión del nuevo nombre de archivo: Se imprime el nuevo nombre de archivo generado.

# Creación de una nueva ruta de archivo: Se crea una nueva ruta de archivo utilizando el nuevo 
# nombre generado, utilizando el método with_name().

# Renombrar el archivo: Se utiliza el método rename() de la clase Path para cambiar el nombre 
# del archivo original al nuevo nombre generado.

# En resumen, este script recorre recursivamente todos los archivos dentro del directorio raíz 
# y sus subdirectorios, y renombra cada archivo agregando el nombre de la carpeta principal 
# como prefijo al nombre original del archivo.