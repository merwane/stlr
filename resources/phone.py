from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from config import ACCOUNT_SID, AUTH_TOKEN, PHONE_NUMBER 

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_msg(body, to):
    try:
        message = client.messages.create(body=body, from_=PHONE_NUMBER, to=to)
        success = True
    except TwilioRestException:
        success = False
    return success
