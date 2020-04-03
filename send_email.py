import smtplib, ssl, intent_classification

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "projectacses@gmail.com"  # Enter your address
password = "acses@1920"

replyData = intent_classification.mailInfo()
receiver_email = replyData['sender_address']  # Enter receiver address
intent = replyData['intent']

if intent == 'password_recovery':
    message = """\
Subject: Response from Acses

Follow the steps in the link to reset your password. \n www.google.com"""
else:
    message = "This is the default response"

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
print("Email Sent")