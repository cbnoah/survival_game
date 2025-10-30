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
    print(f"Is Alive: {p.is_alive}")
    print(f'#############################################')


def get_cli_user_choice():
    choice = input("Please enter your choice: ")
    return choice.strip().lower()


def show_cli_action_menu():
    print("Choose an action:")
    print("1 - Fish")
    print("2 - Sleep")
    print("3 - Look for Water")
    print("4 - Explore")
    print("q - Quit Game")
    print("s - Save Game")

def random_event_prompt(event):
    if event == 0:
        print('You found a casino  Enter (yes/no)?')
    elif event == 1:
        print('You found a school  Enter (yes/no)?')
    elif event == 2:
        print('You found a hospital    Enter (yes/no)?')
    elif event == 3:
        print('You found a police station  Enter (yes/no)?')
    elif event == 4:
        print('You found a store  Enter (yes/no)?')


def get_player_name():
    """
    Demande et retourne le pseudo du joueur.
    """
    while True:
        name = input("Entrez votre pseudo: ").strip()
        if name:
            return name
        print("Le pseudo ne peut pas être vide. Réessayez.")

