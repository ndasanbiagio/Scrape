from pathlib import Path

root_dir = Path('Ex11')
file_paths = root_dir.iterdir()
print(Path.cwd())
for path in file_paths:
    new_filename = "new-" + path.stem + path.suffix
    new_filepath = path.with_name(new_filename)
    print(new_filepath)
    path.rename(new_filepath)
    
    
    
# Claro, aquí tienes una explicación detallada del código proporcionado:

# from pathlib import Path: Esta línea importa la clase Path de la biblioteca pathlib, 
# que proporciona una interfaz orientada a objetos para trabajar con rutas de archivos y 
# directorios de manera más intuitiva que utilizando cadenas de texto.

# root_dir = Path('files'): Define una ruta utilizando la clase Path. Esta ruta representa el 
# directorio 'files'. La variable root_dir ahora contiene un objeto Path que apunta al directorio 'files'.

# file_paths = root_dir.iterdir(): Usa el método iterdir() en el objeto Path para obtener un 
# iterador que recorre todas las rutas de los archivos y directorios contenidos en root_dir. 
# file_paths ahora es un iterador que contiene las rutas de todos los archivos y directorios dentro de 'files'.

# print(Path.cwd()): Imprime el directorio de trabajo actual utilizando el método cwd() de la 
# clase Path. Esto te muestra dónde se está ejecutando el script actualmente.

# for path in file_paths:: Inicia un bucle for que recorre todas las rutas de los archivos y directorios 
# contenidos en file_paths.

# new_filename = "new-" + path.stem + path.suffix: path.stem devuelve el nombre base del archivo 
# (sin la extensión), y path.suffix devuelve la extensión del archivo. Aquí se crea un nuevo nombre 
# de archivo concatenando "new-" al principio del nombre base y manteniendo la extensión.

# new_filepath = path.with_name(new_filename): Usa el método with_name() de la clase Path para crear
# una nueva ruta de archivo con el nuevo nombre. Esto conserva la misma ubicación y extensión del archivo original,
# pero con el nuevo nombre.

# print(new_filepath): Imprime la nueva ruta de archivo.

# path.rename(new_filepath): Finalmente, se utiliza el método rename() de la clase Path para cambiar 
# el nombre del archivo original al nuevo nombre especificado por new_filepath.

# En resumen, este código itera sobre todos los archivos en el directorio 'files', les agrega el prefijo 
# "new-" a sus nombres y los renombra con los nuevos nombres.