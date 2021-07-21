from service_drive import obtener_servicio

SERVICIO = obtener_servicio()
DATOS_FILTROS = {
    'Imagenes': 'image/jpeg',
    'Videos': 'video/mp3',
    'Carpetas': 'application/vnd.google-apps.folder'
}

def busqueda_por_filtros(filtros : set) -> None:
    """
    if not filtros (lista vacia) printear todos los archivos
    if Imagenes q='mimeType="image/jpeg"'
    if Videos q='mimeType="video/mp3"'
    if Carpetas q='mimeType="application/vnd.google-apps.folder'
    if isinstance(i, tuple()) caso tupla (nombre, nombre_deseado) recordar clase objetos aclarar como PRE
    else filtro desconocido
    solicitud = SERVICIO.files().list().execute()
    page_token = None

    while True:
        for archivo in solicitud.get('files', []):  #Recorre los archivos en Drive del usuario
            print('Archivo encontrado: %s (%s)' % (archivo.get('name'), archivo.get('id'))) ###solo nombre?

        page_token = solicitud.get('nextPageToken', None)
        
        if page_token is None:
            break
    """
    
    #busquedas anidadas
    

def main() -> None:
    filtro_deseado = None
    opcion = None

    print('----- Listado de archivos y carpetas -----')
    
    while opcion != 3:
        print('Elige un filtro, si no deseas ninguno elige Salir')
        print('1 - Carpetas\n2 - Nombre\n3 - Salir')
        opcion = int(input('\nFiltro deseado: '))

        if opcion == 1:
            filtro_deseado = 'Carpeta'

        if opcion == 2:
            filtro_deseado = input('Ingresa el nombre: ')

        elif opcion != 3:
            print('Opción inválida, volvé a intentar')

    busqueda_por_filtros(filtro_deseado)

main()
