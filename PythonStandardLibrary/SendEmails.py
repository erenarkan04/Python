from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from string import Template
from pathlib import Path


template = Template(Path("template.html").read_text())

message = MIMEMultipart()
message["from"] = "eren"
message["to"] = "ahmeta04@gmail.com"
message["subject"] = "test"
body = template.substitute({"user": "John"})
message.attach(MIMEText(body, "html"))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("ahmetarkan0424@gmail.com", "pieguy521")
    smtp.send_message(message)
    print("message sent")