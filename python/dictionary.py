import requests

print("===== DIGITAL DICTIONARY =====")

word = input("Enter any English word: ")

url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("\nWord:", word)

    for meaning in data[0]["meanings"]:
        print("\nPart of Speech:", meaning["partOfSpeech"])

        for definition in meaning["definitions"]:
            print("Meaning:", definition["definition"])

            if "example" in definition:
                print("Example:", definition["example"])
else:
    print("Sorry! Meaning not found.")