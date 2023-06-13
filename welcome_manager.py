from Scripts import dad_joke, setup_script


class WelcomeManager():
    def __init__(self):
        setup = setup_script.SetupHost()
        dad = dad_joke.DadJokeHandler()

welcome_manager = WelcomeManager()
