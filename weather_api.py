import requests
import json
from datetime import datetime

# Replace with your actual OpenWeatherMap API key
api_key = '855c3c14556fa2b26cc1a1a9e4d9d5a6'
latitude = 37.7749
longitude = -122.4194
base_url = 'https://api.openweathermap.org/data/2.5/weather?'

def get_weather(api_key, lat, lon):
  complete_url = f"{base_url}lat={lat}&lon={lon}&appid={api_key}&units=imperial"
  response = requests.get(complete_url)
  return response.json()

if __name__ == '__main__':
  weather_data = get_weather(api_key, latitude, longitude)

  current = weather_data['main']
  weather = weather_data.get('weather', [{}])[0]

  temperature = current.get('temp', 'N/A')
  pressure = current.get('pressure', 'N/A')
  humidity = current.get('humidity', 'N/A')
  weather_description = weather.get('description', 'N/A')
  wind_speed = weather_data['wind'].get('speed', 'N/A')
  
  print(f"City: San Francisco")
  print(f"Temperature: {temperature}°C")
  print(f"Pressure: {pressure} hPa")
  print(f"Humidity: {humidity}%")
  print(f"Weather Description: {weather_description.capitalize() if weather_description != 'N/A' else 'N/A'}")
  print(f"Wind Speed: {wind_speed} m/s")
  print(f"Time of Report: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
