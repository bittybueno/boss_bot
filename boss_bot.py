import argparse
import random
from ascii_magic import AsciiArt
from random import randint
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from pyjokes import get_joke
from time import sleep
from colorama import Fore, Style
from sinjin_burns import sinjin_burns


class BossBot:
    def __init__(self):
        # Initialize Boss Bot with any necessary setup
        pass

    def greet(self):
        print(Fore.CYAN + "Hey how's it goin? What's on your mind?" + Style.RESET_ALL)

    def joke(self):
        print(Fore.YELLOW + get_joke() + Style.RESET_ALL)

    def sinjin(self):
        print(Fore.RED + random.choice(sinjin_burns) + Style.RESET_ALL)

    def commands(self):
        list_commands()


def execute_command(args, bot):
    print("\n")
    # Perform action based on command
    if args.command == "greet":
        bot.greet()
    elif args.command == "joke":
        bot.joke()
    elif args.command == "sinjin":
        bot.sinjin()
    elif args.command == "commands":
        bot.commands()


def intro(screen):
    effects = [
        Cycle(
            screen,
            FigletText("JASON", font='big'),
            int(screen.height / 2 - 8)),
        Cycle(
            screen,
            FigletText("BOT!", font='big'),
            int(screen.height / 2 + 3)),
        Stars(screen, 200)
    ]
    screen.play([Scene(effects, 50)], repeat=False)


def outro(screen):
    effects = [
        Cycle(
            screen,
            FigletText("BYEEEE", font='big'),
            int(screen.height / 2 - 8)),
        Stars(screen, 200)
    ]
    screen.play([Scene(effects, 50)], repeat=False)


def list_commands():
    print(Fore.GREEN + 'Jason Bot Commands:' + Style.RESET_ALL)
    print("1. greet - Say hello to the boss man.")
    print("2. joke - Ask the boss for a joke.")
    print("3. sinjin - Scold Sinjin for breaking staging... again.")
    print("4. exit - Quit Jason Bot.")
    print("\nUsage: Enter the command name to interact with the one and only Jason Bot.")





# Create a parser
parser = argparse.ArgumentParser(description="Jason Bot - Your Virtual Jason")

# Create subparsers container
subparsers = parser.add_subparsers(dest="command", help="Available commands")

# Command: greet
parser_greet = subparsers.add_parser("greet", help="Greet Jason Bot")

# Command: joke
parser_joke = subparsers.add_parser("joke", help="Tell a joke")

# Command: joke
parser_joke = subparsers.add_parser("sinjin", help="Scold Sinjin")

parser_joke = subparsers.add_parser("commands", help="See commands")

# Initialize Boss Bot
boss_bot = BossBot()

Screen.wrapper(intro)
my_art = AsciiArt.from_image('jason.png')
my_art.to_terminal(columns=50)

# Main loop
while True:
    try:
        # Prompt for input
        print("\n\nJason Bot is ready. Use 'commands' to see a list of available commands.")
        command = input("Enter a command to seek wisdom from the one and only Jason (or 'exit' to quit): ").strip().lower()

        # Check for exit command
        if command == "exit":
            print("\n\nJason is so sad to see you go...")
            Screen.wrapper(outro)
            break

        # Parse command-line arguments
        args = parser.parse_args([command])

        # Execute command
        execute_command(args, boss_bot)

    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected. Exiting Jason Bot...")
        break
