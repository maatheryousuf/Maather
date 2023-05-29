from bs4 import BeautifulSoup
import requests
import json
import re

def scrape_weather():
    location = input("Enter City name")
    
    base_url = "https://weather.com/?Goto=Redirected"
    search_url = base_url + "/locations/" + location.replace("", "-")
    
    
    response = requests.get(search_url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.content, "html parser")
    
    forecast = soup.find("span", class_="phrase").text.strip()
    
    script_tag = soup.find("script", text-re.compile(r"var metcastData"))
    
    humidity_match = re.search(r'"humidity":"(.*?)"', str(script_tag))
    humidity = humidity_match.group(1) if humidity_match else "N/A"
    
    wind_speed_match = re.search(r'"windSpeed10m":{.*?"text":"(.*?)"', str(script_tag))
    wind_speed = wind_speed_match.group(1) if wind_speed_match else "N/A"
    
    
    weather_data = {"Location": location, "Forecast": forecast,}
    
    with open("weather_data.json", "w") as json_file:
        json.dump(weather_data, json_file)
        
        
        print("Weather Information for", location)
        print("Fotrecast", forecast)
        print("Weather data has been saves to weather_data.json.")