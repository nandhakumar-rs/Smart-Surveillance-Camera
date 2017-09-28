import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os
import smtplib
def send_mail(email = "rsnk2013@gmail.com"):
    img_data = open("final.jpg", 'rb').read()
    msg = MIMEMultipart()
    from_email = "rrj8335@gmail.com"
    from_pass = "44201998"
    to_mail = email

    subject ="Security alert"
    # msg="someone arrijved"
    # message = MIMEText(msg)
    # img = MIMEText(msg,'html')
    msg['subject'] = subject
    msg['to'] = to_mail
    msg['from'] = from_email

    text = MIMEText("someone arrived")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename("final.jpg"))
    msg.attach(image)

    gmail = smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_pass)
    gmail.send_message(msg)

send_mail("rsnk2013@gmail.com")