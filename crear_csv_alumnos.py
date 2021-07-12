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
        with open("alumnos.csv", 'w', newline = '', encoding="UTF-8") as alumnos_profesores_csv:
            csv_writer = csv.writer(alumnos_profesores_csv, delimiter=',', quotechar='"', quoting= csv.QUOTE_NONNUMERIC)
            csv_writer.writerow(["Padron", "Nombre y Apellido"])

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
    ["107123","Brian_Cespedes"],
    ["108212","Bruno_Lanzillotta"],
    ["107313","Bruno_Quiroga"],
    ["108414", "Camila_Rivero"],
    ["107515", "Camila_Alvarez"],
    ["108616", "Camila_Fiorotto"],
    ["107717", "Carlos_Fiamini"],
    ["108818", "Cecilia_Jurges"],
    ["107919", "Clara_Farbiarz"],
    ["108010", "Colby_Vertilus"],
    ["107121", "Cristian_Esem"],
    ["108323", "FCristobal_Rodrigo"],
    ["107424", "Daniel_Arevalo"],
    ["108525", "Daniel_Volvanes"],
    ["107626", "Dante_Reinaudo"],
    ["108727", "David_Burbano"],
    ["107828", "David_Molina"],
    ["108929", "Elvis_Quispe"],
    ["107020", "Emilio_Trevisan"],
    ["108131", "Enzo_Herbas"],
    ["107232", "Ernesto_Monfort"],
    ["108434", "Esteban_Fernandez"],
    ["107535", "Esteban_Sandoval"],
    ["108636", "Ezequiel_Anchorena"],
    ["107737", "Ezequiel_Benzaquen"],
    ["108838", "Facun_Viale"],
    ["107939", "Facundo_Gonzalez"],
    ["108030", "Facundo_Sorasio"],
    ["107141", "Fernando_Guerrico"],
    ["108242", "Florenci_Russo"]
    ]
    crear_csv_alumno(alumnos)

main()
