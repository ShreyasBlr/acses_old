import get_email, time

print('Log in to your email account here')
email_id = input('Enter your email id: ')
pwd = input('Enter password: ')
loop = True

while(loop):
    get_email.get_mail(email_id, pwd)
    time.sleep(30)
