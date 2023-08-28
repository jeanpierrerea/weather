""" Weather App """

import requests, config


BASE_URL = "http://api.weatherapi.com/v1/"
JSON_TYPE = "current.json?"
CITY = "&q=London"
AQI_YES = "&aqi=yes"

FINAL_URL = BASE_URL + JSON_TYPE + "key=" + config.API_KEY + CITY + AQI_YES
# URL = "https://api.weatherapi.com/v1/current.json?key=6f6b01f43b3b4e6fa75175805232808&q=London&aqi=no"

response = requests.get(FINAL_URL, timeout=10)
print(response.json())

def user_input():
    """ Function for User Input"""
    user_input_string = input("Check weather: ")
    return user_input_string

if __name__ == "__main__":
    print(user_input())
