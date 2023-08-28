""" Weather App """

import requests
import config

BASE_URL = "http://api.weatherapi.com/v1/"
JSON_TYPE = "current.json?"
CITY = "&q=London"
AQI_YES = "&aqi=yes"

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

def main():
    """ Function that parses through json data """
    
    data_set = request_data()

    # playing around with different values in json
    test = data_set["location"]["country"]

    current_temp = data_set["current"]["temp_c"]

    # storing current temp in an array
    emptyArray = []
    emptyArray.append(current_temp)
    print(emptyArray)

    return test

if __name__ == "__main__":
    print(main())
