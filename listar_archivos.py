from service_drive import obtener_servicio

SERVICIO = obtener_servicio()

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
    filtros_posibles = ('Tipo', 'Nombre')
    filtros_deseados = set()
    opcion = None

    print('----- Listado de archivos y carpetas -----')
    
    while opcion != len(filtros_posibles):
        
        for i in range(len(filtros_posibles)):  #Muestro opciones al usuario
            print(f'{i} - {filtros_posibles[i]}')
        print(f'{len(filtros_posibles)} - Salir')

        opcion = int(input('Introduce el número asociado al filtro deseado, si no deseas filtrar introduce Salir'))
        
        

    busqueda_por_filtros(filtros_deseados)

main()
