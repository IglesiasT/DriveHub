from service_drive import obtener_servicio

SERVICIO = obtener_servicio()

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

    print('----- Listado de archivos y carpetas -----')
    
    while opcion != 4:
        print('1 - Tipo de archivo\n2 - Nombre de archivo\n3 - Compartido conmigo\n4 - Salir')
        opcion = int(input('Introduce el numero asociado al filtro deseado, si no deseas filtrar introduce 4'))
        
        if opcion == 1:
            tipo_archivo = None
            while tipo_archivo != 4:
                print('1 - Imagenes\n2 - Videos\n3 - Carpetas\n4 - Volver')
                tipo_archivo = int(input('Qué tipo de archivos deseas buscar?'))
                
                #validar que la opcion no se encuentra ya en filtros deseados
                if tipo_archivo == 1:
                    filtros_deseados.append('image/jpeg')
                if tipo_archivo == 2:
                    filtros_deseados.append('video/mp4')
                if tipo_archivo == 3:
                    filtros_deseados.append('application/vnd.google-apps.folder')
                else:
                    print('Opcion invalida')

        if opcion == 2:
            nombre_archivo = input('Introduce el nombre: ')
            filtros_deseados.append(nombre_archivo)

        if opcion == 3:
            filtros_deseados.append(True)

        else:
            print('Debes introducir el número asociado al filtro deseado')

    busqueda_por_filtros(filtros_deseados)

main()
