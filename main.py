""" Weather App """

import requests
import config

BASE_URL = "http://api.weatherapi.com/v1/"
JSON_TYPE = "current.json?"
CITY = "&q=London"
AQI_YES = "&aqi=yes"

FINAL_URL = BASE_URL + JSON_TYPE + "key=" + config.API_KEY + CITY + AQI_YES


def user_input():
    """ Function for User Input"""
    user_input_string = input("Check weather: ")
    return user_input_string

def request_data():
    """ Function for requesting weather data"""
    response = requests.get(FINAL_URL, timeout=10)
    return response.json()

if __name__ == "__main__":
    print(request_data())
