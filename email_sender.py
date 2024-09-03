import smtplib
import ssl
import os


def send_mail(sender, topic, message):

    host = "smtp.gmail.com"
    port = 465

    passkey = os.getenv("GMAIL_APP_PASS")
    username = "svetlin.sii@gmail.com"

    receiver = "svetlin.sii@gmail.com"
    message_to_send = f'''Subject:{topic}
from {sender}
{message}
'''
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:

        server.login(username, passkey)
        server.sendmail(username, receiver, message_to_send.encode('utf8'))
