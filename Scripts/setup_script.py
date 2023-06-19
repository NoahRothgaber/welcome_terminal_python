import os
import os.path
import random
from subprocess import run


def reset_color():
    print("\033[0;0;0m", end="")


def print_with_lolcat(print_val):
    run(["lolcat"], input=print_val, text=True)


def country_codes():
    with open("./config/country_codes.txt", 'r') as file:
        for code in file:
            print_with_lolcat(code)

def state_codes():
    with open("./config/state_codes.txt", 'r') as file:
        for code in file:
            print_with_lolcat(code)

class SetupHost():
    user_name = None
    user_city = ""
    user_state = ""
    user_country = ""
    user_zip = 00000
    welcome_prompt_p1 = 'Hello!\nIt looks like this is your first ' \
                        'time booting up your linux system!'
    welcome_prompt_p2 = "You poor soul..."
    country_code_list = []
    usa_state_code_list =[]
    word_list = []
    used_words = []
    unique_greeting_str = None
    list_file_total = 0
    parse_syn_path = './config/good_synonyms_parsed'
    syn_path = './config/good_synonyms'

    def __init__(self):
        self.set_country_list()
        self.set_state_list()
        self.file_check_greeting()
        self.unique_greetings()
        self.file_check_info()
        self.greet_specific_user()
        # Run script for actual code purpose

    def file_check_info(self):
        directory = './config'
        filename = 'info.txt'
        file_path = os.path.join(directory, filename)
        if not os.path.exists(file_path):
            # File does not exist, create it
            with open(file_path, 'w') as file:
                # Perform any necessary operations on the file
                self.file_check_greeting()
                self.first_setup()
                file.write(f'Name = {self.user_name}\n'
                           f'Country = {self.user_country}\n'
                           f'City = {self.user_city}\n'
                           f'State = {self.user_state}\n'
                           f'Zip = {self.user_zip}'
                           )
        else:
            with open(file_path, 'r') as file:
                for line in file:
                    if line[: 7] == "Name = ":
                        self.user_name = line[7:]
                    elif line[: 6] == "Zip = ":
                        self.user_zip = line[6:]
                    elif line[: 7] == "City = ":
                        self.user_city = line[7:]
                    else:
                        self.user_country = line[10:]

    def file_check_greeting(self):
        directory = './config'
        filename = 'good_synonyms'
        file_path = os.path.join(directory, filename)
        if os.path.exists(file_path):
            # File does not exist, create it
            with open(file_path, 'r') as file:
                for line in file:
                    self.word_list.append(line)
        else:
            with open(file_path, 'w') as file:
                file.write('wtf')
            print("Something went real bad.. uh oh")
        self.list_file_total = len(self.word_list)

    def unique_greetings(self):
        directory = './config'
        filename = 'good_synonyms_parsed'
        file_path = os.path.join(directory, filename)
        proto_str_index = \
            random.randint(0, len(self.word_list) - 1)
        # open file if  it's not first time running program
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                for line in file:
                    self.used_words.append(line)
            file.close()
            # pipe the words from the used file to list
            if len(self.used_words) >= self.list_file_total:
                with open(file_path, 'w') as file:
                    pass
                # erase file if user has received all greetings
            while self.word_list[proto_str_index] in self.used_words:
                proto_str_index = \
                    random.randint(0, len(self.word_list) - 1)
            self.unique_greeting_str = self.word_list[proto_str_index]
            self.used_words.append(self.unique_greeting_str)
        else:
            with open(file_path, 'w') as file:
                self.used_words.append(self.word_list[proto_str_index])
                self.unique_greeting_str = self.word_list[proto_str_index]

    def first_setup(self):
        self.greeting()
        self.name_capture()
        self.country_capture()
        self.city_capture()
        self.state_capture()
        self.zip_capture()

    def greeting(self):
        print_with_lolcat(self.welcome_prompt_p1)
        print(f'\033[1;31m{self.welcome_prompt_p2}')
        reset_color()

    def name_capture(self):
        print_with_lolcat("Please provide the preferred "
                          "username for your greeting:\n")
        self.user_name = input()

    def set_state_list(self):
        with open('config/state_codes.txt', 'r') as states:
            for state in states:
                self.usa_state_code_list.append(state[-3:-1])

    def set_country_list(self):
        with open('config/country_codes.txt', 'r') as countries:
            for country in countries:
                self.country_code_list.append(country[:2])

    def country_capture(self):
        code_selected = False
        while not code_selected:
            print_with_lolcat("Please provide your countries two "
                              "digit code.\nIf you're unsure what your country's"
                              " code is... type \"country\"\n")
            temp_country = input()
            while temp_country != 'country' and \
                    temp_country not in self.country_code_list:
                print_with_lolcat("That wasn't a valid code.\n"
                                  "Please provide your countries two "
                                  "digit code.\nIf you're unsure what your country's"
                                  " code is... type \"country\"\n")
                temp_country =  input()
            if temp_country == "country":
                country_codes()
                temp_country = ""
            else:
                self.user_country = temp_country.upper()
                code_selected = True

    def state_capture(self):
        code_selected = False
        while not code_selected:
            print_with_lolcat("Please provide your States two "
                              "digit code.\nIf you're unsure what your state's"
                              " code is... type \"USA\"\n")
            temp_state = input()
            while temp_state.lower() != 'usa' and \
                    temp_state not in self.usa_state_code_list:
                print_with_lolcat("That wasn't a valid code.\n"
                                  "Please provide your state's two "
                                  "digit code.\nIf you're unsure what your state's"
                                  " code is... type \"USA\"\n")
                input()
            if temp_state.lower() == "usa":
                state_codes()
                temp_state = ""
            else:
                self.user_state = temp_state.upper()
                code_selected = True

    def city_capture(self):
        print_with_lolcat("Please enter the name of your City")
        self.user_city = input()

    def zip_capture(self):
        # Zip code capture
        zip_code_check = False
        while not zip_code_check:
            print_with_lolcat("Please enter your 5 digit US zip code\n")
            temp_zip = input()
            if temp_zip.isnumeric() and len(str(temp_zip)) == 5:
                self.user_zip = temp_zip
                zip_code_check = True
            else:
                print(f'\033[1;31mPlease enter your zipcode in the 5 Digit'
                      f' USA format ex: 12345')
                reset_color()

    def write_used_words(self):
        with open(self.parse_syn_path, 'w') as file:
            for used_word in self.used_words:
                file.write(used_word)

    def greet_specific_user(self):
        print_with_lolcat(f'Glad to see you {self.user_name.rstrip()}!' +
                          f' Hope your day is going ' +
                          f'{self.unique_greeting_str.rstrip()}!'''
                          )
        self.write_used_words()
