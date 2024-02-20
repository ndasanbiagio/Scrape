from pathlib import Path

p1 = Path('files/ghi.txt')
print(type(p1))

if not p1.exists():
  with open(p1, 'w') as file:
    file.write('Content 3')


print(p1.name)
print(p1.stem)
print(p1.suffix)


p2 = Path('files')
print(list(p2.iterdir()))


# Este código utiliza el módulo pathlib de Python, que proporciona una interfaz orientada a 
# objetos para trabajar con rutas de archivos y directorios de una manera más legible y segura.

# Aquí hay una explicación línea por línea:

# from pathlib import Path: Importa la clase Path del módulo pathlib.

# p1 = Path('files/ghi.txt'): Crea un objeto Path llamado p1 que representa la ruta del 
# archivo 'files/ghi.txt'.

# print(type(p1)): Imprime el tipo de p1, que debería ser <class 'pathlib.Path'>.

# if not p1.exists():: Verifica si el archivo representado por p1 no existe.

# with open(p1, 'w') as file:: Si el archivo no existe, abre el archivo en modo escritura 
# ('w'). El archivo se creará si no existe. Utiliza el contexto de with para garantizar
# que el archivo se cierre correctamente después de su uso.

# file.write('Content 3'): Escribe el texto 'Content 3' en el archivo.

# print(p1.name): Imprime el nombre del archivo, que es 'ghi.txt'.

# print(p1.stem): Imprime el tronco del nombre del archivo, es decir, el nombre del 
# archivo sin la extensión. En este caso, imprimiría 'ghi'.

# print(p1.suffix): Imprime la extensión del archivo, que en este caso sería '.txt'.

# p2 = Path('files'): Crea otro objeto Path llamado p2 que representa el directorio 'files'.

# print(list(p2.iterdir())): Itera sobre los elementos dentro del directorio representado 
# por p2 y los imprime como una lista. Esto imprimirá todos los archivos y subdirectorios 
# dentro del directorio 'files'.