from game.player import Player
from utils.gauges import gauge_drawer


def show_cli_menu():
    print("Welcome to the Game CLI!")
    print("1. Start New Game")
    print("2. Load Game")
    print("3. Exit")


def show_cli_status(p:Player, day_survived):
    print(f'#############################################')
    print(f"Days Survived: {day_survived}")
    print(f"Hunger: {gauge_drawer(100-p.hunger, 100)}")
    print(f"Thirst: {gauge_drawer(100-p.thirst, 100)}")
    print(f"Energy: {gauge_drawer(p.energy,100)}")
    print(f'#############################################')


def get_cli_user_choice():
    choice = input("Please enter your choice: ")
    return choice.strip().lower()


def show_cli_action_menu():
    print("Choose your daily action:")
    print("1 - Fish")
    print("2 - Sleep")
    print("3 - Look for Water")
    print("4 - Explore")
    print("q - Quit Game")
    print("s - Save Game")


def get_player_name():
    """
    Ask the user for their player name via CLI.
    """
    while True:
        name = input("Write your nickname: ").strip()
        if name:
            return name
        print("The nickname cannot be empty. Please try again.")

