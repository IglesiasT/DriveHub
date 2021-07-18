from service_drive import obtener_servicio

SERVICIO = obtener_servicio()
SOLICITUD = SERVICIO.files().list().execute()   ###poner parametros de archivos deseados en list()

def busqueda_por_filtros(): ###recibir por parametro el filtro deseado?
    """
    """

    page_token = None

    while True:
        for archivo in SOLICITUD.get('files', []):  #Recorre los archivos en Drive del usuario
            print ('Found file: %s (%s)' % (archivo.get('name'), archivo.get('id')))    ###investigar funcionamiento

        page_token = SOLICITUD.get('nextPageToken', None)
        
        if page_token is None:
            break

def main() -> None:
    filtros_permitidos = [
        'Tipo de archivo',
        'Nombre de archivo',
        'Compartido conmigo',
        'Fecha'
        ]        
    filtros_deseados = []
    opcion = None

    while opcion != len(filtros_permitidos):
        #Muestra menu al usuario con el formato <opcion> - <tipo de filtro>
        for indice, filtro in enumerate(filtros_permitidos):
            print(f'{indice} - {filtro}')
        print(f'{len(filtros_permitidos)} - Salir')

        try:
            print('----- Listado de archivos -----')
            opcion = int(input('Introduzca una opción para agregar un filtro:'))
            print(f'Filtros establecidos: {filtros_deseados}')
            
            if opcion not in filtros_deseados:
                filtros_deseados.append(filtros_permitidos[opcion])
        
        except IndexError:  ###entra con el 4 por ser indexerror
            if opcion != len(filtros_permitidos):
                print('Opción inválida')

        except TypeError:
            print('Debes introducir un número')

    
main()
