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
    ["107123","Cespedes, Brian"],
    ["108212","Lanzillotta, Bruno"],
    ["107313","Quiroga, Bruno"],
    ["108414", "Rivero, Camila"],
    ["107515", "Alvarez, Camila"],
    ["108616", "Fiorotto, Camila"],
    ["107717", "Fiamini, Carlos"],
    ["108818", "Jurges, Cecilia"],
    ["107919", "Farbiarz, Clara"],
    ["108010", "Vertilus, Colby"],
    ["107121", "Esem, Cristian"],
    ["108323", "Rodrigo, Cristobal"],
    ["107424", "Arevalo, Daniel"],
    ["108525", "Volvanes, Daniel"],
    ["107626", "Reinaudo, Dante"],
    ["108727", "Burbano, David"],
    ["107828", "Molina, David"],
    ["108929", "Quispe, Elvis"],
    ["107020", "Trevisan, Emilio"],
    ["108131", "Herbas, Enzo"],
    ["107232", "Monfort, Ernesto"],
    ["108434", "Fernandez, Esteban"],
    ["107535", "Sandoval, Esteban"],
    ["108636", "Anchorena, Ezequiel"],
    ["107737", "Benzaquen, Ezequiel"],
    ["108838", "Viale, Facundo"],
    ["107939", "Gonzalez, Facundo"],
    ["108030", "Sorasio, Facundo"],
    ["107141", "Guerrico, Fernando"],
    ["108242", "Russo, Florenci"]
    ]
    crear_csv_alumno(alumnos)

main()
