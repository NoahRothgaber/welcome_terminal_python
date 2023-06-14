from Scripts import dad_joke, setup_script, weather_caller

class WelcomeManager():
    def __init__(self):
        setup = setup_script.SetupHost()
        dad = dad_joke.DadJokeHandler()
        weather = weather_caller.WeatherCaller()

welcome_manager = WelcomeManager()
