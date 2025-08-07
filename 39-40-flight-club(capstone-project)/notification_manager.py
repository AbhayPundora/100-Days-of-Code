import  os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.account_sid = os.getenv("TWILIO_ACCOUNT_SID")

    def compare_price(self, sheet_data, fetched_data):
        for city in sheet_data:
            i = 0
            if str(fetched_data[i]["lowest_price"]) == "N/A":
                i += 1
                continue
            if city["lowestPrice"] < fetched_data[i]["lowest_price"]:
                self.send_notification(
                    lowest_price=fetched_data[i]["lowest_price"],
                    origin = fetched_data[i]["origin"],
                    destination=fetched_data[i]["destination"],
                    out_date = fetched_data[i]['out_date'],
                    return_date = fetched_data[i]['return_date']

                )
                i += 1

    def send_notification(self, lowest_price, origin, destination, out_date, return_date):
        client = Client(self.account_sid, self.auth_token)

        message = client.messages.create(
            to="+91902769915",
            from_="+18623782981",
            body=f"Low price alert! Only ₹ {lowest_price} to  fly from  {origin} to {destination}, on {out_date} to {return_date}")

        print(message.status)
