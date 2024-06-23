import requests
import json
import sqlalchemy as db
import pandas as pd
from datetime import datetime

# Replace with your actual OpenWeatherMap API key
api_key = '855c3c14556fa2b26cc1a1a9e4d9d5a6'
latitude = 37.7749
longitude = -122.4194
base_url = 'https://api.openweathermap.org/data/2.5/weather?'

def get_weather(api_key, lat, lon):
  complete_url = f"{base_url}lat={lat}&lon={lon}&appid={api_key}&units=metric"
  response = requests.get(complete_url)
  return response.json()

def weather_to_dataframe(weather_data):
  if 'main' in weather_data:
    current = weather_data['main']
    weather = current.get('weather', [{}])[0]

    data = {
        'temperature': [current.get('temp')],
        'pressure': [current.get('pressure')],
        'humidity': [current.get('humidity')],
        'weather_description': [weather.get('description')],
        'wind_speed': [weather_data['wind'].get('speed')],
        'time_of_report': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
    }
    df = pd.DataFrame.from_dict(data)
    return df
  else:
    raise ValueError("Weather data does not contain 'current' key")

if __name__ == '__main__':
  weather_data = get_weather(api_key, latitude, longitude)
    
  df = weather_to_dataframe(weather_data)
  
  engine = db.create_engine('sqlite:///weather_data.db')
  
  df.to_sql('weather', con=engine, if_exists='replace', index=False)
  
  with engine.connect() as connection:
    query_result = connection.execute(db.text("SELECT * FROM weather;")).fetchall()
    print(pd.DataFrame(query_result))
