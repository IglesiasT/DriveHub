import platform
import os
import archivos

# Recibo estructura del estilo:
# CSV del matcheo, cada linea:   PADRON, Apellido_profe
# Info_alumno sale del mail: [ PADRON , APELLIDO NOMBRE , <direccion.zip>]
# [ PADRON , APELLIDO NOMBRE , <direccion.zip>, direccion_carpeta_alumno]
# Windows: "C:\Users\Nombre_usuario\Desktop
# Linux: "\home\nombre_usuario\desktop


OS = platform.system()
CADENA = "\ "
BARRA = CADENA[0]


# ### Prestado de Ro ###


def listar_carpetas(ruta_dir: str) -> list:
    lista_carpetas = []
    for contenido in os.listdir(ruta_dir):
        ruta_completa = os.path.join(ruta_dir, contenido)
        if os.path.isdir(ruta_completa):
            lista_carpetas.append(contenido)
    return lista_carpetas


# #########################


def generador_carpeta_zip() -> None:
    ruta = ruta_desk_w()
    if not os.path.isdir(ruta + "descargas.zip"):
        os.mkdir(f"{ruta}descargas_zip")
    ruta = ruta + "descargas_zip" + BARRA
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


def averiguar_usuario(opciones: list) -> str:
    buscando = True
    USUARIO = ""
    for carpeta in opciones:
        if buscando and os.path.isdir("C:/Users/" + carpeta + "/Desktop"):
            pregunta = input(f"Tu usuario es {carpeta}? (s/n): ")
            if pregunta == "s":
                buscando = False
                USUARIO = carpeta
    return USUARIO


def ruta_desk_w() -> str:
    ruta_base = r"C:\Users"
    opciones = listar_carpetas(ruta_base)
    USUARIO = averiguar_usuario(opciones)
    ruta_desktop = "C:/Users/" + USUARIO + "/desktop/"
    os.mkdir(ruta_desktop + "Carla")
    return ruta_desktop


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
    with open(matcheo, mode='r', newline='', encoding="UTF-8") as alumnos_csv:
        csv_reader = csv.reader(alumnos_csv, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            padron_csv = row[0]
            nombre_apellido_csv = row[1]
            if ((padron in padron_csv) and (nom_apellido == nombre_apellido_csv)):
                existe = True

    # with open(matcheo, "r") as archivo:
    #     for linea in archivo:
    #         linea = linea.rstrip()
    #         if padron in linea:
    #             data_match = linea.split(",")
    #             profe = data_match[1]
    #             profe = remover_comillas(profe)
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
    path = path + padron_alumno + alumno
    return path


def crear_carpetas(info_alumno: list) -> None:
    """
    Aclaraciones extra de la funcion, el path se va actualizando a medida que se crean las carpetas
    """
    ruta_dsk = generador_ruta(OS)
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


def desempaquetar_orden(comando: str) -> list:
    partes = comando.split(" - ")
    return partes


def conseguir_usuario() -> str:
    ruta = os.getcwd()
    partes = BARRA.split(ruta)
    usuario = partes[2]
    return usuario


# def ejecutar_comandos() -> None:
#     exit = False
#     ruta = ""
#     # print reglas comando
#     usuario = conseguir_usuario()
#     while not exit:
#         # listar opciones
#         comando = input(f"{usuario}: ")
#         orden = desempaquetar_orden(comando)
#         if orden[0] == "cd":
#             if orden[1] == ".."
#                 # def borrar ultima ruta
#             else:
#                 # redefinir ruta y
#         elif orden[0] == "mk":
#             # Crear carpeta o archivo
#         elif orden[0] == "help":
#             # printear reglas comando
#         elif orden[0] == "exit":
#             exit = True
#         else:
#             print("El comando es invalido, si necesita ayuda utilice 'help' ")
ruta_desk_w()