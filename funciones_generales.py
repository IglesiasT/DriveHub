def verificar_pregunta_sino(pregunta: str)->str:
    texto = input(pregunta).upper()
    while (len(texto)<1) or ((texto not in "SI") and (texto not in "NO")):
        print("\nError")
        texto = input(pregunta).upper()
    return texto

def eleccion_nombre(texto)->str:
    print("\n")
    nombre = input(texto)
    eleccion = verificar_pregunta_sino("¿Seguro que es el nombre que desea? Si = si |No = no: ").upper()
    while eleccion in "NO":
        nombre = input(texto)
        eleccion = verificar_pregunta_sino("¿Seguro que es el nombre que desea? Si = si |No = no: ").upper()
    
    return nombre
