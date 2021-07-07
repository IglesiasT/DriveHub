import os
import io
import googleapiclient.http
from service_drive import obtener_servicio

#Consultar qué tiene el usuario en drive
servicio = obtener_servicio()

archivos_en_drive = servicio.files().list().execute()

id_archivos = ''    ###obtener id archivo/s

solicitud = servicio.files().get_media(fileId=id_archivos)

fh = io.BytesIO()
descargar = googleapiclient.http.MediaIoBaseDownload(fh, solicitud)
terminado = False

while terminado is False:
    status, terminado = descargar.next_chunk()
    print("Download %d%%." % int(status.progress() * 100))

#Validar y guardarme lo que quiere

#Preguntarle donde lo quiere descargar

#Guardar en binario archivos deseados en ruta deseada
