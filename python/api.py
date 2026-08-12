import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:

    users = response.json()

    for user in users:
        print("Name:", user["name"])
        print("Email:", user["email"])
        print("City:", user["address"]["city"])
        print("--------------------")

else:
    print("Failed to get data.")
    print("Status Code:", response.status_code)