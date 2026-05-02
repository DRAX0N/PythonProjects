import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "draxon"
TOKEN = "123vhcjdsxv2134bj3bdwejk12endalsxnck12e"
graphID = "graph1"
graph_name = "Learning Graph"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create User
# response = requests.post(url=pixela_endpoint, json=user_params)
#
# print(response.text)

# Create graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": graphID,
    "name": graph_name,
    "unit": "h",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Crate Post
post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graphID}"

today = datetime(year=2020, month=1, day=27)
# today = datetime.now()
# print(today.strftime("%Y%m%d"))
post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3.6",
}

# response = requests.post(url=post_endpoint, json=post_config, headers=headers)
# print(response.text)

# Update
new_date = today.strftime("%Y%m%d")
put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graphID}/{new_date}"
put_config = {
    "quantity": "1",
}
# response = requests.put(url=put_endpoint, json=put_config, headers=headers)
# print(response.text)

# Delete
delete_date = today.strftime("%Y%m%d")
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graphID}/{delete_date}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
