import zipfile
import csv
import os

def verificar_zip(ruta: str)->bool:
    """
    Pre-condicion: ruta donde se encuentra el archivo(tipo str)
    Post-condicion: devuelve un booleano (TRUE = Existe | FALSE = No existe)  
    Verifica si el archivo enviado es un zip, y si esta correctamente nombrado
    """
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
            if ((padron in padron_csv) and (nom_apellido in nombre_apellido_csv)):
                existe = True   
    return existe

def descomprimir_archivo(ruta_zip: str, ruta_extraccion: str)->None:
    """
    Pre-condicion: (ruta_del_archivo: str, ruta_de_extraccion_del_archivo: str)
    Post-condicion: no devulve nada
    Descomprime los archivos zip
    """
    contraseña = None
    archivo_zip = zipfile.ZipFile(ruta_zip, "r")
    try:
        print(archivo_zip.namelist())
        archivo_zip.extractall(pwd=contraseña, path=ruta_extraccion)
    except:
        pass
    archivo_zip.close

def listar_directorio(ruta_dir: str)->None:
    """
    Pre-condicion: (ruta_del_directorio: str)
    Post-condicion: no devulve nada
    Muestra todos los archivos y carpetas que hay en la ruta deseada
    """
    contenido = os.listdir(ruta_dir)
    for i in range(len(contenido)):
        print(contenido[i])

def listar_carpetas(ruta_dir: str, printear = False)-> list:
    """
    Pre-condicion: (ruta_del_directorio: str, printeo: str)
    Post-condicion: devuelve el nombre de las carpetas(tipo list)
    Crea una lista con todas las carpetas de la ruta deseada y si es desado puede printearla
    """
    lista_carpetas = []
    for contenido in os.listdir(ruta_dir):
        ruta_completa = os.path.join(ruta_dir, contenido)
        if os.path.isdir(ruta_completa):
            lista_carpetas.append(contenido)
            if printear:
                print(contenido)

    return lista_carpetas

def verificar_archivo_directorio(ruta_dir: str, archivo: str)->bool:
    """
    Pre-condicion: (ruta_del_directorio: str, nombre_del_archivo: str)
    Post-condicion: devuelve un booleano (TRUE = Existe | FALSE = No existe)  
    Verifica si el archivo deseado, existe en el direcctorio indicado
    """
    contenido = os.listdir(ruta_dir)
    existe = False
    for i in range(len(contenido)):
        print(contenido[i])
        if archivo in contenido[i]:
            existe = True  

    return existe
