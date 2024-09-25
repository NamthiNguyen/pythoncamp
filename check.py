import requests
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv('API_KEY')
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    request_url =  f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(request_url)
    
    if response.status_code == 200:
        data= response.json()
        
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        windspeed = data['wind']['speed']
        
        print(f"City: {city}")
        print(f"Temperature: {temp}°C")
        print(f"Weather: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {windspeed} m/s")
    else:
        print("error")
        
city = input("enter your city name: ")
get_weather(city)