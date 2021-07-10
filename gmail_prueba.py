
import pickle
import shutil
import json
import csv
import os
import gmail
import base64

#GET https://www.googleapis.com/gmail/v1/users/me/messages?q=in:sent after:2014/01/01 before:2014/02/01

#https://gmail.googleapis.com/gmail/v1/users/{userId}/labels

#https://gmail.googleapis.com/gmail/v1/users/{userId}/messages

#https://gmail.googleapis.com/gmail/v1/users/{userId}/messages/{id}

#https://gmail.googleapis.com/gmail/v1/users/{userId}/messages/{messageId}/attachments/{id}

#https://www.googleapis.com/gmail/v1/users/me/messages?q=in:sent after:2014/01/01 before:2014/02/01

# ["123654 " , Nicolas Puccar]

servicio = gmail.obtener_servicio()

identificados = []

alumnos = {}

results = servicio.users().messages().list(userId = 'me',q="after:1624987804 before:1626030000").execute()

labels = results.get('messages', [])

if not labels:
    print('No labels found.')

else:
    for label in labels:
        identificados.append(label["id"])

for correo in identificados:
    correo_recibido = servicio.users().messages().get(userId = 'me', id = correo).execute()
    labels_2 = correo_recibido.get('messages', [])
    nombre = correo_recibido["payload"]["headers"][19]["value"]
    try:
        lista = nombre.split("-")
        prueba = lista[1]
    except:
        print("el mensaje no es correcto")
        print()
    else:
        codeo = lista[0]
        total = codeo.strip()
        mensaje_id = results["messages"][0]["id"]
        descripcion = correo_recibido["payload"]["parts"][1]["filename"]
        contenido_id = correo_recibido["payload"]["parts"][1]["body"]["attachmentId"]
        resultado_2 = servicio.users().messages().attachments().get(userId = 'me', messageId = mensaje_id, id = contenido_id ).execute()
        dato = resultado_2["data"]
        codigo = base64.urlsafe_b64decode(dato.encode('UTF-8'))
        with open(descripcion, 'wb') as f:
            f.write(codigo)
        try:
            shutil.move(descripcion, "archivos")
        except:
            print()
            print("el codigo ya existe")

        alumnos[total] = descripcion
print(alumnos)
