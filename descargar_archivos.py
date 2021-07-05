#consultar qué tiene el usuario en drive
#preguntar qué archivo o carpeta quiere descargar
#validar y guardarme lo que quiere
#preguntarle donde lo quiere descargar
#validar y descargar donde indicó

from service_drive import obtener_servicio

servicio = obtener_servicio()

archivos_en_drive = servicio.files().list().execute()