import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather(lat: str, long: str) -> str or None:
    api_key = os.environ.get("WEATHER_API_KEY")
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={long}&appid={api_key}&exclude=minutely,hourly,daily"
    )
    return response.json()
