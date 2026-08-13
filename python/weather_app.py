import requests


def get_weather(city):
    url = "https://wttr.in/" + city + "?format=j1"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print("Could not get weather information.")
            return

        data = response.json()

        current = data["current_condition"][0]

        temperature = current["temp_C"]
        feels_like = current["FeelsLikeC"]
        humidity = current["humidity"]
        description = current["weatherDesc"][0]["value"]
        wind_speed = current["windspeedKmph"]

        print("\n===== WEATHER INFORMATION =====")
        print("City:", city)
        print("Temperature:", temperature, "°C")
        print("Feels Like:", feels_like, "°C")
        print("Condition:", description)
        print("Humidity:", humidity, "%")
        print("Wind Speed:", wind_speed, "km/h")

    except requests.exceptions.RequestException as error:
        print("Connection error:", error)

    except (KeyError, IndexError):
        print("Could not understand the weather data.")


while True:

    print("\n==============================")
    print("       WEATHER APP")
    print("==============================")
    print("1. Check Weather")
    print("2. Exit")
    print("==============================")

    choice = input("Enter your choice: ")

    if choice == "1":
        city = input("Enter city name: ").strip()

        if city:
            get_weather(city)
        else:
            print("Please enter a city name.")

    elif choice == "2":
        print("Thank you for using Weather App!")
        break

    else:
        print("Invalid choice.")