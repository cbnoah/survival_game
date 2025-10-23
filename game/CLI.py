def show_cli_menu():
    print("Welcome to the Game CLI!")
    print("1. Start New Game")
    print("2. Load Game")
    print("3. Exit")


def show_cli_status(player, day_survived):
    print(f'#############################################')
    print(f"Days Survived: {day_survived}")
    print(f"Hunger: {player.hunger}")
    print(f"Thirst: {player.thirst}")
    print(f"Energy: {player.energy}")
    print(f"Is Alive: {player.is_alive}")
    print(f'#############################################')


def get_cli_user_choice():
    choice = input("Please enter your choice: ")
    return choice.strip().lower()


def show_cli_action_menu():
    print("Choose an action:")
    print("1 - Fish")
    print("2 - Sleep")
    print("3 - Look for Water")
    print("4 - Explore (Random Event)")
    print("q - Quit Game")
    print("s - Save Game")


