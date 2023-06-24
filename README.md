
# WeatherAPI

WeatherAPI is a command-line tool that retrieves and displays the current weather forecast for a specific location. It uses the OpenWeatherMap API to fetch weather data and is implemented in Python for data manipulation and parsing. The tool aims to provide a convenient way to access accurate and up-to-date weather information, assisting users in planning their outdoor activities and making day-to-day decisions.

## Features

Features of the Weather Forecasting Tool include:

- Fetching weather data using the [OpenWeatherMap](https://openweathermap.org/current) API.
- Retrieving the current weather forecast for a designated location.
- Command-line interface for easy access and usage.
- Simplicity and efficiency, eliminating the need for complex graphical interfaces or websites.

## Technologies
The technologies utilized in the tool's development are:

- Python: A versatile programming language used for efficient data manipulation and parsing.
- GitHub Copilot: An AI-powered coding assistant that assists with API integration, data parsing, and error handling.
- OpenWeatherMap API: An API offering comprehensive weather data for various locations worldwide.

## Installation

To install and use WeatherAPI, follow the steps given below:
- Fork the carrer-scraper repository by clicking the "Fork" button at the top right corner of the repository page. This will create a copy of the repository under your GitHub account.
- Clone the forked repository to your local machine:
  ```
  git clone https://github.com/{YOUR-USERNAME}/WeatherAPI   
  ```
- Navigate to the project directory: 
  ```
  cd WeatherAPI
  ```
- Install the necessary Python packages by running the following command:
  ```
  pip install -r requirements.txt
  ```


## How to use?

To use WeatherAPI, follow the steps given below:

- Create a free account on WeatherAPI.com and obtain an API key (Wait for sometime if you have created the API key, It takes some hours to get active).
- Paste the API key in the config.ini file.
    ```
    api_key = <API KEY>
    ```
- Run the command-line tool and provide the name of the location for which you want to retrieve the weather forecast.
  ```
    python3 copilot.py --location LOCATION --unit UNIT
    ```

  Example:
    ```
    python3 copilot.py --location london --unit C
    ```
    ```
    python3 copilot.py --location "New York" --unit F
    ```
    Default temperature unit is K (Kelvin).

The tool will fetch the weather data from the OpenWeatherMap API and display the current forecast for the specified location.

### Other Features
Some other helpful and cool features:
- **Location**: Location of the place user want to see the weather can be added easily.
  ```
  python3 weatherapi.py --location LOCATION
  ```
- **Zipcode**: Zipcode of the place user want to see the weather can be added easily and used.
  ```
  python3 weatherapi.py --zipcode ZIPCODE
  ```
- **Unit**: You can change the unit of display according to your convenience.
  ```
  python3 weatherapi.py --location LOCATION --unit C/F/K
  ```
  Default is Kelvin

- **Debug**: Good news for programmers, it has a ``--debug`` option that you can turn on to get **DEBUG** level logging in log file named **app.log**. Default it gives **WARNING** level logging.
  ```
  python3 scraper.py --debug True
  ```
  **NOTE:** The default logging is set to **WARNING** 

## Contributions

Contributions to WeatherAPI are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on the GitHub repository.

## Developed By  

- [Abhishek Singh Kushwaha](https://github.com/ASK-03)
- [Siddhi Agarwal](https://github.com/agaSiddhi)
- [Riddhi Agarwal](https://github.com/riddhi1703)