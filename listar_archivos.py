from service_drive import obtener_servicio

def main() -> None:
    servicio = obtener_servicio()
    page_token = None

    print('Buscando archivos...')

    while True:
        solicitud = servicio.files().list(
            q="mimeType='image/jpeg'",
            spaces='drive',
            fields='nextPageToken, files(id, name)',
            pageToken=page_token).execute()

        for archivo in solicitud.get('files', []):  #Recorre los archivos en Drive y printea el nombre
            print('Archivo encontrado: %s' % (archivo.get('name')))
        page_token = solicitud.get('nextPageToken', None)

        if page_token is None:
            break

main()
