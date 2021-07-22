
import pickle
import shutil
import json
import csv
import os
import gmail
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import generador_carpetas
import archivos

#GET https://www.googleapis.com/gmail/v1/users/me/messages?q=in:sent after:2014/01/01 before:2014/02/01

#https://gmail.googleapis.com/gmail/v1/users/{userId}/labels

#https://gmail.googleapis.com/gmail/v1/users/{userId}/messages

#https://gmail.googleapis.com/gmail/v1/users/{userId}/messages/{id}

#https://gmail.googleapis.com/gmail/v1/users/{userId}/messages/{messageId}/attachments/{id}

#https://www.googleapis.com/gmail/v1/users/me/messages?q=in:sent after:2014/01/01 before:2014/02/01

#https://gmail.googleapis.com/upload/gmail/v1/users/{userId}/messages/send

# ["123654 " , Nicolas Puccar]

def evaluar_alumnos()->list:
    """
    se devolvera una lista conformada con listas de 2 constantes donde se identificara el 
    padron del alumno seguido del profesor asignado " [ 125463 , leo chaves ]"
    """

    cursantes = "alumnos_profesores.csv"

    datos = list()
    with open(cursantes, newline='', encoding="UTF-8") as archivo_csv:
        csv_reader = csv.reader(archivo_csv, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            datos.append(row)

    return datos


def detectar_gmails(recibidos : dict)->list:
    """
    pre : recibe un diccionario con los mensajes recibidos por la cuenta en INBOX

    post: devuelve una lista con todos los ID recibidos
    """

    identificados = []

    labels = recibidos.get('messages', ["INBOX"])

    if not labels:
        print('No labels found.')

    else:
        for label in labels:
            identificados.append(label["id"])

    return identificados

def generar_codigo(servicio : dict , correo_recibido : dict, recibidos : dict)->str:
    """
    pre: recibe el servicio de gmail, el correo recibido/a evaluar y los emails recibidos

    post : devuelve un str en bytes simbolizando el archivo adjunto enviado por el usuario
    """

    mensaje_id = recibidos["messages"][0]["id"]
    contenido_id = correo_recibido["payload"]["parts"][1]["body"]["attachmentId"]
    resultado_2 = servicio.users().messages().attachments().get(userId = 'me', messageId = mensaje_id, id = contenido_id ).execute()
    dato = resultado_2["data"]
    codigo = base64.urlsafe_b64decode(dato.encode('UTF-8'))

    return codigo


def evaluar_padron(padron : str, alumnos : dict)->bool:
    """
    pre: recibe el padron del asunto del mail y una lista con listas que contienen los padrones y sus respectivos correctores

    post: devuelve un booleano que representa si el padron pertenece o no a la lista de alumnos
    """

    flag = False

    for i in range(len(alumnos)):
        if padron == alumnos[i][0]:
            flag = True
        
    return flag

def generar_mensaje(correo_recibido : dict, servicio : dict,flag : bool, booleano : bool)->None:
    """
    pre : recibe el ID del correo recibido/a analizar, el servicio de gmail, un booleano que representa que el padron pertenece
    al de uno de los alumnos cursantes y otro booleano que representa que el archivo recibido es correcto

    post: envia un email informando sobre el estado de su entrega
    """

    destinatario = correo_recibido["payload"]["headers"][6]["value"]

    if flag == True:

        if booleano == True:
            emailMsg = "su correo fue recibido correctamente"

        elif booleano == False:
            emailMsg = "el archivo adjunto no es correcto, envie nuevamente el mail con el archivo correcto"

    elif flag == False:
        emailMsg = "el padron es incorrecto, envie el email con el padron correcto"

    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = destinatario
    nombre = correo_recibido["payload"]["headers"][19]["value"]
    mimeMessage['subject'] = nombre
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
    message = servicio.users().messages().send(userId='me', body={'raw': raw_string}).execute()

def guardar_archivo(correo_recibido : dict, padron : str , alumnos : dict, servicio : dict, recibidos : dict, lista : list,archivo_ruta : str,ruta_evaluaciones:str)->None:
    """
    pre : recibe el ID del correo recibido/a analizar, el padron recibido del asunto del gmail, una lista con listas que contienen los padrones y sus respectivos correctores, 
    el servicio de gmail, un diccionario con los mensajes recibidos por la cuenta en INBOX, una lista que contiene el padron y el nombre enunciado en el asunto, un str representando
    la ruta de los zip y un str representando la carpeta ruta donde iran las evaluaciones

    post : en caso de ser los datos del asunto correcto y el archivo adjunto ser correcto, enviara el adjunto a las carpetas ruta y se le informara mediante mail,
    en caso de haber algun dato erroneo, se le informara mediante mail para que reenvie el mail con los respectivos cambios
    """

    flag = evaluar_padron(padron,alumnos)
    if flag == True:

        CADENA = "\ "

        BARRA = CADENA[0]        

        archivo_dir = correo_recibido["payload"]["parts"][1]["filename"]
        print(archivo_dir)

        ruta_zip = archivo_ruta + BARRA + archivo_dir

        # ruta_zip = archivos + BARRA + "123654 - Puccar, Nicolas.zip" 
        
        booleano = archivos.verificar_zip(ruta_zip)
        print(booleano)
 
        if booleano == True:
            
            #print("el mail es correcto")
            generar_mensaje(correo_recibido,servicio,flag,booleano)
            codigo = generar_codigo(servicio, correo_recibido, recibidos)
            descripcion = correo_recibido["payload"]["parts"][1]["filename"]
            with open(descripcion, 'wb') as f:
                f.write(codigo)
            try:
                shutil.move(descripcion, archivo_ruta)
            except:
                print()
                print("el archivo ya existe")

            generar_mensaje(correo_recibido,servicio,flag,booleano)

            #pasar cosas a gonza y enviar mensaje de confirmacion

            lista.append( ruta_zip ) 
            print(lista)
            
            OS = generador_carpetas.platform.system()
           
            path = generador_carpetas.generador_ruta_base(OS) 
            print("path: ",path)
            generador_carpetas.crear_carpetas(lista,ruta_evaluaciones)

        if booleano == False:
            #print("el mail no es correcto")
            generar_mensaje(correo_recibido,servicio,flag,booleano)

    elif flag == False:     
        #messages = serviciousers().messages().get(userId = 'me').execute()
        booleano = False
        generar_mensaje(correo_recibido,servicio,flag,booleano)
        #print("el asunto del mail fue enviado incorrectamente")

def recibir_archivos(servicio : dict,correo : str, alumnos : dict , recibidos : dict, archivo_ruta : str, ruta_evaluaciones : str)->None:
    """
    pre : recibe el servicio de gmail, el ID del correo a evaluar, la lista de alumnos cursantes, un diccionario con los mail recibidos de INBOX, y 2 str 
    representando la carptea ruta de los zip y de las evaluaciones respectivamente

    post : en caso de ser un mail que sea de evaluacion del respectivo trabajo, se mandara a evaluar su formato, en caso de no ser parte de la evaluacion, se ovbiara
    """

    correo_recibido = servicio.users().messages().get(userId = 'me', id = correo).execute()
    nombre = correo_recibido["payload"]["headers"][19]["value"]

    lista = nombre.split("-")
    if len(lista) == 2:
        codeo = lista[0]
        padron = codeo.strip()
        if padron.isnumeric():
            guardar_archivo(correo_recibido,padron,alumnos,servicio,recibidos,lista,archivo_ruta,ruta_evaluaciones)
        else:
            print("no sirve tampoco")

    else:
        print("no sirve")

def inicio_gmail():
    
    archivo_ruta = generador_carpetas.generador_carpeta_zip()

    ruta_evaluacion = generador_carpetas.carpeta_evaluaciones()

    alumnos = evaluar_alumnos()  

    servicio = gmail.obtener_servicio()

    #https://gmail.googleapis.com/gmail/v1/users/{userId}/labels

    #labels = servicio.users().labels().get(userId = 'me', id = "INBOX").execute()

    recibidos = servicio.users().messages().list(userId = 'me', labelIds = "INBOX", maxResults = 500).execute()#,q = "after : 1624987804 before : 1626030000" 

    identificados = detectar_gmails(recibidos)

    for correo in identificados:
        recibir_archivos(servicio,correo,alumnos,recibidos,archivo_ruta,ruta_evaluacion)
    
