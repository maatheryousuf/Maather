import requests

API_Key = "9c11b2ad7a28a207e61ab63802244716"  

city_name = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}"

response = requests.get(url)

if response.status_code == 200:
    res = response.json()

    data = res["main"]
    live_temperature = data["temp"] - 273.15
    live_pressure = data["pressure"]
    humidity = data["humidity"]
    wind_speed = res["wind"]["speed"]
    desc = res["weather"]
    weather_description = desc[0]["description"]

    print("Temperature (in Celsius scale): " + str(live_temperature))
    print("Pressure: " + str(live_pressure))
    print("Humidity: " + str(humidity))
    print("Wind Speed: " + str(wind_speed))
    print("Description: " + str(weather_description))
else:
    print("Please enter a valid city name")