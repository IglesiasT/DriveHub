from service_drive import obtener_servicio

SERVICIO = obtener_servicio()
DATOS_FILTROS = {
    'Imagenes': 'image/jpeg',
    'Videos': 'video/mp3',
    'Carpetas': 'application/vnd.google-apps.folder'
}

def pedir_tipo() -> str:
    """
    Muestra un menu al usuario y le permite escoger el tipo de archivo por el cual
    desea filtrar
    POST: Valida la entrada y devuelve una cadena con la opcion elegida
    """
    tipo = ''
    opcion = None

    while opcion != 4:  #optimizar esto y hacerlo escalable
        print('Ingresa el tipo de archivos que deseas ver')
        print('1 - Imagenes\n2 - Videos\n3 - Carpetas\n4 - Volver')
        opcion = int(input('\nIngresa una opción: '))

        if opcion == 1:
            tipo = 'Imagenes'
        
        if opcion == 2:
            tipo = 'Videos'

        if opcion == 3:
            tipo = 'Carpetas'
        
        elif opcion != 4:
            print('Opción inválida, volvé a intentar')

    return tipo

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
    filtros_deseados = []
    opcion = None

    print('----- Listado de archivos y carpetas -----')
    
    while opcion != 3:
        print('Elige un filtro, si no deseas ninguno elige Salir')
        print('1 - Tipo\n2 - Nombre\n3 - Salir')
        opcion = int(input('\nFiltro deseado: '))

        if opcion == 1:
            tipo = pedir_tipo()
            if tipo:    #Valido de no agregar la cadena vacía
                filtros_deseados.append(tipo)

        if opcion == 2:
            nombre_archivos = input('Ingresa el nombre: ')
            filtros_deseados.append(nombre_archivos)

        elif opcion != 3:
            print('Opción inválida, volvé a intentar')

    busqueda_por_filtros(set(filtros_deseados)) #set para no tener filtros repetidos

main()
