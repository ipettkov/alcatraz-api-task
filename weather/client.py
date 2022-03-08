import pytest
import requests

API_KEY = "08f86f73fb82f39bab545fc122868405"
BASE_URI = "https://api.openweathermap.org/data/2.5/weather"
KELVIN = 273.15


def get_city_temp_code(city_to_check: list):
    city_and_code = {}
    city_and_temp = {}

    for index, city in enumerate(city_to_check):
        json_resp = requests.get(f"{BASE_URI}?q={city.capitalize()}&appid={API_KEY}").json()
        city_and_code[json_resp["name"]] = json_resp["sys"]["country"]
        city_and_temp[json_resp["name"]] = json_resp["main"]["temp"]

    return city_and_code, city_and_temp
