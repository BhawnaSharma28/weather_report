import requests
import os
from datetime import datetime

user_api = os.environ['weather']
location = input("Enter the City Name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
#complete api link
api_link = requests.get(complete_api_link)
api_data = api_link.json()

if api_data['cod'] == '404':
    print("Invalid City: {}, Please check your City Name".format(location))
else:
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %y | %I:%M:%S %p")

    print("------------------------------------------------------------")
    print("Weather Stats for = {} || {}".format(location.upper(),datetime))
    print("------------------------------------------------------------")

    print("Current temperature is: {:2f} deg C".format(temp_city))
    print("Current weather desc  :",weather_desc)
    print("Current Humidity      :",hmdt,"%")
    print("Current wind speed    :",wind_spd,'kmph')
