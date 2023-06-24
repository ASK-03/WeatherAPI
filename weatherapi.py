# Import
import argparse
import configparser
import requests
import logging
from rich.progress import track
import time
from rich.table import Table
from rich.console import Console
from rich import box, print
from datetime import datetime
from banner import print_banner

# write a function to get geolocation from city name using openweathermap api
def get_geolocation_using_cityname(cityname):

    """
    Description: This function is used to get geolocation from city name using openweathermap api
    Input: cityname
    Output: None
    """

    url = f"https://api.openweathermap.org/geo/1.0/direct?q={cityname}&appid={API_KEY}"
    response = requests.get(url)
    try:
        if response.status_code == 200:
            response_json = response.json()[0]
            return response_json["lat"], response_json["lon"]
        else:
            logging.error(msg="response status code is not 200")
            return [None, None]
    except Exception as e:
        logging.fatal(msg=e)
        exit()

# write a function to get geolocation from zipcode using openweathermap api
def get_geolocation_using_zipcode(zipcode):

    """
    Description: This function is used to get geolocation from zipcode using openweathermap api
    Input: zipcode
    Output: None
    """

    url = f"https://api.openweathermap.org/geo/1.0/zip?zip={zipcode}&appid={API_KEY}&limit=1"
    response = requests.get(url=url)
    try:
        if response.status_code == 200:
            response_json = response.json()[0]
            return response_json["lat"], response_json["lon"]
        else:
            logging.error(msg="response status code is not 200")
            return None, None
    except Exception as e:
        logging.fatal(msg=e)
        exit()

# write a function to get weather using geolocation using openweathermap api
def get_weather_using_geolocation(lat, lon) -> None:

    """
    Description: This function is used to get weather using geolocation using openweathermap api
    Input: lat, lon
    Output: None
    """

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(url)
    try:
        if response.status_code == 200:
            return response.json()
        else:
            logging.error(msg="response status code is not 200")
            return None
    except Exception as e:
        logging.fatal(msg=e)
        exit()


# write a function to display weather field in table format on terminal using rich library
def display_field_table(response, location, unit) -> None:

    """
    Description: This function is used to display weather field in table format on terminal using rich library
    Input: response, location, unit
    Output: None
    """

    if unit == "C" or unit == "F":
        unit = f"°{unit}"

    # print todays date using datetime module
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    table = Table(
        show_header=True,
        header_style="bold gold3",
        border_style="white",
        title=f"\n CURRENT WEATHER | {date}\n",
        title_style="bold white on black",
        title_justify="center",
        box=box.SIMPLE_HEAVY,
        show_footer=True,
        footer_style="bold gold3",
    )
    table.add_column("Field", justify="left", style="bold green", width=40)
    table.add_column("Value", justify="left", style="bold violet", width=40)

    location = location
    temp = (
        f"{convert_kelvin_to_unit(kelvin=response['main']['temp'], unit=unit)} {unit}"
    )
    wind_speed = f"{response['wind']['speed']} meter/sec"
    humidity = f"{response['main']['humidity']} %"
    weather = f"{get_emoji_for_icon_id(icon_id=response['weather'][0]['icon'])} {response['weather'][0]['main']} : {response['weather'][0]['description']}"
    max_temp = f"{convert_kelvin_to_unit(kelvin=response['main']['temp_max'], unit=unit)} {unit}"
    min_temp = f"{convert_kelvin_to_unit(kelvin=response['main']['temp_min'], unit=unit)} {unit}"

    table.add_row("📍  Location", f"{location}")
    table.add_row()
    table.add_row("🌡️   Current Temperature", f"{temp}")
    table.add_row()
    table.add_row("🌬️   Current Wind Speed", f"{wind_speed} ")
    table.add_row()
    table.add_row("💧  Current Humidity", f"{humidity} ")
    table.add_row()
    table.add_row("🌤️   Current Condition", f"{weather} ")
    table.add_row()
    table.add_row(f"📈  Max Temp {unit}", f"{max_temp} ")
    table.add_row()
    table.add_row(f"📉  Min Temp {unit}", f"{min_temp}")
    table.add_row()
    console = Console()
    console.print(table)


def test_function() -> None:
    """
    Description: This function is used to test the API
    Input: None
    Output: None
    """

    url = f"http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API_KEY}"
    response = requests.get(url)
    print(response.json())


def get_emoji_for_icon_id(icon_id) -> str:
    
    """
    Description: This function is used to get emoji for icon id
    Input: icon_id
    Output: emoji
    """
    mappings = {
        "01d": "🌞",
        "01n": "🌚",
        "02d": "🌤️",
        "02n": "💨🌚",
        "03d": "💨",
        "03n": "💨",
        "04d": "💨",
        "04n": "💨",
        "09d": "🌧️",
        "09n": "🌧️",
        "10d": "🌦️",
        "10n": "🌦️🌚",
        "11d": "⛈️",
        "11n": "⛈️",
        "13d": "🌨️",
        "13n": "🌨️",
        "50d": "🌫️",
        "50n": "🌫️",
    }

    return mappings.get(icon_id, "🤷")


def check_unit(unit) -> str:

    """
    Description: This function is used to check if the unit is valid or not, and corrects if user has given wrong input close to the valid unit
    Input: unit - unit to check
    Output: unit - valid unit
    """

    if unit == "K" or unit.lower() == "kelvin" or unit[0].lower() == "k":
        return "K"
    elif unit == "C" or unit.lower() == "celsius" or unit[0].lower() == "c":
        return "C"
    elif unit == "F" or unit.lower() == "fahrenheit" or unit[0].lower() == "f":
        return "F"
    else:
        logging.error(msg="Invalid unit. Defaulting to Celsius")
        return "C"


def convert_kelvin_to_unit(kelvin, unit) -> float:
    """
    Description: This function is used to convert kelvin to celsius or fahrenheit   
    Input: kelvin - temperature in kelvin
           unit   - unit to convert into
    Output: converted value
    """
    if type(kelvin) == str:
        kelvin = round(float(kelvin), 2)

    if unit == "C" or unit == "°C":
        return round(kelvin - 273.15, 2)
    elif unit == "F" or unit == "°F":
        return round((kelvin - 273.15) * (9 / 5) + 32, 2)
    else:
        return kelvin
    

def get_arguments() -> dict:

    """
    Description: This function uses argparse module to get arguments from command line
    Input: None
    Output: dictionary of arguments
    """

    parser = argparse.ArgumentParser(
        prog="",
        description="Get weather information from OpenWeatherMap using city name or zip code.",
    )
    parser.add_argument(
        "--location",
        type=str,
        help="City name: Name of the city, you want to find current weather for",
        default=None,
    )
    parser.add_argument(
        "--zipcode",
        type=str,
        help="Zip code: Zipcode of the city, you want to find current weather for",
        default=None,
    )
    parser.add_argument(
        "--unit", type=str, help="K: Kelvin, C: Celsius, F: Fahranheit", default="K"
    )
    parser.add_argument(
        "--debug",
        type=bool,
        help="Debug mode for developers out there :P, default will run in critical debug levels",
        default=False,
    )

    args = parser.parse_args()
    location = args.location
    zipcode = args.zipcode
    unit = check_unit(unit=args.unit)
    debug = args.debug

    return {
        "location": location,
        "zipcode": zipcode,
        "unit": unit,
        "debug": debug,
    }


if __name__ == "__main__":
    # write a function to API_KEY from config.ini using configparser
    config = configparser.ConfigParser()
    config.read("config.ini")

    API_KEY = config["openweathermap"]["api_key"]

    try:
        arguments = get_arguments()
    except Exception as e:
        logging.fatal(msg=e)
        logging.fatal(msg="Please check your arguments")
        exit()

    location = arguments["location"]
    zipcode = arguments["zipcode"]
    unit = arguments["unit"]
    debug = arguments["debug"]

    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)

    logging.debug(msg=f"location: {location}")

    print_banner()
    # write a loop to display progress bar using rich.progress track method
    for _ in track(sequence=range(100), description="[green]Fetching data"):
        time.sleep(0.02)

    if location is not None:
        try:
            lat, lon = get_geolocation_using_cityname(cityname=location)
        except Exception as e:
            logging.fatal(msg=e)
            exit()
    elif zipcode is not None:
        try:
            lat, lon = get_geolocation_using_zipcode(zipcode=zipcode)
        except Exception as e:
            logging.fatal(msg=e)
            exit()
    else:
        logging.fatal("Please enter a valid location or zipcode")
        exit()

    if lat is not None and lon is not None:
        response = get_weather_using_geolocation(lat=lat, lon=lon)
        display_field_table(response=response, location=location, unit=unit)

    exit()
