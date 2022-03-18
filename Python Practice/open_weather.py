import requests

def get_weather_description_and_temp():
    api_key = "68ee2e7da869076eff535a3a0bcdda6b"
    city = input("What city would you like to see the weather for?\n") # Retrieve city name weather is requested for.
    city = city.capitalize() # Capitalize the input provided by the users.
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"
    
    request = requests.get(url)
    json = request.json()
    
    description = json.get("weather")[0].get("description")
    feels_like = json.get("main").get("feels_like")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")
    
    return{"description": description,
        "feels_like": feels_like,
        "temp_max": temp_max,
        "temp_min": temp_min}

def main():
    weather_dict = get_weather_description_and_temp()
    print("Today's forecast is", weather_dict.get("description"))
    print("Today's temperature feels like", weather_dict.get("feels_like"))
    print("Today's low is", weather_dict.get("temp_min"))
    print("Today's high is", weather_dict.get("temp_max"))
    print("up your butt and tenblocks down")

main()