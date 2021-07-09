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
matcheo = {"Guido_Costa": {"107789_Ebbes": True,
                           "110389_Puccar": False,
                           "108923_Iglesias": True},
           "Leonel_Chaves": {"107876_Ianello": True}}

def generador_ruta(sistema_actual: str, BARRA: str) -> str:
    if sistema_actual == "Windows":
        ruta = os.getcwd()
        divisiones = ruta.split(BARRA)
        ruta_escritorio = []
        for i in range(4):
            ruta_escritorio.append(divisiones[i])
        path = BARRA.join(ruta_escritorio)
        print(path + BARRA)
        return path


def crear_carpetas(matcheo: dict, ruta_sistema: str) -> None:
    path = ruta_sistema + BARRA
    os.mkdir(f"{path}Evaluaciones")
    path += ("Evaluaciones" + BARRA)
    for docente in matcheo:
        os.mkdir(f"{path}{docente}")
        for alumno in matcheo[docente]:
            padron_alumno = ""
            for i in range(6):
                padron_alumno += alumno[i]
            if matcheo[docente][alumno]:
                os.mkdir(f"{path}{docente}{BARRA}{padron_alumno}")


# url del repo: https://github.com/IglesiasT/TP2.git
def main() -> None:
    ruta = generador_ruta(OS, BARRA)
    crear_carpetas(matcheo, ruta)

main()
