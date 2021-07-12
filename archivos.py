import zipfile

def descomprimir_archivo(ruta_zip: str, ruta_extraccion: str)->None:
    contraseña = None
    archivo_zip = zipfile.ZipFile(ruta_zip, "r")
    try:
        print(archivo_zip.namelist())
        archivo_zip.extractall(pwd=contraseña, path=ruta_extraccion)
    except:
        pass
    archivo_zip.close

def main()->None:
    CADENA = "\ "
    BARRA = CADENA[0]
    ruta = "E:"+BARRA+"UBA"+BARRA+"Fiuba"+BARRA+"2021"+BARRA+"1074141-Ianniello,Rocio.zip"
    ruta2 ="E:"+BARRA+"UBA"+BARRA+"Fiuba"+BARRA+"2021"
    descomprimir_archivo(ruta, ruta2)

main()