# import the Libs
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from smtplib import SMTP
from time import sleep
from dotenv import load_dotenv

load_dotenv()

# email creds
sen = os.getenv("EMAIL")
sp = os.getenv("APP_PASSWORD")

# compose email
msg = MIMEMultipart()
msg['From'] = sen
rec = input("Enter Receiver: ")
msg['To'] = rec
sub = input("Enter Subject: ")
msg['Subject'] = sub

body = input("Enter Email Body: ")

# Attact Text Body
msg.attach(MIMEText(body, 'plain'))

de = int(input("Enter delay time(sec): "))

for i in range(de):
        print("sending email after ", str(de - i - 1), " seconds \r",end="", flush=True)
        sleep(1)

print()

# send email 
try:
        with  SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sen,sp)
                server.sendmail(sen, rec, msg.as_string())
                print("Email sent")
        
except Exception as e:
        print("Issues: ", e)