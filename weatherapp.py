"""This application takes the city name and predict its weather condition."""

import os

import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")


def fetch_data(city):
    """This function fetches data from OpenWeatherMap API"""

    try:
        weather_data = requests.get(
            f"{BASE_URL}?q={city}&units=imperial&APPID={API_KEY}", timeout=10
        )
        return weather_data
    except requests.Timeout:
        print("The request timed out")
        return None
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def predict_weather(weather_data, city):
    """This function predicts the weather of the entered city"""

    weather_data = weather_data.json()
    if weather_data["cod"] == "404":
        print("You haven't entered a valid city!!!")
    else:
        weather = weather_data["weather"][0]["main"]
        temp = round(weather_data["main"]["temp"])

        print(f"The weather in {city} is: {weather}")
        print(f"The temperature in {city} is: {temp}ºF")


def main():
    """This function is the driver of the application."""

    city = input("Enter City :\t")
    weather_data = fetch_data(city)
    predict_weather(weather_data, city)


if __name__ == "__main__":
    main()
