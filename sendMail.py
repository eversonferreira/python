import smtplib
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

 
# create message object instance
msg = MIMEMultipart()
 
 
message = "Thank you"
 
# setup the parameters of the message
password = "meuPassword"
msg['From'] = "meueamail@dominio.com.br"
msg['To'] = "fulano@dominio.com.br"
msg['Subject'] = "Assunto da Mensagem"
 
# add in the message body
msg.attach(MIMEText(message, 'plain'))
 
#create server
server = smtplib.SMTP('smtp.servidor.com.br: 587')
 
server.starttls()
 
# Login Credentials for sending the mail
server.login(msg['From'], password)
 
 
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
