import smtplib
from email.mime.text import MIMEText

sender = 'daddymrrobot@gmail.com'
password = ''
receivers = ['daddymrrobot@gmail.com', 'aa20.iaboyte86@iespabloserrano.com']
body = 'Esto es un correo de prueba'

# Email format
msg = MIMEText(body, 'html')
msg['Subject'] = 'Pruebas'
msg['From'] = sender
msg['To'] = ','.join(receivers)

server = smtplib.SMTP_SSL(host= 'smtp.gmail.com', port= 465)
server.login(user=sender, password=password)
server.sendmail(sender, receivers, msg.as_string())
server.quit()