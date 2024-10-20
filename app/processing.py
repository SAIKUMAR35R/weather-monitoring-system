import pandas as pd # type: ignore

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def process_weather_data(data):
    processed_data = []
    for city, weather in data.items():
        temp_celsius = kelvin_to_celsius(weather['temp'])
        feels_like_celsius = kelvin_to_celsius(weather['feels_like'])
        processed_data.append({
            'city': city,
            'main': weather['main'],
            'temp': temp_celsius,
            'feels_like': feels_like_celsius,
            'timestamp': weather['dt']
        })
    return pd.DataFrame(processed_data)

def calculate_daily_aggregates(df):
    daily_summary = df.groupby('city').agg({
        'temp': ['mean', 'max', 'min'],
        'main': lambda x: x.mode()[0]  # Dominant weather condition
    }).reset_index()
    return daily_summary
