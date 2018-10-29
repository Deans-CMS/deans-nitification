'''
Written by Michelle Lim Shi Hui & Nicholas Phang
Dean's Crisis Management System - Notification Subsystem
For CZ3003 Software System Analysis & Design

Message Manager -
API Server that receives JSON requests through API endpoints & processes them
'''
from flask import Flask, request, Response
from datetime import datetime
#import report_generation
import facebook_client
import sms_client
import twitter_client
import json
#import email_client

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world!"

# JSON format: {"message" : string}
@app.route('/socialmessages/', methods=['POST'])
def post_social_message():
    data = request.get_json()
    message = data['message']
    print('Connecting to Twitter...')
    twitter_client.main(message)
    print('Connecting to Facebook...')
    facebook_client.main(message)
    json_response = {'result' : 'Success!', 'posted' : message}
    return Response(json.dumps(json_response), status=201, mimetype='application/json')

# JSON format: {"number" : string, "message" : string}
@app.route('/dispatchnotices/', methods=['POST'])
def post_dispatch_notice():
    data = request.get_json()
    number = data['number']
    message = data['message']
    print('Connecting to Twilio...')
    sms_client.main(number, message)
    json_response = {'result': 'Success!', 'sent_to': number, 'posted': message}
    return Response(json.dumps(json_response), status=201, mimetype='application/json')

'''
# JSON format: {"email" : email address, 'cases' : [ {'time' : time, 'location' : location, 'type' : type, 'status' : string, 'resolved_in' : double},...]
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
    app.run(host='localhost', port=8000, debug=True)