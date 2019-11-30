import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
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

    msg.attach(MIMEText(message, 'html'))

    # the image is in the current directory
    fp = open('captcha_4528.png', 'rb')
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


ms = """

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Message</title>
    <style>
        * {
            padding: 0;
            margin: 0;
            background-color: darkslategray;
            color: white;

        }

        .message {

            text-align: center;
        }
        .verify {
            margin:10px;
            border: none;
            background-color: cornflowerblue;
            color: black;
            border-radius: 5px;
        }

        img {
          margin-left: auto;
          margin-right: auto;
          display: block;
        }
        
    </style>
</head>

<body>
    <div class="message">
        <h3>Hello Mr : Insert name</h3>
        <br>
        <h4>This is your token </h4>
        <img src="cid:token">
        <br>
        <br>
        <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Vero veniam commodi .</p>
        <br>
        <br>
        <button class="verify">Verify my account</button>
    </div>


</body>

</html>
"""


sendMail("mehdidouy@gmail.com", 'Math problem', ms)
