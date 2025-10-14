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

# attach files 
filename = input("Enter filename: ")
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
       
da = input("Enter date (YYYY-MM-DD): ")
ti = input("Enter time (HH:MM, 24hr format): ")

st = datetime.strptime(da + " " + ti, "%Y-%m-%d %H:%M")

now = datetime.now()
delay = (st - now).total_seconds()

if delay <= 0:
        print("The scheduled time is in the past. Please choose a future time.")
        exit()

while delay > 0:
    print(f"\rTime left: {int(delay)} seconds", end="", flush=True)
    sleep(1)
    delay -= 1

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