import os
import io
import googleapiclient.http
from service_drive import obtener_servicio

def pedir_nombre_archivo(servicio, archivos_en_drive) -> str:
    """
    """
    
    archivo_deseado = input('Indica el nombre del/los archivo/s a descargar: ')

    while not archivo_deseado in archivos_en_drive:
        archivo_deseado = input('Archivo inexistente. Vuelve a intentar\n')

    return archivo_deseado

def pedir_ubicacion():
    """
    """

    ubicacion = input('¿Dónde deseas guardar el archivo')

    return ubicacion

def obtener_id(servicio, nombre_archivo : str) -> str:
    """
    PRE: servicio debe ser un objeto de tipo Resource con los datos del usuario
    y nombre_archivo una cadena con el nombre del archivo o carpeta que desea
    descargar
    POST: Devuelve una cadena con el id del archivo indicado
    """

    id_archivos = ''

    return id_archivos

def descargar(id_archivos):
    """
    """

    fh = io.FileIO(id_archivos, 'r')
    descargar = googleapiclient.http.MediaIoBaseDownload(fh, )
    terminado = False

    while terminado is False:
        status, terminado = descargar.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))

def main() -> None:

    servicio = obtener_servicio()
    archivos_en_drive = servicio.files().list().execute()

    id_archivos = pedir_nombre_archivo(servicio, archivos_en_drive)
    solicitud = servicio.files().get_media(fileId=id_archivos)
    descargar(id_archivos)
    ubicacion = pedir_ubicacion()

main()