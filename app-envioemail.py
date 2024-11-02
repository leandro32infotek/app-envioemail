import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Informações do seu e-mail Yahoo
remetente = 'leandro32infotek@yahoo.com.br'
senha = 'tepbrndecyvohpoi'
destinatario = 'leandro32infotek@yahoo.com.br'

# Cria a mensagem
mensagem = MIMEMultipart()
mensagem['From'] = remetente
mensagem['To'] = destinatario
mensagem['Subject'] = 'Teste de envio de e-mail com Python'

# Corpo da mensagem
corpo = 'Este é um teste de envio de e-mail utilizando Python.'
mensagem.attach(MIMEText(corpo, 'plain'))

# Configurações do servidor SMTP do Yahoo
servidor_smtp = 'smtp.mail.yahoo.com'
porta = 587

# Conecta ao servidor SMTP e envia a mensagem
with smtplib.SMTP(servidor_smtp, porta) as server:
    server.starttls()
    server.login(remetente, senha)
    server.sendmail(remetente, destinatario, mensagem.as_string())
    print('E-mail enviado com sucesso!')