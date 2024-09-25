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
        
        temp_Celsius= data['main']['temp']
          #chaning temperature to fahreniet and rounding it 
        temp_fahrenhiet = round(temp_Celsius *9/5) + 32
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        windspeed = data['wind']['speed']
        max_temp_Celsius  = data['main']['max_temp']
        #chaning mzc temperature to fahreniet and rounding it 
        max_temp_fahrenhiet = round(max_temp_Celsius *9/5) +32 
        min_temp_Celsius  = data['main']['min_temp']
        #chaning min temperature to fahreniet and rounding it 
        min_temp_fahrenhiet = round(min_temp_Celsius *9/5) +32 
        
        
        
        print(f"City: {city}")
        print(f"Temperature: {temp_fahrenhiet}°F")
        print(f"Weather: {description}")
        print(f'max temperature: {max_temp_fahrenhiet}')
        print(f"min temperature: {min_temp_fahrenhiet}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {windspeed} m/s")
        
    else:
        print("error")
        
city = input("enter your city name: ")
get_weather(city)