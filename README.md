# Weather Prediction Application

This application provides real-time weather information for any city using the OpenWeatherMap API. Given a city name, the application fetches the current weather data and displays the weather condition and temperature.

## Features

- **City-Based Weather Prediction**: Enter any city name to receive the latest weather condition and temperature in Fahrenheit.
- **API Integration**: Leverages the OpenWeatherMap API to fetch real-time weather data.
- **Environment Variable Management**: Uses environment variables to securely manage API keys and base URLs.

## Prerequisites

- **Python 3.x**: Make sure you have Python installed on your machine.
- **pip**: Python package installer to install required libraries.
- **OpenWeatherMap API Key**: Obtain an API key from [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).

## Code Explanation

The application consists of three main functions and a driver function `main()`:

### `fetch_data(city)`

This function is responsible for fetching weather data from the OpenWeatherMap API based on the provided city name. It constructs a request URL using the base URL and API key stored in environment variables and sends a GET request to the API.

- **Parameters**:
  - `city` (str): The name of the city for which the weather data is to be fetched.

- **Returns**:
  - A response object containing weather data if the request is successful.
  - `None` if the request times out or encounters an error.
 
### `predict_weather(weather_data, city)`

This function processes the JSON response from the `fetch_data` function and extracts the weather condition and temperature for the specified city. It then prints these details to the console.

- **Parameters**:
  - `weather_data` (Response object): The response from the `fetch_data` function.
  - `city` (str): The name of the city for which the weather prediction is made.
 
### `main()`

This is the main driver function of the application. It prompts the user to enter a city name, fetches the weather data using the `fetch_data` function, and then uses the `predict_weather` function to display the weather condition and temperature.

**Steps**:
1. Prompts the user to input a city name.
2. Calls `fetch_data(city)` to retrieve the weather data for the entered city.
3. Calls `predict_weather(weather_data, city)` to process and print the weather information.

### Error Handling

The application includes robust error handling mechanisms to ensure smooth operation and user feedback:

- **Timeout Handling**: If the request to the OpenWeatherMap API takes longer than 10 seconds, a timeout exception is raised and handled. The application notifies the user about the timeout.

- **Invalid City Handling**: If the city name entered by the user does not match any known city (API returns a 404 error), the application informs the user that the city is not valid.

- **General Request Exceptions**: Other exceptions related to the HTTP request (e.g., network errors) are caught and handled gracefully. Error messages are printed to provide diagnostic information for troubleshooting.


