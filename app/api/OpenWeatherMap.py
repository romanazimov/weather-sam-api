import os
import request

API_KEY = os.environ.get('weatherApiKey')

def get_weather_data(latitude, longitude):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    endpoint = f"{base_url}?lat={latitude}&lon={longitude}&appid={API_KEY}&units=imperial"
    results = requests.get(endpoint)
    return results['main']