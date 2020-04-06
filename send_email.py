import smtplib, ssl, pymysql
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 

def send_mail(sender_id, sender_pwd, reciver_id, intent, confidence, subject, body):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = sender_id
    password = sender_pwd

    receiver_email = reciver_id

    try:
        db = pymysql.connect(host='192.168.64.2',user='shreyas',passwd='Shreyas@1999',db='acses')
        cursor = db.cursor()
    except:
        print("Unable to connect to db")
        exit()

    if confidence > 0.5:
        query = ("select response from intent_response where intent='"+intent+"'")
        cursor.execute(query)
        for row in cursor:
            for value in row:
                response = value
        
        message = MIMEMultipart("alternative")
        message["Subject"] = "Response from customer support"
        message["From"] = sender_email
        message["To"] = receiver_email
        message.attach(MIMEText(response, "plain"))
        
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
        except:
            print("Failed to send response") 
        response_query = ("INSERT INTO attended_emails VALUES (NULL,'"+receiver_email+"','"+subject+"','"+body+"','"+intent+"')")
        cursor.execute(response_query)
        db.commit()
          
    else:
        forward_query = ("INSERT INTO forwarded_emails VALUES (NULL,'"+receiver_email+"','"+subject+"','"+body+"')")
        cursor.execute(forward_query)
        db.commit()
        print("Forward email to CSR")