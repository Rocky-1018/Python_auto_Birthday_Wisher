import os
from email.message import EmailMessage
import ssl
import smtplib

def mail(Subject,body):
    sender_id='strava.gaming@gmail.com'
    receiver_id='bethiprashanth87@gmail.com'
   password='onlyynkwwtuvemtn'
password='Rocky@1999$'
    em=EmailMessage()
    em['from']=sender_id
    em['to']=receiver_id
    em['subject']=Subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_id, password)
        server.sendmail(sender_id, receiver_id,em.as_string())
    return 0

