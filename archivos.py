import zipfile
import csv
import os

def verificar_zip(ruta: str)->bool:
    CADENA = "\ "
    BARRA = CADENA[0]
    existe = False
    lista_ruta = ruta.split(BARRA)
    espacio_archivo = (len(lista_ruta)-1)
    lista_archivo = (lista_ruta[espacio_archivo].replace(".zip",""))
    lista_archivo = lista_archivo.split(" - ")
    padron = lista_archivo[0]
    nom_apellido = lista_archivo[1] 

    with open("alumnos.csv", mode ='r', newline='', encoding="UTF-8") as alumnos_csv:
        csv_reader = csv.reader(alumnos_csv, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            padron_csv = row[0]
            nombre_apellido_csv = row[1]
            if ((padron in padron_csv) and (nom_apellido == nombre_apellido_csv)):
                existe = True   
    return existe

def descomprimir_archivo(ruta_zip: str, ruta_extraccion: str)->None:
    contraseña = None
    archivo_zip = zipfile.ZipFile(ruta_zip, "rb")
    try:
        print(archivo_zip.namelist())
        archivo_zip.extractall(pwd=contraseña, path=ruta_extraccion)
    except:
        pass
    archivo_zip.close

def listar_directorio(ruta_dir: str)->None:
    contenido = os.listdir(ruta_dir)
    for i in range(len(contenido)):
        print(contenido[i])

def verificar_archivo_directorio(ruta_dir: str, archivo: str)->bool:
    contenido = os.listdir(ruta_dir)
    existe = False
    for i in range(len(contenido)):
        print(contenido[i])
        if archivo in contenido[i]:
            existe = True  
    """
    with os.scandir(ruta_dir) as directorio:
        for contenido in directorio:
            print(contenido)
        if archivo in directorio:
            existe= True
        else:
            existe = False
    """
    return existe
