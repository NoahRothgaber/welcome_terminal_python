import os
import os.path
import random
from subprocess import run

def reset_color():
    print("\033[0;0;0m", end="")


def print_with_lolcat(print_val):
    run(["lolcat"], input=print_val, text=True)


class SetupHost():
    user_name = None
    user_zip = 00000
    welcome_prompt_p1 = 'Hello!\nIt looks like this is your first ' \
                        'time booting up your linux system!'
    welcome_prompt_p2 = "You poor soul..."
    word_list = []
    used_words = []
    unique_greeting_str = None
    list_file_total = 0
    parse_syn_path = './config/good_synonyms_parsed'
    syn_path = './config/good_synonyms'

    def __init__(self):
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
                file.write(f'Name = {self.user_name}\nZip = '
                           f'{self.user_zip}')
        else:
            with open(file_path, 'r') as file:
                for line in file:
                    if line[: 7] == "Name = ":
                        self.user_name = line[7:]
                    else:
                        self.user_zip = line[6:]

    def file_check_greeting(self):
        directory = './config'
        filename = 'good_synonyms'
        file_path = os.path.join(directory, filename)
        print(os.getcwd())
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
        self.zip_capture()

    def greeting(self):
        print_with_lolcat(self.welcome_prompt_p1)
        print(f'\033[1;31m{self.welcome_prompt_p2}')
        reset_color()

    def name_capture(self):
        self.user_name = input("Please provide the preferred "
                               "username for your greeting:\n")

    def zip_capture(self):
        # Zip code capture
        zip_code_check = False
        while not zip_code_check:
            temp_zip = input("Please enter your 5 digit US zip code\n")
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