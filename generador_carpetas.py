import platform
import os
import archivos
import csv

# Recibo estructura del estilo:
# CSV del matcheo, cada linea:   PADRON, Apellido_profe
# Info_alumno sale del mail: [ PADRON , APELLIDO NOMBRE , <direccion.zip>]
# [ PADRON , APELLIDO NOMBRE , <direccion.zip>, direccion_carpeta_alumno]

OS = platform.system()
CADENA = "\ "
BARRA = CADENA[0]


def generador_carpeta_zip() -> None:
    ruta = ruta_desk_w()
    if not os.path.isdir(ruta + "descargas.zip"):
        os.mkdir(f"{ruta}descargas_zip")
    ruta = ruta + "descargas_zip" + BARRA
    return ruta

def listar_carpetas(ruta_dir: str, printear = False) -> list:
    lista_carpetas = []
    for contenido in os.listdir(ruta_dir):
        ruta_completa = os.path.join(ruta_dir, contenido)
        if os.path.isdir(ruta_completa):
            lista_carpetas.append(contenido)
            if printear:
                print(contenido)
    return lista_carpetas

def generador_carpeta(nombre_carpeta: str, ruta_base: str) -> None:
    pidiendo_nombre = True
    while pidiendo_nombre:
        try:
            os.mkdir(ruta_base + nombre_carpeta)
        except IOError:
            if os.path.isdir(ruta_base + nombre_carpeta):
                nombre_carpeta = input("La carpeta ya existe, ingrese otro nombre o Exit para cancelar: ")
                if nombre_carpeta == "Exit":
                    pidiendo_nombre = False
            else:
                nombre_carpeta = input("El nombre ingresado contiene caracteres invalidos,"
                                       " por favor intente denuevo: ")
        else:
            print("La carpeta se ha creado correctamente")
            pidiendo_nombre = False

def averiguar_usuario_w(opciones: list) -> str:
    buscando = True
    USUARIO = ""
    carpetas_inutiles = ["All Users", "Default", "Default User", "Public"]
    for carpeta in opciones:
        if buscando and os.path.isdir("C:/Users/" + carpeta + "/Desktop") and carpeta not in carpetas_inutiles:
            pregunta = input(f"Tu usuario es {carpeta}? (s/n): ")
            if pregunta == "s":
                buscando = False
                USUARIO = carpeta
    return USUARIO

def averiguar_usuario_linux(opciones: list) -> str:
    buscando = True
    USUARIO = ""
    for carpeta in opciones:
        if buscando and os.path.isdir("/home/" + carpeta + "/Desktop"):
            pregunta = input(f"Tu usuario es {carpeta}? (s/n): ")
            if pregunta == "s":
                buscando = False
                USUARIO = carpeta
    return USUARIO

def ruta_desk_w() -> str:
    ruta_base = r"C:\Users"
    opciones = listar_carpetas(ruta_base)
    USUARIO = averiguar_usuario_w(opciones)
    ruta_desktop = "C:/Users/" + USUARIO + "/desktop/"
    return ruta_desktop

def ruta_desk_linux() -> str:
    ruta_base = r"/home"
    opciones = listar_carpetas(ruta_base)
    USUARIO = averiguar_usuario_linux(opciones)
    ruta_desktop = "/home/" + USUARIO + "/desktop/"
    return ruta_desktop

def generador_ruta_base(sistema_actual: str) -> str:
    if sistema_actual == "Windows":
        ruta = ruta_desk_w()
    elif sistema_actual == "Linux":
        ruta = ruta_desk_linux()
    elif sistema_actual == "Mac":
        pass
    else:
        print("Lo sentimos, su sistema no es soportado por el programa.")
        ruta = ""
    return ruta


def remover_comillas(palabra: str) -> str:
    salida = ""
    for caracter in palabra:
        if caracter != '"':
            salida += caracter
    return salida


def info_matcheo(padron: str, matcheo: str) -> str:
    profe = ""
    
    with open(matcheo, mode ='r', newline='', encoding="UTF-8") as archivo:
        csv_reader = csv.reader(archivo, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            profesor = row[1]
            padron_csv = row[0]
            if padron_csv in padron:
                print("padron: ",padron_csv,"profesor: ",profesor)
                profe = profesor  
    print(profe)
    return profe

"""
def carpeta_evaluaciones(ruta_desktop: str) -> str:
    # marcando_carpeta = True
    # while marcando_carpeta:
    #     archivos.listar_carpetas()
    if not os.path.isdir(f"{ruta_desktop}Evaluaciones"):
        os.mkdir(f"{ruta_desktop}Evaluaciones")
    path = ruta_desktop + "Evaluaciones" + BARRA
    return path
"""
def verificar_dir(direccion: str) -> str:
    while not os.path.isdir(direccion):
        direccion = input("La ruta es incorrecta, intenta denuevo: ")
    return direccion

def carpeta_evaluaciones() -> str:
    existe = input("La carpeta de evaluaciones existe (1) o quieres crearla (2)? : ")
    if existe == "1":
        direccion = input("Cual es la ruta completa de la carpeta: ")
        path = verificar_dir(direccion)
    else:
        direccion = input("Donde quieres crear la carpeta? : ")
        direccion = verificar_dir(direccion)
        nombre = input("Que nombre tendra la carpeta evaluacion? : ")
        generador_carpeta(nombre, direccion)
        path = direccion + "/" + nombre + "/"
    return path

def carpeta_docente(path: str, docente: str) -> str:
    if not os.path.isdir(path + docente):
        os.mkdir(path + docente)
    path = path + docente + BARRA
    return path


def carpeta_alumno(path: str, alumno: str, padron_alumno: str) -> str:
    if not os.path.isdir(path + padron_alumno + alumno):
        os.mkdir(path + padron_alumno + alumno)
    else: 
        print(path + padron_alumno + alumno)
    path = path + padron_alumno + alumno
    return path

def crear_carpetas(info_alumno: list , carpeta_evaluacion: str) -> None:
    """
    Aclaraciones extra de la funcion, el path se va actualizando a medida que se crean las carpetas
    """
    ubicacion_zip = info_alumno[2]
    archivo_matcheo = "alumnos_profesores.csv"
    padron_alumno = info_alumno[0]
    docente = info_matcheo(padron_alumno, archivo_matcheo)
    nombre_alumno = "_" + info_alumno[1].replace(" ", "_")
    path = carpeta_evaluacion
    #path = "C:/Users/Hector/Desktop/evaluaciones/"  # Se reemplaza por funcion que elige donde quiere y
    path = carpeta_docente(path, docente)      # con que nombre la carpeta
    
    path = carpeta_alumno(path, nombre_alumno, padron_alumno)
    print(path)
    print(ubicacion_zip)
    archivos.descomprimir_archivo(ubicacion_zip, path)

"""
def crear_carpetas(info_alumno: list, carpeta_evaluacion: str) -> None:
    
    #Aclaraciones extra de la funcion, el path se va actualizando a medida que se crean las carpetas
    
    ubicacion_zip = info_alumno[2]
    archivo_matcheo = "alumnos_profesores.csv"
    padron_alumno = info_alumno[0]
    docente = info_matcheo(padron_alumno, archivo_matcheo)
    nombre_alumno = "_" + info_alumno[1].replace(" ", "_")
    path = carpeta_evaluacion
    path = carpeta_docente(path, docente)
    path = carpeta_alumno(path, nombre_alumno, padron_alumno)
    archivos.descomprimir_archivo(ubicacion_zip, path)
"""