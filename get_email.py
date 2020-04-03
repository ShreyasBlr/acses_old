import imaplib, email

user = "projectacses@gmail.com"
pwd = "acses@1920"
imap_url = "imap.gmail.com"

con = imaplib.IMAP4_SSL(imap_url)
con.login(user,pwd)

con.select("inbox")
result,data = con.uid('search',None,"ALL")

inbox_item_list = data[0].split()
latest_mail = inbox_item_list[-1]

status,email_data = con.uid('fetch',latest_mail,'(RFC822)')

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
