import os
import csv

# Leo_Chaves
    # 107123
    # 108212
    # 107313
# Franco_Lucchesi
    # 108414
    # 107515
    # 108616
# Guido_Costa
    # 107717
    # 108818
    # 107919
# Franco_Capra
    # 108010
    # 107121
    # 108323
# Daniela_Palacios
    # 107424
    # 108525
    # 107626
# Ariadna_Catteneo
    # 108727
    # 107828
    # 108929
# Carolina_Di_Matteo
    # 107020
    # 108131
    # 107232
# Lautaro_Dabbraccio
    # 108434
    # 107535
    # 108636
# Tomas Villegas
    # 107737
    # 108838
    # 107939
# Bruno Lanzillotta
    # 108030
    # 107141
    # 108242


def crear_csv_alumno(alumnos: dict)->None:
    directorio = os.getcwd() #direcctiorio en donde estamos
    if not os.path.isfile(directorio):
        with open("alumnos_profesores.csv", 'w', newline = '', encoding="UTF-8") as alumnos_profesores_csv:
            csv_writer = csv.writer(alumnos_profesores_csv, delimiter=',', quotechar='"', quoting= csv.QUOTE_NONNUMERIC)
            csv_writer.writerow(["Padron", "Nombre y Apellido del profesor"])

            for i in range(len(alumnos)):
                csv_writer.writerow((alumnos[i][0], alumnos[i][1]))
    """
    else:
        with open("alumnos_profesores.csv", 'a', newline = '', encoding="UTF-8") as alumnos_profesores_csv:
            csv_writer = csv.writer(alumnos_profesores_csv, delimiter=',', quotechar='"', quoting= csv.QUOTE_NONNUMERIC)
            csv_writer.writerow(["Padron", "Nombre"])

            for i in range(len(alumnos)):
                csv_writer.writerow((alumnos[i][0], alumnos[i][1]))
    """

def main()->None:
    alumnos = [
    ["107123","Leo_Chaves"],
    ["108212","Leo_Chaves"],
    ["107313","Leo_Chaves"],
    ["108414", "Franco_Lucchesi"],
    ["107515", "Franco_Lucchesi"],
    ["108616", "Franco_Lucchesi"],
    ["107717", "Guido_Costa"],
    ["108818", "Guido_Costa"],
    ["107919", "Guido_Costa"],
    ["108010", "Franco_Capra"],
    ["107121", "Franco_Capra"],
    ["108323", "Franco_Capra"],
    ["107424", "Daniela_Palacios"],
    ["108525", "Daniela_Palacios"],
    ["107626", "Daniela_Palacios"],
    ["108727", "Ariadna_Catteneo"],
    ["107828", "Ariadna_Catteneo"],
    ["108929", "Ariadna_Catteneo"],
    ["107020", "Carolina_Di_Matteo"],
    ["108131", "Carolina_Di_Matteo"],
    ["107232", "Carolina_Di_Matteo"],
    ["108434", "Lautaro_Dabbraccio"],
    ["107535", "Lautaro_Dabbraccio"],
    ["108636", "Lautaro_Dabbraccio"],
    ["107737", "Tomas_Villegas"],
    ["108838", "Tomas_Villegas"],
    ["107939", "Tomas_Villegas"],
    ["108030", "Bruno_Lanzillotta"],
    ["107141", "Bruno_Lanzillotta"],
    ["108242", "Bruno_Lanzillotta"]]
    crear_csv_alumno(alumnos)

main()