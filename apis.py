import requests

# Replace with your actual API key
api_key = "a2d57de4b3a509697a9b52fd8ca96828"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name: ")
complete_url = f"{base_url}appid={api_key}&q={city_name}"

response = requests.get(complete_url)
data = response.json()

if data["cod"] != "404":
    main_info = data["main"]
    current_temperature = main_info["temp"]
    current_pressure = main_info["pressure"]
    current_humidity = main_info["humidity"]
    weather_description = data["weather"][0]["description"]

    print(f"Temperature: {current_temperature} K")
    print(f"Atmospheric pressure: {current_pressure} hPa")
    print(f"Humidity: {current_humidity}%")
    print(f"Description: {weather_description}")
else:
    print("City not found")
