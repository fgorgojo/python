# weatherService.py

import requests

class WeatherService:
    baseUrl = 'https://api.openweathermap.org/data/2.5'
    appId = '45b3eb2041f2907d2468147fdbe76d5b'

    @classmethod
    def getForecast(cls, city="new york", country="us"):
        url = f'{cls.baseUrl}/forecast'

        response = requests.get(url, params=[
            ('q', f'{city},{country}'),
            ('mode', 'json'),
            ('APPID', cls.appId)
            ])

        data = response.json()

        return data['list']

if __name__ == "__main__":
    print("Fetching weather forecast...")
    print(WeatherService.getForecast())