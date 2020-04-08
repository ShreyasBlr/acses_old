import smtplib, ssl, pymysql
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 

def send_mail(sender_id, sender_pwd, reciver_id, intent, confidence, subject, body):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = sender_id
    password = sender_pwd
    csr_email = "sumedhascadiga@gmail.com"
    customer_email = reciver_id

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
        message["To"] = customer_email
        message.attach(MIMEText(response, "plain"))
        
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, customer_email, message.as_string())
        except:
            print("Failed to send response") 

        response_query = ("INSERT INTO attended_emails VALUES (NULL,'"+customer_email+"','"+subject+"','"+body+"','"+intent+"')")
        cursor.execute(response_query)
        db.commit()
          
    else:
        original_msg = MIMEMultipart("alternative")
        original_msg["Subject"] = "Could not generate response"
        original_msg["To"] = csr_email
        fwd_msg = """\
            <html>
                <body>
                    <h2>Customer requested support</h2>
                    <hr>
                    <table>
                        <tr>
                            <td><h3><b>From:</b></h3></td>
                            <td><h3>"""+customer_email+"""</h3></td>
                        </tr>
                        <tr>
                            <td><h3><b>Subject:</b></h3></td>
                            <td><h3>"""+subject+"""</h3></td>
                        </tr>
                        <tr>
                            <td><h3><b>Message:</b></h3></td>
                            <td><h3>"""+body+"""</h3></td>
                        </tr>
                    </table>
                </body>
            </html>
            """
        original_msg.attach(MIMEText(fwd_msg, "html"))

        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, csr_email, original_msg.as_string())
        except:
            print("Failed to send email")

        forward_query = ("INSERT INTO forwarded_emails VALUES (NULL,'"+customer_email+"','"+subject+"','"+body+"')")
        cursor.execute(forward_query)
        db.commit()
        