from game.CLI import show_cli_status
from game.CLI import show_cli_action_menu
from game.player import Player
from game.daily_event import daily_event
import random

from utils.save_handler import save_game


def main(player: Player, day_survived: int = 0) -> None:

    while True:

        show_cli_status(player, day_survived)
        show_cli_action_menu()
        choice = input("Your Choice: ").strip().lower()


        if choice == "1":
            player.fish()
            player.modify_energy(10)
            day_survived += 1

        elif choice == "2":
            player.sleep()

            day_survived += 1

        elif choice == "3":
            player.look_for_water()
            day_survived += 1

        elif choice == "4":
            random_event = random.randint(0, 4)
            player.explore(random_event)
            day_survived += 1

            while True:
                response = input().strip().lower()
                if response in ("yes", "y", "oui", "o"):
                    if random_event == 0:  # casino
                        player.modify_hunger(5)
                        player.modify_energy(-10)
                        print("You enter the casino.")
                    elif random_event == 1:  # school
                        player.modify_energy(10)
                        print("You enter the school.")
                    elif random_event == 2:  # hospital
                        player.modify_energy(20)
                        player.modify_thirst(-10)
                        print("You enter the hospital.")
                    elif random_event == 3:  # police station
                        player.modify_energy(5)
                        print("You enter the police station.")
                    elif random_event == 4:  # house store
                        player.modify_hunger(-15)
                        player.modify_thirst(-10)
                        print("You enter the store.")
                    break
                elif response in ("no", "n", "non"):
                    print("You decided not to enter.")
                    break
                else:
                    print("Invalid choice. Please enter yes or no.")


        elif choice == "s":
            save_game(player, day_survived)
            print("Game saved.")
            continue

        elif choice == "q":
            print("Leaving the game.")
            break

        else:
            print("Invalid choice, please try again.")
            continue


        daily_event(player)


        if day_survived >= 60:
            print(f"Congratulations! {player.name} has survived for 60 days and won the game!")
            break

        if not player.is_alive:
            print(f"{player.name} is no longer alive. Game over.")
            break


