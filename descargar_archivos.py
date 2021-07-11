import os
import io
import googleapiclient.http
from service_drive import obtener_servicio

SERVICIO = obtener_servicio()
ARCHIVOS_EN_DRIVE = SERVICIO.files().list().execute()

def pedir_nombre_archivos() -> str:
    """
    Solicita al usuario el nombre del archivo que desea descargar de su Drive
    lo valida y si existe devuelve una cadena con el nombre del mismo,
    sino vuelve a pedir hasta que sea valido
    """
    
    archivo_deseado = input('Indica el nombre del/los archivo/s a descargar: ')

    while not archivo_deseado in ARCHIVOS_EN_DRIVE: ##esta comparando str con files
        archivo_deseado = input('Archivo inexistente. Vuelve a intentar\n')

    return archivo_deseado

def pedir_ubicacion():
    """
    """

    ubicacion = input('¿Dónde deseas guardar el archivo')

    return ubicacion

def obtener_id(nombre_archivo : str) -> str:
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
    descargar = googleapiclient.http.MediaIoBaseDownload(fh, SERVICIO)
    terminado = False

    while terminado is False:
        status, terminado = descargar.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))

def guardar_en_binario(ubicacion, archivo) -> None:
    """
    """

    pass

def main() -> None:

    archivos_deseados = pedir_nombre_archivos(SERVICIO, archivos_en_drive)
    id_archivos = obtener_id(archivos_deseados)
    solicitud = SERVICIO.files().get_media(fileId=id_archivos)
    descargar(id_archivos, SERVICIO)

    ubicacion = pedir_ubicacion()
    guardar_en_binario(ubicacion, id_archivos)

main()