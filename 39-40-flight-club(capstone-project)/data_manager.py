import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_PUT_ENDPOINT = "https://api.sheety.co/4da66501a9c088d32610d8321018f319/flightDeals/prices/"

# headers = {
#     "Authorization": os.getenv("BEARER_AUTH")
# }

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def set_iata_code(self, complete_flight_data):
        for city in complete_flight_data:
            body = {
                "price": {
                    "iataCode" : city["iataCode"]
                }
            }
            response = requests.put(url=F"{SHEETY_PUT_ENDPOINT}{city["id"]}", json=body)
            print(response.text)

