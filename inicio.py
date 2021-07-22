import gmail_prueba
import os
import generador_carpetas
import archivos
import funciones_generales
import shutil
import platform
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
        print("1-Mostrar archivos\n2-Crear archivo o carpeta\n3-Subir archivo\n4-Descargar archivo")
        print("5-Sincronizar")
        print("M-mostrar menu\nS-Salir")
    elif lugar == "local":
        print("\nMenu local:")
        print("1-Descargar eveluciones de alumnos\n2-Mostrar archivos\n3-Crear archivo o carpeta\n4-Subir archivo")
        print("\n5-Sincronizar")
        print("M-mostrar menu\nS-Salir")
    else:
        print("\nMenu: \nR-Archivos del DriveGit\nL-Archivos locales\nM-mostrar menu\nS-Salir")  
    
def definir_lugar(opc: str)->str: 
    """
    Pre-condicion: (opcion: str)
    Post-condicion: devulve el lugar como string
    Define si el entorno es el local o el remoto, dependiendo dela opcion del usuario
    """   
    if (opc in "R"):
        lugar = "drivehub"
    elif opc in "L":
        lugar = "local"
    elif (opc ):
        lugar = "principales"
    return lugar

def carpeta_o_archivo()->bool:
    """
    Pre-condicion: ninguna
    Post-condicion: devuleve un booleano, True = carpeta | False = archivo
    Le pregunta al usuario si quiere crear una carpeta o un archivo
    """
    print("\n")
    carpeta = input("¿Desea crear una carpeta o un archivo? Carpeta = C | Archivo = A: ").upper()
    while(len(carpeta) < 1 ) or ((carpeta not in "C") and (carpeta not in "A")):
        carpeta=input("Error, intentelo nuevamente: ").upper()
    if carpeta in "A":
        carpeta = False
    elif carpeta == "C":
        carpeta = True

    return carpeta

def main()->None:
    CARPETA_ACTUAL = os.getcwd()
    OS = platform.system()
    listas_opciones= {  #Son las opcciones que puede elegir el usurio dependiendo de cada menu
        "principales":["R","L","S","M"],
        "local":["1","2","3","4","5", "6","S","M"],
        "drivehub":["1","2","3","4","S","M"]
    }
    lugar = ""  #El lugar puede ser local o en el drivehub
    mostrar_menu(lugar)
    opc = validar_opcion(listas_opciones["principales"])
    lugar = definir_lugar(opc)
    
    while opc != "S":
        if (lugar == "local"):
            if (opc in "1"): #Descargar eveluciones de alumnos
                gmail_prueba.inicio_gmail()

            if (opc in "2"): #Mostrar archivos
                archivos.listar_directorio(CARPETA_ACTUAL)

            if (opc in "3"): #Crear archivo o carpeta
                carpeta = carpeta_o_archivo()
                if carpeta == True:
                    nombre = funciones_generales.eleccion_nombre("Ingrese el nombre de la carpeta: ")
                    generador_carpetas.generador_carpeta(nombre, CARPETA_ACTUAL)
                else:
                    archivos.crear_archivo(CARPETA_ACTUAL)

            if (opc in "4"): #Subir archivo
                print("Subir archivo")

            if (opc in "5"): #Sincronizar
                print("Sincronizar")

        if (lugar == "drivehub"): 
            if (opc in "1"): #Mostrar archivos
                print("Mostrar archivos")

            if (opc in "2"): #Crear archivos
                print("Crear archivos")

            if (opc in "3"): #Subir archivo
                print("Subir archivo")

            if (opc in "4"): #Descargar archivo
                print("Descargar archivo")

            if (opc in "5"): #Sincronizar
                print("Sincronizar")

        if (opc in "M"):
            mostrar_menu(lugar)

        opc = validar_opcion(listas_opciones[lugar])
        if (opc in "R") or (opc in "L"):
            definir_lugar(opc)
    escritorio = generador_carpetas.generador_ruta_base(OS) 
    existe = archivos.verificar_archivo_directorio(escritorio , "descargas_zip") #verifica si la carpeta descarga exista
    if existe:
        shutil.rmtree(escritorio + "descargas_zip")   #borra la carpeta descargas

main()

