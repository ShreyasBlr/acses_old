import smtplib, ssl 

def send_mail(sender_id, sender_pwd, reciver_id, intent, confidence):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = sender_id
    password = sender_pwd

    receiver_email = reciver_id

    if confidence > 0.5:
        if intent == 'password_recovery':
            message = """\
            Subject: Response from Acses

            Follow the steps in the link to reset your password. \n www.google.com"""
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        print("Email Sent")       
    else:
        print("Forward email to CSR")