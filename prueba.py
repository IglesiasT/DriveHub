def validar_opcion(lista: list)->str:
    opc = input("\nIngrese un comando: ").upper()
    while(len(opc) < 1 ) or (opc not in lista):
        opc=input("Error, intentelo nuevamente: ")
    return opc

def menu(lugar: str)->None:
    if lugar == "drivegit":
        print("\nMenu del DriveGit:")
        print("1-Mostrar archivos\n2-Crear archivos\n3-Subir archivo")
        print("5-Sincronizar")
        print("M-mostrar menu\nS-Salir")
    elif lugar == "local":
        print("\nMenu local:")
        print("1-Mostrar archivos\n2-Crear archivos\n3-Subir archivo")
        print("4-Descargar archivo\n5-Sincronizar")
        print("M-mostrar menu\nS-Salir")
    else:
        print("\nMenu: \nR-Archivos del DriveGit\nL-Archivos locales\nM-mostrar menu\nS-Salir")
    
    
def definir_lugar(opc)->str:    
    if (opc == "R"):
        lugar = "drivegit"
    elif opc == "L":
        lugar = "local"
    else:
        lugar = "principales"
    return lugar


def main()->None:
    listas_opciones= {
        "principales":["R","L","S","M"],
        "drivegit":["1","2","3","4","5","S","M"],
        "local":["1","2","3","5","S","M"]
    }
    lugar = ""
    menu(lugar)
    opc = validar_opcion(listas_opciones["principales"])
    lugar = definir_lugar(opc)
    
    while opc != "S":
        if (opc == "M"):
            menu(lugar)
        opc = validar_opcion(listas_opciones[lugar])
main()