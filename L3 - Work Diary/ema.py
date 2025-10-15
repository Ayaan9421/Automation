# import the Libs
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from smtplib import SMTP
from time import sleep
from dotenv import load_dotenv
from datetime import datetime
from email.mime.base import MIMEBase
from email import encoders

load_dotenv()

def send_email(filename):
        # email creds
        sen = os.getenv("EMAIL")
        sp = os.getenv("APP_PASSWORD")

        # compose email
        msg = MIMEMultipart()
        msg['From'] = sen
        rec = 'ayaantemp9421@gmail.com'
        msg['To'] = rec
        sub = "Testing"
        msg['Subject'] = sub

        body = "Testing"

        # Attact Text Body
        msg.attach(MIMEText(body, 'plain'))

        # attach files 
        if os.path.exists(filename):
                with open(filename, 'rb') as f:
                        part = MIMEBase("application", 'octet-stream')
                        data = f.read()
                        part.set_payload(data)
                        encoders.encode_base64(part)
                        part.add_header('Content-Disposition', "attachment;filename="+ os.path.basename(filename))
                        msg.attach(part)
        else: 
                print("no file found ...sending without attachment")

        # send email 
        try:
                with  SMTP("smtp.gmail.com", 587) as server:
                        server.starttls()
                        server.login(sen,sp)
                        server.sendmail(sen, rec, msg.as_string())
                        print("Email sent")
                
        except Exception as e:
                print("Issues: ", e)
