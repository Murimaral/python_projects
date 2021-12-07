#!/usr/bin/env python3

from email.message import EmailMessage
import os
import mimetypes

### Setting variables
sender = 'fufiauau@hotmail.com'
recipient = 'murimaral@gmail.com'
subject = "Greetings from {} to {}!".format(sender, recipient)
### Instantiating EmailMessage object
message = EmailMessage()

### Adding variable values to message fields
### From, To, and Subject are examples of email header fields
message['From'] = sender
message['To'] = recipient
message['Subject'] = subject

### Setting and adding content to the BODY
body = """Hey there!!

  I'm learning how to send emails with Python!!!"""
message.set_content(body)

### Attach
### Setting attachment path
attachment = os.path.abspath('./image.jpeg')

### Get mime type and subtype of the attachment
mime_type = mimetypes.guess_type(attachment)
m_type, m_subtype = mime_type[0].split('/')

### ATTACH TO BODY by opening and reading in BINARY MODE
with open(attachment, 'rb') as att:
  message.add_attachment(att.read(),
                         maintype = m_type,
                         subtype = m_subtype,
                         filename = os.path.basename(attachment))
### Show message object contents
# print(message)

### INITIALIZING SMTP SERVER
import getpass     ### classe para receber input secreto 
import smtplib     ### inicia servidor de email e envia
host =  'smtp.office365.com'
port = 587
login = input("Por favor insira seu hotmail:\n")
password = getpass.getpass('Password? ')
### inicia o servidor
server = smtplib.SMTP(host, port)

### login no email inputado
### antes do login deve ser atendida às condiçoes de autenticaçao do servidor (hotmail) usando 
### nesse caso as funçoes ehlo() e starttls() 
#server.ehlo()
server.starttls() 
server.login(login, password)


### ENVIO DO EMAIL
server.send_message(message)
### retorna um dicionario dos usuarios dos recipients que NAO RECEBERAM A MSG
### Terminado o processo DESLOGAR DO SERVIDOR
server.quit()
