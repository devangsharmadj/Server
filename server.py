from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<page_name>')
def works(page_name='index.html'):
    return render_template(page_name)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.form.to_dict()
        email = EmailMessage()
        email['from'] = data['name']
        email['subject'] = data['subject']
        email['to'] = 'devangsharmadj@gmail.com'
        email.set_content(data['message'])
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()

            smtp.send_message(email, data['email'])


