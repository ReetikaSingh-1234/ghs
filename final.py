import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = "r75073868@gmail.com"
sender_password = "yfqv dmfi hihy kixm"

server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
server.login(sender_email, sender_password)

receiver_emails = ["satyendrasingh.mkp@gmail.com"]
for receiver_email in receiver_emails:
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "hii mr. satyendra kumar singh"
    msg['From'] = sender_email
    msg['To'] = receiver_email
    html = """
        <h1>hello</h1>
    """
    msg.attach(MIMEText(html, 'html'))
    server.sendmail(sender_email, receiver_email, msg.as_string())

server.quit()