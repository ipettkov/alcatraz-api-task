import pytest
from client import get_city_temp_code
import pytest_check as check
from test_data import capitals_and_correct_code, cities_to_check

KELVIN = 273.15


class TestWeatherApi:
    def test_city_codes(self):
        cap_code, cap_temp = get_city_temp_code(cities_to_check)
        for city, code in cap_code.items():
            check.equal(capitals_and_correct_code[city], cap_code[city], f"Code for {city}'s country is not {code}")

    def test_city_temp_range(self):
        cap_code, cap_temp = get_city_temp_code(cities_to_check)
        for city, temp in cap_temp.items():
            check.is_true(-25 <= (temp - KELVIN) <= 40,
                          f"Temperature of {city} is {round(temp - KELVIN)} which is out of range (-25 +40)")
