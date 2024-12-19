from datetime import datetime

import requests

USERNAME = "brainy"
TOKEN = "weeewradfddfdr"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
#
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# CREATING A USER ON PIXELA
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# CREATING A GRAPH
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Coding Graph",
#     "unit": "km",
#     "type": "float",
#     "color": "momiji",
# }
#
headers = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# UPDATE A PIXEL TO GRAPH ON PIXELA

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10.20",
}
#
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)