# https://pyowm.readthedocs.io/en/latest/v3/code-recipes.html
import os

from pyowm.owm import OWM
from pyowm.utils.config import get_config_from
import time

# 1000 calls per day on  a free plan. I will not hit that, but still
# intend on file checking
''' will try to implement a hard cap to the number of calls per day
(the api itself does this, I do not need to do this)
by checking a directory of weather calls for the area that are
stored when the api is called. If a file exists with the current 
day (or hour) then i will just print that files weather data. 
The API allows for 10,000 free calls per day but I want to ensure
I do not exceed the amount.
'''
from subprocess import run


def print_with_lolcat(print_val):
    run(["lolcat"], input=print_val, text=True)


def get_forecast_path():
    time_str = time.asctime()
    index = 0
    for char in time_str:
        if char == " ":
            time_str = time_str[:index] + "_" + time_str[index + 1:]
        index += 1
    index = 0
    count_ = 0
    for char in time_str:
        if char == "_":
            count_ += 1
        if count_ == 3:
            time_str = time_str[:index + 3]
        index += 1
    path = './config/forecasts'
    path = os.path.join(path, time_str + '.txt')
    return path


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
    final_forecast_string = ""

    def __init__(self):
        forecast_path = get_forecast_path()
        print_with_lolcat("And now for the weather...")
        if os.path.exists(forecast_path):
            print_with_lolcat("Weather for this hour exists in path...\n"
                              "Printing\n...\n...\n...")
            with open(forecast_path, 'r') as forecast:
                for line in forecast:
                    print_with_lolcat(line)
        else:
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
                str(self.weather_read.current.precipitation_probability) \
                    .title() + '%'
            if current_rain_chance == "None%":
                # this was terrible why did I do it like this
                current_rain_chance = "0%"
            time.sleep(2)  # give time to load so it's clean
            self.final_forecast_string = \
                f'The temperature in {self.city}, {self.state} ' \
                f'is {current_temp} degrees with {current_status}\n' \
                f'The humidity is {current_humidity}, and there is a ' \
                f'{current_rain_chance} chance of rain.'
            print_with_lolcat(self.final_forecast_string)
            self.forecast_store()

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

    def forecast_store(self):
        path = get_forecast_path()
        with open(path, 'w') as forecast:
            forecast.write(self.final_forecast_string)
