from http.client import responses

import requests
import json
import datetime as dt


# Extracting relevant pieces of info from the input text
nuro_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nuro_headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}
user_input = input("Tell me which exercise you did?: ")

body = {
    "query": user_input,
}

response = requests.post(url=nuro_endpoint, headers=nuro_headers, json= body)
nuro_data = response.json()

today = dt.datetime.now()
formatted_date = today.strftime("%d/%m/%Y")
formatted_time = today.strftime("%H:%M:%S")

# adding data to our spreadsheet

headers = {
    "Authorization": f"Bearer {AUTH_HEADER}"
}

for new_data in nuro_data['exercises']:
    data = {
        "date": formatted_date,
        "time": formatted_time,
        "exercise": new_data['name'],
        "duration": new_data['duration_min'],
        "calories": new_data['nf_calories']

    }
    print(data)

    s_body =  {
            "workout": data
        }
    # sheety_endpoint = f'https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{exercises}'
    sheety_endpoint = "https://api.sheety.co/4da66501a9c088d32610d8321018f319/myWorkouts/workouts"

    res2 = requests.post(url=sheety_endpoint, json=s_body, headers=headers)
    print(res2.text)