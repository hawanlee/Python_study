from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACf99fc8d5d78e059d5061ecdb8e7d552b"
# Your Auth Token from twilio.com/console
auth_token  = "f40f90971f2092513ed4d21490619e73"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+8617612167996", 
    from_="+15108903403",
    body="You are so Niubi! - From Laden")

print(message.sid)