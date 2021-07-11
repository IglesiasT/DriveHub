import io
import googleapiclient.http
from service_drive import obtener_servicio

SERVICIO = obtener_servicio()
SOLICITUD = SERVICIO.files().list().execute()
ARCHIVOS_EN_DRIVE = SOLICITUD.get('files', [])

def pedir_nombre_archivos() -> str:
    """
    Solicita al usuario el nombre del archivo que desea descargar de su Drive
    lo valida y si existe devuelve una cadena con el nombre del mismo,
    sino vuelve a pedir hasta que sea valido
    """
    
    archivo_deseado = input('Indica el nombre del/los archivo/s a descargar: ')

    for archivo in ARCHIVOS_EN_DRIVE:
        if archivo['name'] == archivo_deseado:
            return archivo_deseado
    
    archivo_deseado = input('Archivo inexistente. Vuelve a intentar\n')

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

    return SOLICITUD

def descargar(id_archivos):
    """
    """

    solicitud = SERVICIO.files().get_media(fileId=id_archivos)
    fh = io.FileIO(id_archivos, 'r')
    descargar = googleapiclient.http.MediaIoBaseDownload(fh, solicitud)
    terminado = False

    while terminado is False:
        status, terminado = descargar.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))

def guardar_en_binario(ubicacion, archivo) -> None:
    """
    """

    pass

def main() -> None:
    
    #archivos_deseados = pedir_nombre_archivos()
    id_archivos = obtener_id('archivos_deseados')
    
    descargar(id_archivos)

    ubicacion = pedir_ubicacion()
    guardar_en_binario(ubicacion, id_archivos)

main()