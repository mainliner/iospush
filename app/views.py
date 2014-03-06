from app import app, db
from apns import APNs, Payload
from flask import render_template, flash, redirect, request

import os
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/send',methods=['GET','POST'])
def send():
    #if request.method == 'GET':
    #    return render_template('send.html') 
    certfile= os.path.abspath(os.path.dirname(__file__))+ '/PushChatCert.pem'
    keyfile= os.path.abspath(os.path.dirname(__file__))+ '/PushChatkey2.pem'
    apns = APNs(use_sandbox=True, cert_file=certfile, key_file=keyfile)
    # Send a notification
    token_hex = '5315b5bdabc6b9da640e7103200e83b0126904cf3b26ed00498797ddb34e3f06'
    payload = Payload(alert="Hello World!", sound="default", badge=1,custom={'url':'http://ddd.d.com'})
    apns.gateway_server.send_notification(token_hex, payload)
    #for (token_hex, fail_time) in apns.feedback_server.items():
    #    return "send successful" + str(fail_time)
    return "successful"