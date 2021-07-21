from service_drive import obtener_servicio

SERVICIO = obtener_servicio()
DATOS_FILTROS = {
    'Imagenes': 'image/jpeg',
    'Videos': 'video/mp3',
    'Carpetas': 'application/vnd.google-apps.folder'
}

def pedir_tipo() -> str:
    """
    """

    tipo = ''


    return tipo

def busqueda_por_filtros(filtros : list):
    """
    if not filtros (lista vacia) printear todos los archivos
    if Imagenes q='mimeType="image/jpeg"'
    if Videos q='mimeType="video/mp3"'
    if Carpetas q='mimeType="application/vnd.google-apps.folder'
    if isinstance(i, tuple()) caso tupla (nombre, nombre_deseado) recordar clase objetos aclarar como PRE
    else filtro desconocido
    """
    ###recorrer filtros y al final printear los archivos que hayan cumplido con todos los filtros
    solicitud = SERVICIO.files().list().execute()
    page_token = None

    while True:
        for archivo in solicitud.get('files', []):  #Recorre los archivos en Drive del usuario
            print('Archivo encontrado: %s (%s)' % (archivo.get('name'), archivo.get('id'))) ###solo nombre?

        page_token = solicitud.get('nextPageToken', None)
        
        if page_token is None:
            break

def main() -> None:
    filtros_deseados = []
    opcion = None

    print('----- Listado de archivos y carpetas -----')
    
    while opcion != 3:
        print('Elige un filtro, si no deseas ninguno elige Salir')
        print('1 - Tipo\n2 - Nombre\n3 - Salir')
        opcion = int(input('\nFiltro deseado: '))

        if opcion == 1:
            filtros_deseados.append(pedir_tipo())

        if opcion == 2:
            pass
        elif opcion != 3:
            print('Opción inválida, volvé a intentar')

    busqueda_por_filtros(set(filtros_deseados)) #set para no tener filtros repetidos

main()
