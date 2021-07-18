from service_drive import obtener_servicio

SERVICIO = obtener_servicio()
FILTROS_PERMITIDOS = {
    'Tipo de archivo': {
        'Imagen': '',
        'Video': '',
        'Carpeta': 'application/vnd.google-apps.folder'
    },
    'Nombre de archivo': '',
    'Compartido conmigo': 'SharedWithMe',
    'Fecha': ''
}

def busqueda_por_filtros(filtros : list):
    """
    """
    ###recorrer filtros y al final printear los archivos que hayan cumplido con todos los filtros
    solicitud = SERVICIO.files().list().execute()
    page_token = None

    while True:
        for archivo in solicitud.get('files', []):  #Recorre los archivos en Drive del usuario
            print('Found file: %s (%s)' % (archivo.get('name'), archivo.get('id')))    ###archivo.get('name')

        page_token = solicitud.get('nextPageToken', None)
        
        if page_token is None:
            break

def main() -> None:        
    filtros_deseados = []
    opcion = None

    while opcion != len(FILTROS_PERMITIDOS):
        #Muestra menu al usuario con el formato <opcion> - <tipo de filtro>
        for indice, filtro in enumerate(FILTROS_PERMITIDOS.keys()):
            print(f'{indice} - {filtro}')
        print(f'{len(FILTROS_PERMITIDOS)} - Salir')

        try:
            print('----- Listado de archivos -----')
            opcion = int(input('Introduzca una opción para agregar un filtro:'))
            print(f'Filtros establecidos: {filtros_deseados}')
            
            if opcion not in filtros_deseados:
                filtros_deseados.append(filtros_permitidos[opcion])
        
        except IndexError:
            if opcion != len(FILTROS_PERMITIDOS):
                print('Opción inválida')

        except TypeError:
            print('Debes introducir un número')

    busqueda_por_filtros(filtros_deseados)

main()
