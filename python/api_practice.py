import requests

url = "https://dummyjson.com/quotes/random"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("Quote:", data["quote"])
    print("Author:", data["author"])

else:
    print("Failed to get quote.")