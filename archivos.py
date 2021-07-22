import zipfile
import csv
import os
import funciones_generales
import time

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

def eleccion_tipo_archivos()->str:
    """
    Pre-condicion: ninguna
    Post-condicion: devuelve el tipo de archivo como string
    Se le pide el tipo de archivo al usuario
    """
    print("\n")
    tipo = input("Elija si crear un archivo .Json = j | .CSV = c | .text = t: ").upper()
    eleccion = funciones_generales.verificar_pregunta_sino("¿Seguro que es el archivo que desea? Si = si |No = no: ").upper()
    while eleccion in "NO":
        tipo = input("Elija si crear un archivo .Json = j | .CSV = c | .text = t: ").upper()
        eleccion = funciones_generales.verificar_pregunta_sino("¿Seguro que es el archivo que desea? Si = si |No = no: ").upper()
    
    return tipo

def crear_archivo(ruta_carpeta: str)->None:
    """
    Pre-condicion: (ruta_del_directorio: str)
    Post-condicion: no devulve nada
    Crear un archivo, del tipo y nombre que el usuario le indique
    """
    tipo = eleccion_tipo_archivos()
    pidiendo_nombre = True
    while pidiendo_nombre:
        try:
            nombre = funciones_generales.eleccion_nombre("Ingrese el nombre del archivo: ")
        except IOError:
            if(verificar_archivo_directorio(ruta_carpeta, nombre) == True):
                nombre = input("El archivo ya existe, ingrese otro nombre o Exit para cancelar: ")
                if nombre_carpeta == "Exit":
                    pidiendo_nombre = False
            else:
                nombre_carpeta = input("El nombre ingresado contiene caracteres invalidos,"
                                       " por favor intente de nuevo: ")
        else:   
            if tipo in "T":
                nombre = nombre +".txt"
            if tipo in "C":
                nombre = nombre +".csv"
            if tipo in "J":
                nombre = nombre +".json"
            open(nombre, "w").close()
            print("Se creo el archivo correctamente")

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
        if archivo in contenido[i]:
            existe = True  

    return existe

def fecha_modificacion(ruta_archivo: str)-> str:
    """
    Pre-condicion: (ruta_del_archivo: str)
    Post-condicion: devuelve un string con la fecha, hora de la modificacion
    Indica cuando se hizo la modificacion de un archivo
    """
    modificacion = time.ctime(os.path.getmtime(ruta_archivo))
    print("mod: ", modificacion)
    return modificacion

