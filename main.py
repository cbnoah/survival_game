from game.CLI import show_cli_menu, get_cli_user_choice, get_player_name
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
                    save_info = load_game()
                    main(Player(save_info["player"].name, save_info["player"].hunger, save_info["player"].thirst, save_info["player"].energy), save_info['days_survived'])
                except Exception:
                    print("Save unloadable or corrupted.")
            else:
                print("No saved game found.")
        elif choice == "3":
            print("Exiting the game.")
            break
        else:
            print("Incorrect answer. Please try again.")