import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

account_sid = os.getenv("ACCOUNT_SID")
auth_token  = os.getenv("AUTH_TOKEN")

# print(api_key)
# print(auth_token)


MY_LAT = 30.392500
MY_LNG = 78.092201

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": api_key,
    "cnt": 4,

}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
print(response.status_code)
print(response.json())

weather_data_list = response.json()["list"]

# weather_id = response.json()["list"][0]["weather"][0]["id"]
# weather_description = response.json()["list"][0]["weather"][0]["description"]
# print(weather_id, weather_description)

condition_code_list = []
for item in weather_data_list:
    id = item["weather"][0]["id"]
    if id < 700:
        condition_code_list.append(id)

#list comprehension:
condition_code_list2 = [item["weather"][0]["id"] for item in weather_data_list if item["weather"][0]["id"] < 700]

if len(condition_code_list) > 0:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+919027606415",
        from_="+18623782981",
        body="It's going to rain today! Remember to bring an umbrella ☂ ️")

    print(message.status)



# print(condition_code_list)
# print(condition_code_list2)