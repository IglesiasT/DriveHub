from generador_carpetas import generador_carpeta, ruta_desk_w
import io, os
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

def pedir_ruta() -> str:
    """
    Pide al usuario la ruta donde desea guardar el archivo
    hasta que ingrese una válida
    POST: Devuelve una cadena con la ruta deseada
    """

    print('¿Dónde deseas guardar el archivo o carpeta?')
    ruta = input('Indica la ruta: ')

    while not (os.path.exists(ruta) or os.path.isdir(ruta)):
        ruta = input('Ruta inválida. Vuelve a intentarlo')

    return ruta

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
        f.write(fh.read())

def main() -> None:
    
    #Pedido y validación de archivo (Drive reconoce las carpetas como archivos)
    archivo_deseado = input('Indica el nombre del archivo o carpeta a descargar: ')
    
    while not archivo_valido(archivo_deseado):
        archivo_deseado = input('Archivo inexistente. Vuelve a intentar\n')

    id_archivo = obtener_id(archivo_deseado)

    #Pedido y validación de la ruta deseada para el archivo a descargar
    ruta = pedir_ruta()
    descargar_archivo(id_archivo, os.path.join(ruta, archivo_deseado))

main()