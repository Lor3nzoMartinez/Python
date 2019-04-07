import os
import smtplib
import imghdr
from email.message import EmailMessage

# to setup local port use command:
# python -m smtpd -c DebuggingServer -n localhost:1025

db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')

files = ['char.png']

msg = EmailMessage()
msg['Subject']  = 'Someone may have used python to send this message'
msg['From']     = db_user
msg['To']       = 'lorenzo651@live.com'
msg.set_content('I attached Things...')
msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype='html')

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    # msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(db_user, db_pass)
    smtp.send_message(msg)


print("Finished")
