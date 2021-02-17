from twilio.rest import Client
from PopularPackages.config import account_sid, auth_token

client = Client(account_sid, auth_token)

client.messages.create(
    to="+16123230029",
    from_="+15022375417",
    body="sent from python"
)
