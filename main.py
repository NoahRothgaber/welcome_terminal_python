"""
Noah Rothgaber
This is script is probably pointless, but  it shall
1: Open up a linux terminal
2: Welcome  me  with a setup prompt asking for some information
3: Will ask to set up any aliases (if first time ran)
4:  Will print out a prompt in the following way
                "Hello {name}! Hope you are having
                a/an {synonym for good} day!


                It's  {date} and  the time is {time}

                Here's the expected weather today in {setup_location}

                Here's a dad joke from {dad_joke_source_name}

                joke: {dad_joke}

                {condition for updates available}

                updates available :
                " You have a few updates available, would you like to
                 install?"

                 updates not available:
                 "You have no updates available"

                 ___________________________________________________
                 Order Brain Storm

                 Open up terminal environment
                 Use multiple files in python script
                 File 1 main.py
                 File 2 init_setup.py
                 File 3 info.txt

                 Find out means of pulling dad jokes from either https
                 or some api call

                 Pipe into file, check file every run to ensure no repeat

                 API Call it is
                 https://github.com/Anupya/dadjoke-cli

                 Find weather data api

                 PyOWM
                 https://pyowm.readthedocs.io/en/latest/#

                 make system call to apt and parse into conditional

                $ /usr/lib/update-notifier/apt-check --human-readable
                0  packages can be updated.
                0 updates are security updates.

                parse system call output into custom string
                provide prompt to user for installation through apt install
                sub process
                https://www.section.io/engineering-education/how-to-execute-linux-commands-in-python/




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
                 Text file 1 info.txt
"""

from Scripts import setup_script


def main():
    welcome = setup_script.SetupHost()


if __name__ == "__main__":
    main()
