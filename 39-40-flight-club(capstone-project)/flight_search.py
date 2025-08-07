import os
from dotenv import load_dotenv
import requests
import datetime as dt
from flight_data import FlightData
import json

load_dotenv()

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_OFFER_SEARCH_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
     self.complete_data = []
     self._api_key = os.getenv("AMADEUS_API_KEY")
     self._api_secret = os.getenv("AMADEUS_API_SECRET")
     self._token = self._get_new_token()

    def set_flight_data(self, flight_data):
        for city in flight_data:
            params = {
                "keyword": city["city"]
            }
            headers = {"Authorization": f"Bearer {self._token}"}

            response = requests.get(url=IATA_ENDPOINT, params=params, headers=headers)
            # print(response.json())

            code = response.json()["data"][0]["iataCode"]
            city["iataCode"] = code
            self.complete_data.append(city)

    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        print(response.json())
        return response.json()["access_token"]


    def search_cheapest_flight(self):
        origin_location_code = "PAR"
        tomorrow = dt.datetime.now() + dt.timedelta(days=1)
        six_month_from_today = dt.datetime.now() + dt.timedelta(days=(6 * 30))
        check_flight_data = []
        # print(origin_location_code)
        for city in self.complete_data[1:]:
            destination_location_code = city["iataCode"]
            # print(destination_location_code)
            params = {
                "originLocationCode": origin_location_code,
                "destinationLocationCode": destination_location_code,
                "departureDate": tomorrow.strftime("%Y-%m-%d"),
                "returnDate": six_month_from_today.strftime("%Y-%m-%d"),
                "adults" :1,
                "nonStop": "true",
                "currencyCode": "GBP",
                "max": "10",

            }

            headers = {"Authorization": f"Bearer {self._token}"}

            response = requests.get(url=FLIGHT_OFFER_SEARCH_ENDPOINT, params=params, headers=headers)
            # print(json.dumps(response.json()))
            data = response.json()

            flight_data = FlightData()
            check_flight_data.append(flight_data.check_flight(data,origin_location_code, destination_location_code))
            print(check_flight_data)

        return check_flight_data


        # obj = FlightSearch()
# print(obj.set_flight_data())