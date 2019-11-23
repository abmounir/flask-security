import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from random import seed
from random import randint
from validate_email import validate_email


def validMail(mail):
    is_valid = validate_email(mail, verify=True)
    return is_valid


def sendMail(sendTo, subject, message):
    email = 'banktokensend@gmail.com'
    password = '1234ANANANAbank'

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = sendTo
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, sendTo, text)
    server.quit()
