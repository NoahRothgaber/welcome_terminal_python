# https://pyowm.readthedocs.io/en/latest/v3/code-recipes.html
from pyowm.owm import OWM
from pyowm.utils.config import get_config_from
import time

''' will try to implement a hard cap to the number of calls per day
by checking a directory of weather calls for the area that are
stored when the api is called. If a file exists with the current 
day (or hour) then i will just print that files weather data. 
The API allows for 10,000 free calls per day but I want to ensure
I do not exceed the amount.
'''
from subprocess import run


def print_with_lolcat(print_val):
    run(["lolcat"], input=print_val, text=True)


class WeatherCaller:
    open_weather_key = ''
    owm = None
    config_dict = get_config_from("./config/owm_config.json")
    reg = None
    weather_manager_obj = None
    country = ''
    city = ''
    state = ''
    zip = ''
    lat = None
    lon = None
    weather_read = None
    list_of_locations = None
    location_coord = None

    def __init__(self):
        print_with_lolcat("And now for the weather...")
        self.load_key()
        self.owm = OWM(self.open_weather_key)
        self.reg = self.owm.city_id_registry()
        self.weather_manager_obj = self.owm.weather_manager()
        self.parse_user_info()
        self.reg = self.owm.city_id_registry()
        self.list_of_locations = self.reg.locations_for(
                city_name=self.city,
                state=self.state, country=self.country,
                matching='exact'
            )
        self.location_coord = self.list_of_locations[0]
        self.lat = self.location_coord.lat
        self.lon = self.location_coord.lon
        self.weather_read = self.weather_manager_obj.one_call(
            self.lat, self.lon)
        current_status = \
            str(self.weather_read.current.detailed_status).title()
        current_temp_dict = \
            self.weather_read.current.temperature("fahrenheit")
        current_temp = str(round(current_temp_dict['temp'], 1)).title()
        current_humidity = \
            str(self.weather_read.current.humidity).title() + '%'
        # The current humidity is {humidity}
        current_rain_chance = \
            str(self.weather_read.current.precipitation_probability)\
            .title() + '%'
        if current_rain_chance == "None%":
            current_rain_chance = "0%"
        time.sleep(2)  # give time to load so it's clean
        print_with_lolcat(f'The temperature {current_temp} degree with {current_status}.\n'
                          f'The humidity is {current_humidity}, and there is a {current_rain_chance} chance of rain.')

    def load_key(self):
        with open("./config/dont_commit", 'r') as file:
            for line in file:
                self.open_weather_key = line
                break

    def parse_user_info(self):
        with open('./config/info.txt', 'r') as file:
            for line in file:
                if line[: 6] == "Zip = ":
                    self.zip = line[6:].strip()
                elif line[: 7] == "City = ":
                    self.city = line[7:].strip()
                elif line[: 10] == "Country = ":
                    self.country = line[10:].strip()
                else:
                    self.state = line[8:].strip()
