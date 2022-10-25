import requests
import datetime

TOKEN = "qwertyuiop"
USER_NAME = "balaganesh"
pixela_end_point = "https://pixe.la/v1/users"
GRAPH_ID="graph1"
user_parameters = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# create A user account
# response = requests.post(url=pixela_end_point, json=user_parameters)
# print(response.text)
headers = {
    'X-USER-TOKEN': TOKEN
}
graph_endpoint = f"{pixela_end_point}/{USER_NAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "my reading graph",
    "unit": "number",
    "type": "int",
    "color": "sora",
}

# response = requests.post(url=graph_endpoint, json=graph_config,headers=headers)
# print(response.text)
today=datetime.datetime.now()

DATE=today.strftime("%Y%m%d")


data_entry = {"date": DATE,
              "quantity": input("how many pages have you read today??:")

              }


pixela_creation_endpoint=f"{pixela_end_point}/{USER_NAME}/graphs/{GRAPH_ID}"
response = requests.post(url=pixela_creation_endpoint, json=data_entry, headers=headers)
print(response.text)

## update a pixel

# pixela_update_endpoint=f"{pixela_end_point}/{USER_NAME}/graphs/{GRAPH_ID}/{DATE}"
# update_data={"quantity": "15"}
# response=requests.put(url=pixela_update_endpoint,json=update_data,headers=headers)
# print(response.text)

# # delete a pixel
# pixela_delete_endpoint=f"{pixela_end_point}/{USER_NAME}/graphs/{GRAPH_ID}/{DATE}"
# response=requests.delete(url=pixela_delete_endpoint,headers=headers)
# print(response.text)
