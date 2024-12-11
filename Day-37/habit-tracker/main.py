import requests

USERNAME = "brainy"
TOKEN = "weeewradfddfdr"

pixela_endpoint = "https://pixe.la/v1/users"
#
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
#
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "km",
    "type": "float",
    "color": "momiji",
}

graph_endpoint = f"/v1/{pixela_endpoint}/{USERNAME}/graphs"

response = requests.post(url=graph_endpoint, json=graph_config)
print(response.text)
