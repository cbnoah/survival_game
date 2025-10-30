from game.CLI import show_cli_menu, get_cli_user_choice, show_cli_status , get_player_name
from game.game_loop import main
from game.player import Player
from utils.save_handler import load_game, is_there_info

if __name__ == "__main__":
    while True:
        show_cli_menu()
        choice = get_cli_user_choice()
        if choice == "1":
            player_name = get_player_name()
            main(Player(player_name))
            break
        elif choice == "2":
            if is_there_info():
                try:
                    player = load_game()
                    main(Player(player.name, player.hunger, player.thirst, player.energy))
                except Exception:
                    print("Impossible de charger la sauvegarde.")
            else:
                print("Aucune sauvegarde disponible.")
        elif choice == "3":
            print("Quitter le jeu.")
            break
        else:
            print("Choix invalide, réessayez.")