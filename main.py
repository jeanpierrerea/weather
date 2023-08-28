""" Weather App """

import requests
import config

BASE_URL = "http://api.weatherapi.com/v1/"
JSON_TYPE = "current.json?"
CITY = "&q=London"
AQI_YES = "&aqi=yes"

#final_url = BASE_URL + JSON_TYPE + "key=" + "96b89389842e4c14b4e202506232808" + CITY + AQI_YES

def user_input():
    """ Function for User Input"""
    user_input_string = input("Choose a city: ")
    return user_input_string

def request_data():
    """ Function for requesting weather data"""
    city = "&q=" + user_input()
    final_url = BASE_URL + JSON_TYPE + "key=" + config.API_KEY + city + AQI_YES
    response = requests.get(final_url, timeout=10)
    return response.json()

if __name__ == "__main__":
    print(request_data())
