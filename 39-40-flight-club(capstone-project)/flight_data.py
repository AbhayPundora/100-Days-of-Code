import os
import requests
from dotenv import load_dotenv

load_dotenv()

SHEETY_GET_ENDPOINT = "https://api.sheety.co/4da66501a9c088d32610d8321018f319/flightDeals/prices"

headers = {

}

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.flight_data = []

    def fetch_flight_data(self):
        response = requests.get(url=SHEETY_GET_ENDPOINT, headers=headers)
        print(response.json())
        self.flight_data = response.json()["prices"]

    def check_flight(self, data, origin_code, des_code):
        flight_data_for_notification = ""
        if not data.get("data"):
            print("No flight data available.")
            flight_data_for_notification = {
                "lowest_price": "N/A",
                "origin": "N/A",
                "destination": "N/A",
                "out_date": "N/A",
                "return_date": "N/A",

            }
        try:
            first_flight = data['data'][0]
            lowest_price = float(first_flight["price"]["grandTotal"])

            nr_stops = len(first_flight["itineraries"][0]["segments"]) - 1

            dep = first_flight["itineraries"][0]["segments"][0]["departure"]

            origin = origin_code
            destination = first_flight["itineraries"][0]["segments"][nr_stops]["arrival"]["iataCode"]

            out_date = dep["at"].split("T")[0]

            return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

            print(f"{origin} ➡ {destination} | ₹{lowest_price} | {out_date} → {return_date}")

            flight_data_for_notification = {
                "lowest_price": lowest_price,
                "origin": origin,
                "destination": destination,
                "out_date": out_date,
                "return_date": return_date,

            }


        except (KeyError, IndexError) as e:
            print("Error parsing flight data:", e)


        finally:
            return flight_data_for_notification


