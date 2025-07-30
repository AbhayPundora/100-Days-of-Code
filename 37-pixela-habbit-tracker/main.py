import requests
import datetime as dt

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

USERNAME = "pundora"
TOKEN = ""
GRAPH_ID = "graph1"

#creting user
user_params = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)


# #creating a new graph
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id":"graph1",
    "name":"Running Graph",
    "unit":"km",
    "type":"float",
    "color":"sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#
# #adding a pixel to the graph
ADD_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

# date = dt.datetime.now().date()
# print(date)

# 1 >>>>>
# formatted_date = "-".split(str(date))
# print(formatted_date)

# 2 >>>>>
# formatted_date = ""
# for word in str(date):
#     if word == "-":
#         pass
#     else:
#         formatted_date += word

# 3 >>>>>
today = dt.datetime.now()
formatted_date = today.strftime("%Y%m%d")

print(formatted_date)

pixel_data = {
    "date": formatted_date,
    "quantity":"10.7"
}

response = requests.post(url=ADD_PIXEL_ENDPOINT, json=pixel_data, headers=headers)
print(response.text)


# #update a pixel
date_to_update = "20250729"

UPDATE_DELETE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_update}"
update_pixel_data = {
    "quantity":"2.5"
}

response = requests.put(url=UPDATE_DELETE_PIXEL_ENDPOINT, json=update_pixel_data, headers=headers)
print(response.text)
#
# #delete a pixel
response = requests.delete(url=UPDATE_DELETE_PIXEL_ENDPOINT,headers=headers)
print(response.text)



