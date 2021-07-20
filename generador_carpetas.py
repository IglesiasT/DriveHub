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
    if not os.path.isfile(ruta + "descargas.zip"):
        os.mkdir(f"{ruta}descargas_zip")
    ruta = ruta + BARRA + "descargas_zip" + BARRA
    return ruta


def generador_carpeta(nombre_carpeta: str) -> None:
    ruta = ruta_desk_w()
    pidiendo_nombre = True
    while pidiendo_nombre:
        try:
            os.mkdir(ruta + nombre_carpeta)
        except IOError:
            if os.path.isdir(ruta + nombre_carpeta):
                nombre_carpeta = input("La carpeta ya existe, ingrese otro nombre o Exit para cancelar: ")
                if nombre_carpeta == "Exit":
                    pidiendo_nombre = False
            else:
                nombre_carpeta = input("El nombre ingresado contiene caracteres invalidos,"
                                       " por favor intente denuevo: ")
        else:
            print("La carpeta se ha creado correctamente")
            pidiendo_nombre = False



def ruta_desk_w() -> str:
    ruta = os.getcwd()
    divisiones = ruta.split(BARRA)
    ruta_escritorio = []
    for i in range(4):
        ruta_escritorio.append(divisiones[i])
    ruta = BARRA.join(ruta_escritorio)
    return ruta + BARRA


def generador_ruta(sistema_actual: str) -> str:
    if sistema_actual == "Windows":
        ruta = ruta_desk_w()
    elif sistema_actual == "Linux":
        pass
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


def carpeta_evaluaciones(ruta_desktop: str) -> str:
    # marcando_carpeta = True
    # while marcando_carpeta:
    #     archivos.listar_carpetas()
    if not os.path.isdir(f"{ruta_desktop}Evaluaciones"):
        os.mkdir(f"{ruta_desktop}Evaluaciones")
    path = ruta_desktop + "Evaluaciones" + BARRA
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

def encontrar_usuario():
    pass

def crear_carpetas(info_alumno: list) -> None:
    """
    Aclaraciones extra de la funcion, el path se va actualizando a medida que se crean las carpetas
    """

    usuario = encontrar_usuario()
    usuario = "Hector"
    ruta_dsk = "C:"+ BARRA + "Users" + BARRA + usuario + BARRA + "Desktop" + BARRA # C:\Users\Hector\Desktop
    ubicacion_zip = info_alumno[2]
    archivo_matcheo = "alumnos_profesores.csv"
    padron_alumno = info_alumno[0]
    docente = info_matcheo(padron_alumno, archivo_matcheo)
    nombre_alumno = "_" + info_alumno[1].replace(" ", "_")
    path = carpeta_evaluaciones(ruta_dsk)    # Se reemplaza por funcion que elige donde quiere y
    path = carpeta_docente(path, docente)      # con que nombre la carpeta
    
    path = carpeta_alumno(path, nombre_alumno, padron_alumno)
    print(path)
    print(ubicacion_zip)
    archivos.descomprimir_archivo(ubicacion_zip, path)
