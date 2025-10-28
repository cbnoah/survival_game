from game.CLI import show_cli_menu, get_cli_user_choice
from game.game_loop import main

if __name__ == "__main__":
    while True:
        show_cli_menu()
        choice = get_cli_user_choice()
        if choice == "1":
            main()
            break
        elif choice == "2":
            print("A faire")
        elif choice == "3":
            print("Quitter le jeu.")
            break
        else:
            print("Choix invalide, réessayez.")