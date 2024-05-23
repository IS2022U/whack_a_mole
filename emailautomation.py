import os
import smtplib 
#SIIMPLE MAIL TRANSFER PROTOCOL#server create garna parxa ani port create garna parxa 
from email.mime.text import MIMEText
import getpass #mailpassword lukauna 

email_sender="kan078bct035@kec.edu.np"
email_password=getpass.getpass(prompt="Kantipur@123")
email_reciever="kan078bct003@kec.edu.np"
body="hello aadii.probablity ma nasikako haina???"
mail=MIMEText(body)
mail['From']=email_sender
mail['To']=email_reciever
mail['Subject']="Test Mail"
with smtplib.SMTP("smtp.gmail.com",587) as smtp:
    smtp.starttls()
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_reciever,mail.as_string)
    print(f"Mail sent to {email_reciever}")
    print("done")





























