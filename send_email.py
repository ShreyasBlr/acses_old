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
            Password recovery response"""
        elif intent == 'order_status':
            message = """\
                Subject: Response from Acses
                Order Status response"""
        elif intent == 'cancel_order':
            message = """\
                Subject: Response from Acses
                Order Status response"""
        elif intent == 'create_account':
            message = """\
                Subject: Response from Acses
                Order Status response"""
        elif intent == 'delete_account':
            message = """\
                Subject: Response from Acses
                Order Status response"""
        elif intent == 'change_account':
            message = """\
                Subject: Response from Acses
                Order Status response"""
        elif intent == 'delivery_options':
            message = """\
                Subject: Response from Acses
                Order Status response"""
        elif intent == 'get_refund':
            message = """\
                Subject: Response from Acses
                Order Status response"""
        elif intent == 'payment_issue':
            message = """\
                Subject: Response from Acses
                Order Status response"""
        elif intent == 'payment_options':
            message = """\
                Subject: Response from Acses
                Order Status response"""
        elif intent == 'request_csr':
            message = """\
                Subject: Response from Acses
                Order Status response"""
        elif intent == 'review':
            message = """\
                Subject: Response from Acses
                Order Status response"""
        elif intent == 'shipping_address':
            message = """\
                Subject: Response from Acses
                Order Status response"""
        elif intent == 'update_profile':
            message = """\
                Subject: Response from Acses
                Order Status response"""
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        print("Email Sent")       
    else:
        print("Forward email to CSR")