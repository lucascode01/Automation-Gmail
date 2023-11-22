# Gmail
import smtplib
import email.message

def enviar_email():
    corpo_email = """
    <p>Olá </p>
    <p>Muito prazer </p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'lucassantoschaves369@gmail.com'
    msg['To'] = 'lucassantoschaves369@gmail.com,lucasdesigner808@gmail.com'
    password = 'dekwzglikkxnlrik' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    
    # Pass recipients as a list to sendmail
    s.sendmail(msg['From'], msg['To'].split(','), msg.as_string().encode('utf-8'))
    
    print('Email enviado')

enviar_email()
