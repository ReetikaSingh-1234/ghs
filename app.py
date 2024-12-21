import json
from flask import Flask,render_template,request
from flask_mail import Mail, Message

app = FLask(__name__)

#configuration for email server
app.config['MAIL-SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['mail_username'] = 'r75073868@gmail.com'
app.config['MAIL_PASSWORD'] = 'usyp qsrl lcnz zthk'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

#create email instance
mail = Mail(app)

#make routes
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/send_email',methods=[""])
def send_email():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']
    msg = Message(subject=subject, sender=email, recipients=['your email id'])
    msg.body = message
    mail.send(msg)
    return 'Email sent Successfully'


if __name__ == '__main__':
    app.run(debug=True)

