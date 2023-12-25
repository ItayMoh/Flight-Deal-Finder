import os
from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = os.environ.get("ACCOUNT_SID")
        self.auth_token = os.environ.get("AUTH_TOKEN")
        self.client = Client(self.account_sid, self.auth_token)
        self.TWILIO_SENT_NUMBER = os.environ["TWILIO_SENT_NUMBER"]
        self.YOUR_NUMBER = os.environ["YOUR_NUMBER"]

    #Handles message sending to your number
    def send_msg(self,msg):
        message = self.client.messages.create(
             body=msg,
             from_=self.TWILIO_SENT_NUMBER,
             to=self.YOUR_NUMBER
         )