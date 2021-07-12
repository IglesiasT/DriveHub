import io
import googleapiclient.http
from service_drive import obtener_servicio

SERVICIO = obtener_servicio()
SOLICITUD = SERVICIO.files().list().execute()
ARCHIVOS_EN_DRIVE = SOLICITUD.get('files', [])

def archivo_valido(archivo_deseado : str) -> bool:
    """
    PRE: Recibe una cadena con el nombre del archivo o carpeta que el usuario
    desea descargar de Drive a su equipo.
    POST: Devuelve en booleano si el archivo o carpeta existe en su Drive
    """

    for archivo in ARCHIVOS_EN_DRIVE:
        if archivo['name'].capitalize() == archivo_deseado.capitalize():
            return True
    
    return False 

def pedir_ubicacion():
    """
    """

    ubicacion = input('¿Dónde deseas guardar el archivo')

    return ubicacion

def obtener_id(archivo_deseado : str) -> str:
    """
    PRE: Recibe una cadena con el nombre del archivo o carpeta que desea
    descargar
    POST: Devuelve una cadena con el id del archivo indicado
    """

    try:
        for archivo in ARCHIVOS_EN_DRIVE:
            if archivo['name'].capitalize() == archivo_deseado.capitalize():
                return archivo['id']
    except:
        print('Archivo inválido. Corroborar que el nombre del archivo se encuentre en Drive del usuario.')

def descargar_archivo(id_archivo : str, ruta : str):
    """
    """

    solicitud_descarga = SERVICIO.files().get_media(fileId=id_archivo)
    fh = io.BytesIO()
    descargar = googleapiclient.http.MediaIoBaseDownload(fh, solicitud_descarga)
    terminado = False

    while terminado is False:
        status, terminado = descargar.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))

def guardar_en_binario(ubicacion, archivo) -> None:
    """
    """

    pass

def main() -> None:
    
    #Pedido y validación de archivo
    archivo_deseado = input('Indica el nombre del archivo o carpeta a descargar: ')
    
    while not archivo_valido(archivo_deseado):
        archivo_deseado = input('Archivo inexistente. Vuelve a intentar\n')

    id_archivo = obtener_id(archivo_deseado)

    ubicacion = pedir_ubicacion()
    descargar_archivo(id_archivo)
    guardar_en_binario(ubicacion, id_archivo)

main()