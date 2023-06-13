#  check if dad joke is installed, install if not
import os
from dadjokes import Dadjoke
from subprocess import run


def print_with_lolcat(print_val):
    run(["lolcat"], input=print_val, text=True)


class DadJokeHandler():
    current_joke = Dadjoke()
    dad_joke_string = current_joke.joke + '\n'
    directory = './config'
    filename = 'used_dadjokes'
    file_path = os.path.join(directory, filename)
    i_can_haz_lim = 744
    joke_list = []
    joke_file_total = 0

    def __init__(self):
        print_with_lolcat('Sourcing the funniest thing ever...')
        self.file_check_and_parse()
        self.check_unique()
        self.print_joke()

    def file_check_and_parse(self):
        if os.path.exists(self.file_path):
            # File does not exist, create it
            self.reset_file_if_full()
            with open(self.file_path, 'r') as file:
                for line in file:
                    self.joke_list.append(line)
                self.joke_file_total = len(self.joke_list)
        else:
            with open(self.file_path, 'w') as file:
                file.write('')

    def check_unique(self):
        while self.dad_joke_string in self.joke_list:
            self.dad_joke_string = self.current_joke.joke

    def reset_file_if_full(self):
        if self.joke_file_total == self.i_can_haz_lim:
            with open(self.file_path, 'w') as file:
                file.write(self.dad_joke_string)

    def print_joke(self):
        print_with_lolcat("Dad Joke:\t" + self.dad_joke_string)
        with open(self.file_path, 'a') as file:
            file.write(self.dad_joke_string)

