from twilio.rest import Client

account_sid = 'AC08c3bbf6ad2d86160ab5b8bfe6a10bf5'
auth_token = '7d79e23c03f3ec56d0ec565d08918dc5'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Your appointment is coming up on July 21 at 3PM',
    to='whatsapp:+353833424734'
)

print(message.sid)