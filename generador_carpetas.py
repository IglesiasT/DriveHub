import platform
import os
import archivos
import csv
import shutil


# Recibo estructura del estilo:
# CSV del matcheo, cada linea:   PADRON, Apellido_profe
# Info_alumno sale del mail: [ PADRON , APELLIDO NOMBRE , <direccion.zip>]
# [ PADRON , APELLIDO NOMBRE , <direccion.zip>, direccion_carpeta_alumno]
# Windows: "C:\Users\Nombre_usuario\Desktop
# Linux: "\home\nombre_usuario\desktop


OS = platform.system()


def generador_carpeta_zip() -> None:
    ruta_desk = generador_ruta_base(OS)
    if not os.path.isdir(ruta_desk + "descargas.zip"):
        os.mkdir(f"{ruta_desk}descargas_zip")


def generador_carpeta(nombre_carpeta: str, ruta_base: str) -> None:
    """
    PRE  : ruta_base debe ser un directorio valido
    POST : crea la carpeta en el directorio, si el nombre elegido es invalido o existe, se pide otro
    """
    pidiendo_nombre = True
    while pidiendo_nombre:
        try:
            os.mkdir(ruta_base + "/" + nombre_carpeta)
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
    """
    PRE  : Opciones es la lista de carpetas contenidas dentro de C:users de la cual se filtraran solo
           los que sean posibles nombres de usuario
    POST : Segun el usuario, la funcion devolvera el nombre del usuario elegido
    """
    buscando = True
    usuarios = []
    carpetas_inutiles = ["All Users", "Default", "Default User", "Public"]  # Carpetas predeteminadas y no de
    for carpeta in opciones:                                                # usuarios, de windows
        if carpeta in carpetas_inutiles:
            usuarios.append(carpeta)
    while buscando:
        for usuario in usuarios:
            if os.path.isdir("C:/Users/" + usuario + "/Desktop"):
                pregunta = input(f"Tu usuario es {usuario}? (s/n): ")
                if pregunta == "s":
                    buscando = False
                    USUARIO = usuario
    return USUARIO


def ruta_desk_w() -> str:
    """
    POST : La funcion devolvera un path en formato string, que lleva al escritorio de un usuario de windows
    """
    ruta_base = r"C:\Users"
    opciones = archivos.listar_carpetas(ruta_base)
    USUARIO = averiguar_usuario_w(opciones)
    ruta_desktop = "C:/Users/" + USUARIO + "/desktop/"
    return ruta_desktop


def averiguar_usuario_linux(opciones: list) -> str:
    """
        PRE  : Opciones es la lista de carpetas contenidas dentro de /home de la cual se filtraran solo
               los que sean posibles nombres de usuario
        POST : Segun el usuario, la funcion devolvera el nombre del usuario elegido
        """
    buscando = True
    usuarios = []
    carpetas_inutiles = ["All Users", "Default", "Default User", "Public"]
    for carpeta in opciones:
        if carpeta in carpetas_inutiles:
            usuarios.append(carpeta)
    while buscando:
        for usuario in usuarios:
            if os.path.isdir("/home/" + usuario + "/Desktop"):
                pregunta = input(f"Tu usuario es {usuario}? (s/n): ")
                if pregunta == "s":
                    buscando = False
                    USUARIO = usuario
    return USUARIO


def ruta_desk_linux() -> str:
    """
    POST : La funcion devolvera un path en formato string, que lleva al escritorio de un usuario de linux
    """
    ruta_base = r"/home"
    opciones = archivos.listar_carpetas(ruta_base)
    USUARIO = averiguar_usuario_linux(opciones)
    ruta_desktop = "/home/" + USUARIO + "/desktop/"
    return ruta_desktop


def generador_ruta_base(sistema_actual: str) -> str:
    """
    PRE  : sistema actual solo puede ser las 3 opciones que devolveria el platform.system()
    POST : La funcion devolvera la ruta al desktop del usuario, independientemente del sistema
    """
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
    """
    POST : Si el string pasado como parametro tiene comillas, las removera, y lo devuelve sin comillas
    """
    salida = ""
    for caracter in palabra:
        if caracter != '"':
            salida += caracter
    return salida


def info_matcheo(padron: str, matcheo: str) -> str:
    """
    PRE  : Matcheo debe ser el nombre del archivo contra el que se quiere buscar el dato correspondiente
    POST : Si el padron esta en el archivo, devuelve el nombre del profesor correspodiente,
           si no lo tiene, quedara sin profesor
    """
    profe = "SIN_PROFE"
    with open(matcheo, mode='r', newline='', encoding="UTF-8") as archivo:
        csv_reader = csv.reader(archivo, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            profesor = row[1]
            padron_csv = row[0]
            if padron_csv in padron:
                print("padron: ", padron_csv, "profesor: ", profesor)
                profe = profesor
                print(profe)
    return profe


def verificar_dir(direccion: str) -> str:
    """
    PRE  : Recibe un path en forma de string
    POST : Si el path corresponde a una carpeta, la devolvera, sino, pedira otra hasta que sea una existente
    """
    while not os.path.isdir(direccion):
        direccion = input("La ruta es incorrecta, intenta denuevo: ")
    return direccion


def carpeta_evaluaciones() -> str:
    """
    POST : Ademas de crear la carpeta, devuelve el nombre del path donde se ubica
    """
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
    """
    PRE  : Path debe ser una ruta de carpeta valida
    POST : Creara la carpeta con el nombre del docente dentro del path especificado (Si es que no existe ya
           la carpeta del docente) y devolvera la ruta de esa nueva carpeta
    """
    if not os.path.isdir(path + docente):
        os.mkdir(path + docente)
    path = path + docente + "/"
    return path


def carpeta_alumno(path: str, alumno: str, padron_alumno: str) -> str:
    """
    PRE  : Path debe ser una ruta valida de un directorio
    POST : Creara la carpeta con el nombre del alumno y su padron, dentro del path especificado
    (Si es que no existe ya la carpeta del alumno) y devolvera la ruta de esa nueva carpeta
    """
    if not os.path.isdir(path + padron_alumno + alumno):
        os.mkdir(path + padron_alumno + alumno)
    path = path + padron_alumno + alumno
    return path


def crear_carpetas(info_alumno: list, carpeta_evaluacion: str) -> None:
    """
    Aclaraciones extra de la funcion, el path se va actualizando a medida que se crean las carpetas
    PRE  : Info alumnos debera contener un numero de padron, el nombre y apellido de ese alumno, y
    la ruta donde se encuentra el archivo zip de su entrega
    """
    ubicacion_zip = info_alumno[2]
    archivo_matcheo = "alumnos_profesores.csv"
    padron_alumno = info_alumno[0]
    docente = info_matcheo(padron_alumno, archivo_matcheo)
    nombre_alumno = "_" + info_alumno[1].replace(" ", "_")    # Dando un formato mas amigable
    path = carpeta_evaluacion
    path = carpeta_docente(path, docente)
    path = carpeta_alumno(path, nombre_alumno, padron_alumno)
    archivos.descomprimir_archivo(ubicacion_zip, path)
