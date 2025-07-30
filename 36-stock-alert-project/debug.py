from twilio.rest import Client

client = Client("AC209d36747005271e171c0e7db98e29d1", "9ee2efbf30fc34142b87884664fac061")

message = client.messages.create(
    body="Test SMS from Twilio",
    from_="+18623782981",
    to="+9190276488415"
)

print(message.sid)
print(message.status)
