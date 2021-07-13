import platform
import os

# Recibo estructura del estilo:
# CSV del matcheo, cada linea:   PADRON, Apellido_profe
# Info_alumno sale del mail: [ PADRON , APELLIDO NOMBRE , <direccion.zip>]
# [ PADRON , APELLIDO NOMBRE , <direccion.zip>, direccion_carpeta_alumno]

OS = platform.system()
CADENA = "\ "
BARRA = CADENA[0]


def generador_carpeta_zip(BARRA: str) -> None:
    ruta = ruta_desk_w(BARRA)
    os.mkdir(f"{ruta}descargas_zip")


def ruta_desk_w(BARRA: str) -> str:
    ruta = os.getcwd()
    divisiones = ruta.split(BARRA)
    ruta_escritorio = []
    for i in range(4):
        ruta_escritorio.append(divisiones[i])
    ruta = BARRA.join(ruta_escritorio)
    return ruta + BARRA


def generador_ruta(sistema_actual: str, BARRA: str) -> str:
    if sistema_actual == "Windows":
        ruta = ruta_desk_w(BARRA)
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
    with open(matcheo, "r") as archivo:
        for linea in archivo:
            linea = linea.rstrip()
            if padron in linea:
                data_match = linea.split(",")
                profe = data_match[1]
                profe = remover_comillas(profe)
    return profe


def carpeta_evaluaciones(ruta_desktop: str) -> str:
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
        os.mkdir(padron_alumno + alumno)
    path = path + padron_alumno + alumno
    return path


def crear_carpetas(info_alumno: list, ruta_sistema: str) -> None:
    ubicacaion_zip = info_alumno[2]
    archivo_matcheo = "matcheo.csv"        # Hay que actualizar el nombre
    padron_alumno = info_alumno[0]
    docente = info_matcheo(padron_alumno, archivo_matcheo)
    nombre_alumno = "_" + info_alumno[1].replace(" ", "_")
    path = carpeta_evaluaciones(ruta_sistema)
    path = carpeta_docente(path, docente)
    path = carpeta_alumno(path, nombre_alumno, padron_alumno)
    # descomprimir_zip(ubicacion_zip, path)




# url del repo: https://github.com/IglesiasT/TP2.git
def main() -> None:
    ruta = generador_ruta(OS, BARRA)
    base_alumnos = [["107123", "Ebbes_Gonzalo", "<direccion.zip>"],
                   ["107515", "Nicolas Puccar", "<direccion.zip>"]]
    for elem in base_alumnos:
        info_alumno = elem
        crear_carpetas(info_alumno, ruta)
    generador_carpeta_zip(BARRA)

main()
