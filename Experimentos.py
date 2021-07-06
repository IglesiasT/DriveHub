import os
directorio_actual = os.getcwd()
archivo = "Ruta"
boolean = os.path.exists(directorio_actual)    # booleano depende de si existe la ruta
genera_direccion = os.path.join(directorio_actual, archivo)   # Unira directorio y archivo
os.remove(archivo)       # Elimina archivo
os.mkdir("Carpeta")

