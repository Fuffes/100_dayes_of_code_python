from twilio.rest import Client
import os
from dotenv import load_dotenv


load_dotenv()

def send_alert(message):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_="+17623713261",
        to="+375295401927",
    )

    print(message.status)