import platform
import os

# Recibo estructura del estilo:
# CSV del matcheo, cada linea:   PADRON, Apellido_profe
# Info_alumno sale del mail: [ PADRON , APELLIDO NOMBRE , <direccion.zip>]

OS = platform.system()
CADENA = "\ "
BARRA = CADENA[0]


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


def crear_carpetas(info_alumno: list, ruta_sistema: str) -> None:
    archivo_matcheo = "matcheo.csv"
    padron_alumno = info_alumno[0]
    docente = info_matcheo(padron_alumno, archivo_matcheo)
    path = ruta_sistema
    if not os.path.isdir(f"{path}Evaluaciones"):
        os.mkdir(f"{path}Evaluaciones")
    path = path + "Evaluaciones" + BARRA
    nombre_alumno = " - " + info_alumno[1]
    if os.path.isdir(path + docente):
        os.mkdir(path + docente + BARRA + padron_alumno + nombre_alumno)
    else:
        os.mkdir(path + docente)
        os.mkdir(path + docente + BARRA + padron_alumno + nombre_alumno)



# url del repo: https://github.com/IglesiasT/TP2.git
def main() -> None:
    ruta = generador_ruta(OS, BARRA)
    base_alumnos = [["107123", "Ebbes_Gonzalo"], ["107515", "Nicolas Puccar"]]
    for elem in base_alumnos:
        info_alumno = elem
        crear_carpetas(info_alumno, ruta)

main()
