import platform
import os

# Recibo estructura del estilo:
# Match = {docente : {alumno1: Boole,...},...}
# Docente = Nombre_Apellido
# Alumno = Padron_Apellido
# Boole = True o False dependiendo de Entrega correcta o incorrecta

OS = platform.system()
CADENA = "\ "
BARRA = CADENA[0]


def generador_ruta(sistema_actual: str, BARRA: str) -> str:
    if sistema_actual == "Windows":
        ruta = os.getcwd()
        divisiones = ruta.split(BARRA)
        ruta_escritorio = []
        for i in range(4):
            ruta_escritorio.append(divisiones[i])
        path = BARRA.join(ruta_escritorio)
        print(path)


def crear_carpetas(matcheo: dict, ruta_sistema: str) -> None:
    for docente in matcheo:
        os.mkdir(f"{ruta_sistema}/{docente}")
        for alumno in matcheo[docente]:
            padron_alumno = ""
            for i in range(6):
                padron_alumno += alumno[i]
            os.mkdir(f"{ruta_sistema}/{docente}/{padron_alumno}")


# url del repo: https://github.com/IglesiasT/TP2.git