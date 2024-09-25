import requests

API_KEY = '3780b24b3d3e6a3188c8a4a95adf27ad'
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    request_url =  f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(request_url)
    
    if response.status_code == 200:
        data= response.json()
        
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        print(f"City: {city}")
        print(f"Temperature: {temp}°C")
        print(f"Weather: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("error")
        
city = input("Enter the city name: ")
get_weather(city)