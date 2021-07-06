import gmail

servicio = gmail.obtener_servicio()

#https://gmail.googleapis.com/gmail/v1/users/{userId}/labels

#https://gmail.googleapis.com/gmail/v1/users/{userId}/messages

#https://gmail.googleapis.com/gmail/v1/users/{userId}/messages/{id}

#https://gmail.googleapis.com/gmail/v1/users/{userId}/messages/{messageId}/attachments/{id}

identificados = []

results = servicio.users().messages().list(userId = 'me').execute()

labels = results.get('messages', [])

if not labels:
    print('No labels found.')

else:
    print('Labels:')
    for label in labels:
        identificados.append(label["id"])

resultado = servicio.users().messages().get(userId = 'me', id = identificados[0]).execute()

labels_2 = resultado.get('messages', [])

if not labels:
    print('No labels found.')

"""
else:
    print('Labels:')
    for label in labels:
        print(label['id'])

for i in range(len(results["messages"])):
    print(results["messages"][i])
    identificados.append(results["messages"][i]["id"])
"""

print(resultado["payload"]["headers"][6]["value"])
print(resultado["payload"]["headers"][19]["value"])

poema = resultado["payload"]["parts"][1]["filename"]
print(poema)
mensaje_id = resultado["payload"]["headers"][18]["value"]

resultado_2 = servicio.users().messages().get(userId = 'me', messageId = mensaje_id, Id = identificados[0] ).execute()
print(resultado_2)