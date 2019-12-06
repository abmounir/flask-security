import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from random import seed
from random import randint
from validate_email import validate_email
from securité.captchacreater import create_image_captcha
from securité import TokenGenerator


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

    msg.attach(MIMEText(message, 'html'))

    # the image is in the current directory
    x = str(TokenGenerator.getTokenUser(sendTo))
    fp = open(create_image_captcha(x), 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<token>')
    msg.attach(msgImage)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, sendTo, text)
    server.quit()


#sendMail("mehdidouy@gmail.com", 'Math problem', ms)
