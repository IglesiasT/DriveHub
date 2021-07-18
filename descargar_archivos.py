from generador_carpetas import generador_carpeta, ruta_desk_w
import io, os
import googleapiclient.http
from service_drive import obtener_servicio

SERVICIO = obtener_servicio()
SOLICITUD = SERVICIO.files().list().execute()
ARCHIVOS_EN_DRIVE = SOLICITUD.get('files', [])

def pedir_nombre_archivo() -> str:
    """
    PRE: Recibe una cadena con el nombre del archivo o carpeta que el usuario
    desea descargar de Drive a su equipo.
    POST: Devuelve en booleano si el archivo o carpeta existe en su Drive
    """

    nombre_archivo = input('Indica el nombre del archivo o carpeta a descargar: ')

    while not nombre_archivo_valido(nombre_archivo):
        nombre_archivo = input('Archivo inexistente. Vuelve a intentar\n')

    return nombre_archivo

def nombre_archivo_valido(nombre_archivo : str) -> bool:
    """
    PRE: Recibe una cadena con el nombre del archivo a verificar
    POST: Devuelve en booleano si el nombre del archivo se encuentra en los archivos
    de Drive del usuario
    """

    archivo_valido = False

    for archivo in ARCHIVOS_EN_DRIVE:
        if archivo['name'].capitalize() == nombre_archivo.capitalize():
            archivo_valido = True

    return archivo_valido

def obtener_id(nombre_archivo : str) -> str:
    """
    PRE: Recibe una cadena con el nombre del archivo o carpeta que desea
    descargar
    POST: Devuelve una cadena con el id del archivo indicado
    """

    try:
        for archivo in ARCHIVOS_EN_DRIVE:
            if archivo['name'].capitalize() == nombre_archivo.capitalize():
                return archivo['id']
    except:
        print('Archivo inválido. Corroborar que el nombre del archivo se encuentre en Drive del usuario.')

def descargar_archivo(id_archivo : str, nombre_archivo : str) -> None:
    """
    PRE: Recibe una cadena con el id del archivo a descargar y su nombre
    POST: Crea una carpeta llamada Descargas Drive en el escritorio y guarda
    el archivo dentro de la misma
    """
    #Localización de la descarga
    nombre_carpeta = 'Descargas Drive'
    generador_carpeta(nombre_carpeta)    #Crea carpeta en escritorio donde voy a guardar el archivo
    ruta = ruta_desk_w() + nombre_carpeta

    #Inicialización de la descarga
    solicitud_descarga = SERVICIO.files().get_media(fileId=id_archivo)
    fh = io.BytesIO()
    descargar = googleapiclient.http.MediaIoBaseDownload(fh, solicitud_descarga)
    terminado = False

    while terminado is False:
        status, terminado = descargar.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))

    #Escritura de archivo en binario dentro de carpeta Descargas Drive
    with open(os.path.join(ruta, nombre_archivo), 'wb') as f:
        f.write(fh.read())  ###revisar fh.read()

def main() -> None:
    
    #Pedido y validación de archivo (Drive reconoce las carpetas como archivos)
    nombre_archivo = pedir_nombre_archivo()

    id_archivo = obtener_id(nombre_archivo)

    descargar_archivo(id_archivo, nombre_archivo)

main()