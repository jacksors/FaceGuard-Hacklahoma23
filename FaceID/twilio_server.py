from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse
# from arduino import Arduino
import serial
from serial import SerialException
import time
import threading
import faceid
from arduino import Arduino

app = Flask(__name__)

@app.route('/', methods=['POST'])
def sms_reply():
    # Get the message text sent by the user
    message_text = request.form.get('Body')
    print(message_text)

    
    approved_senders = []
    
    if request.form.get('From') in approved_senders:
    
        if message_text.lower() == "unlock":
            print(Arduino.is_unlocked)
            try:
                if Arduino.is_unlocked:
                    resp = MessagingResponse()
                    resp.message(f"Already unlocked")
                    return str(resp)
                else:
                    resp = MessagingResponse()
                    resp.message(f"Unlocked")
                    t = threading.Thread(target=Arduino.unlock)
                    t.start()
                    return str(resp)
            except SerialException as e:
                print(e)
                resp = MessagingResponse()
                resp.message(f"Already unlocked")
                return str(resp)

if __name__ == '__main__':
    t = threading.Thread(target=faceid.stream)
    t.start()
    app.run(debug=True)
