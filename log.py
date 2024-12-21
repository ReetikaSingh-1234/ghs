from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail= Mail(app)


with open('config.json','r') as f:
    params= json.load(f)['param']
#configuration for email server
app.config['MAIL-SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['mail_username'] = params['gmail.user']
app.config['MAIL_PASSWORD'] = params['gmail.password']
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

users=[{'name':'reetika','email':'reetikasingh003@gmail.com'}]

#create email instance
mail = Mail(app)


@app.route("/")
def index():
    return render_template('index.html')
#make routes
@app.route("/contact",methods=['POST'])
def contact():
    if request.method=="POST":
        name=request.form["name"]
        email=request.form["email"]
        subject=request.form["subject"]
        message=request.form["message"]
    msg=Message(subject,sender=email,recipients=['reetikasingh003@gmail.com'])
    msg.body=message
    
    mail.send(msg)       
    return "msg sent"



if __name__ == '__main__':
    app.run(debug=True)
