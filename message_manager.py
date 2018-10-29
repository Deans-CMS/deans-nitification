'''
Written by Michelle Lim Shi Hui & Nicholas Phang
Dean's Crisis Management System - Notification Subsystem
For CZ3003 Software System Analysis & Design

Message Manager -
API Server that receives JSON requests through API endpoints & processes them
'''

from flask import Flask, jsonify, request
from datetime import datetime
# import reportgeneration
import facebook_client
import sms_client
import twitter_client
import email_client

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# JSON format: {'message' : string}
@app.route('/socialmessages/', methods=['POST'])
def post_social_message():
    data = request.get_json()
    message = data['message']
    print('Connecting to Twitter...')
    twitter_client.main(message)
    print('Connecting to Facebook...')
    facebook_client.main(message)
    return jsonify({'result' : 'Success!', 'posted' : message})

# JSON format: {'number' : string, 'message' : string}
@app.route('/dispatchnotices/', methods=['POST'])
def post_dispatch_notice():
    data = request.get_json()
    number = data['number']
    message = data['message']
    print('Connecting to Twilio...')
    sms_client.main(number, message)
'''

# JSON format: {'email' : email address,
@app.route('/reports/', methods=['POST'])
def generate_report():
    data = request.get_json()
    emailadd = data['email']
    subject = "Crisis Summary Report for" + #auto-generate
    report = report_generation.main(data)
    print('Connecting to Gmail...')
    email_client.main(emailadd, subject, report)
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)