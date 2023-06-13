# https://pyowm.readthedocs.io/en/latest/v3/code-recipes.html
from pyowm.owm import OWM
from pyowm.utils.config import get_config_from

''' will try to implement a hard cap to the number of calls per day
by checking a directory of weather calls for the area that are
stored when the api is called. If a file exists with the current 
day (or hour) then i will just print that files weather data. 
The API allows for 10,000 free calls per day but I want to ensure
I do not exceed the amount.

Here are the examples searching via city ids

from pyowm.owm import OWM
owm = OWM('your-api-key')
reg = owm.city_id_registry()

# All Ontario cities in the uS
ontarios_in_us = reg.ids_for('Ontario', country='US', matching='exact')  # five results

# Ontario in Canade
ontario_in_canada = reg.ids_for('Ontario', country='CA', matching='exact')  # one result: [(6093943, 'Ontario', 'CA', None, 49.250141, -84.499832)]

# Ontario in the state of New York
ontario_in_ny = reg.ids_for('Ontario', country='US', state='NY', matching='exact')  # one result: [(5129887, 'Ontario', 'US', 'NY', 43.220901, -77.283043)]
'''


class WeatherCaller:
    open_weather_key = ''
    owm = OWM(open_weather_key)
    config_dict = get_config_from("./config/owm_config.json")
    reg = owm.city_id_registry()

    def __init__(self):
        self.load_key()
        self.owm = OWM(self.open_weather_key, self.config_dict)

    def load_key(self):
        with open("./config/dont_commit", 'r') as file:
            for line in file:
                self.open_weather_key = line
