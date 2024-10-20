import requests # type: ignore
from config.config import API_KEY, CITIES

def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()

def get_weather_data():
    weather_data = {}
    for city in CITIES:
        data = fetch_weather_data(city)
        weather_data[city] = {
            'main': data['weather'][0]['main'],
            'temp': data['main']['temp'],  # in Kelvin
            'feels_like': data['main']['feels_like'],
            'dt': data['dt']
        }
    return weather_data
