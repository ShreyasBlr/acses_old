import imaplib, email
import send_email as se
import intent_classification as ic

def get_mail(user, pwd):
    # user = "projectacses@gmail.com"
    # pwd = "acses@1920"
    imap_url = "imap.gmail.com"

    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user,pwd)

    con.select("inbox")
    result,data = con.search(None, "Unseen")

    inbox_item_list = data[0].split()
    if inbox_item_list:
        # latest_mail = inbox_item_list[-1]
        for mail in inbox_item_list:
            status,email_data = con.fetch(mail,'(RFC822)')

            raw_email = email_data[0][1].decode("utf-8")
            message = email.message_from_string(raw_email)

            def get_body(msg):
                if msg.is_multipart():
                    return get_body(msg.get_payload(0))
                else:
                    return msg.get_payload(None,True)

            body = get_body(message)

            msg_body = body.decode('utf-8')
            # print("From:", message['From'])
            # print("Subject:", message['Subject'])
            # print("Body:", msg_body)
            # print("\n <---------------------- Mail Read --------------------> \n")
            classified_result = ic.classify_intent(msg_body)
            se.send_mail(user,pwd,message['From'],classified_result['intent'],classified_result['confidence'], message['Subject'],msg_body)
    else:
        print("No unread emails")