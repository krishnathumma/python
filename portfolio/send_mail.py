import smtplib, ssl
import os

def send_mail(message):
    host = "smtp.gmail.com"
    port = 465

    username = "krishna.thumma9@gmail.com"
    password = os.getenv("PASSWORD")

    recevier = "psyennam@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, recevier, message)