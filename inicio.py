import gmail_prueba
import os
import generador_carpetas
import archivos
def validar_opcion(lista: list)->str:
    """
    Pre-condicion: (lista_de_opciones: list)
    Post-condicion: devuelve la opcion elegida
    Valida la opcion del usuario
    """
    opc = input("\nIngrese un comando: ").upper()
    while(len(opc) < 1 ) or (opc not in lista):
        opc=input("Error, intentelo nuevamente: ").upper()
    return opc

def mostrar_menu(lugar: str)->None:
    """
    Pre-condicion: (lugar: str) *lugar = si el usuario se encuentra en el repositorio remoto o en el local
    Post-condicion: no devulve nada
    Muestra las opciones del menu, dependiendo donde se encuentre
    """
    if lugar == "drivehub":
        print("\nMenu del DriveHub:")
        print("1-Mostrar archivos\n2-Crear archivos\n3-Subir archivo")
        print("4-Sincronizar")
        print("M-mostrar menu\nS-Salir")
    elif lugar == "local":
        print("\nMenu local:")
        print("1-Descargar eveluciones de alumnos\n2-Mostrar archivos\n3-Crear archivos\n4-Subir archivo")
        print("5-Descargar archivo\n6-Sincronizar")
        print("M-mostrar menu\nS-Salir")
    else:
        print("\nMenu: \nR-Archivos del DriveGit\nL-Archivos locales\nM-mostrar menu\nS-Salir")
    
    
def definir_lugar(opc)->str:    
    if (opc in "R"):
        lugar = "drivehub"
    elif opc in "L":
        lugar = "local"
    elif (opc ):
        lugar = "principales"
    return lugar


def main()->None:
    CARPETA_ACTUAL = os.getcwd()
    listas_opciones= {
        "principales":["R","L","S","M"],
        "local":["1","2","3","4","5", "6","S","M"],
        "drivehub":["1","2","3","4","S","M"]
    }
    lugar = ""
    mostrar_menu(lugar)
    opc = validar_opcion(listas_opciones["principales"])
    lugar = definir_lugar(opc)
    
    while opc != "S":
        if (lugar == "local"):
            if (opc in "1"):
                gmail_prueba.inicio_gmail()

            if (opc in "2"):
                print("Mostrar archivos")

            if (opc in "3"):
                print("Crear archivos")

            if (opc in "4"):
                print("Subir archivo")

            if (opc in "5"):
                print("Descargar archivo")

            if (opc in "6"):
                print("Sincronizar")

        if (lugar == "drivehub"):
            if (opc in "1"):
                print("Mostrar archivos")

            if (opc in "2"):
                print("Crear archivos")

            if (opc in "3"):
                print("Subir archivo")

            if (opc in "4"):
                print("Sincronizar")


        if (opc in "M"):
            mostrar_menu(lugar)

        opc = validar_opcion(listas_opciones[lugar])
        if (opc in "R") or (opc in "L"):
            definir_lugar(opc)
main()

