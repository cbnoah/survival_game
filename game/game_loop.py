from game.CLI import show_cli_status
from game.CLI import show_cli_action_menu
from game.player import Player
import random




def main():

    day_survived = 0
    player = Player("Survivant")
    while True:

        show_cli_action_menu()
        choice = input("Votre choix: ").strip().lower()


        if choice == "1":
            player.fish()
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
                reponse = input().strip().lower()
                if reponse in ("yes", "y", "oui", "o"):
                    if random_event == 0:  # casino
                        player.modify_hunger(5)
                        player.modify_energy(-10)
                        print("Vous entrez dans le casino.")
                    elif random_event == 1:  # school
                        player.modify_energy(10)
                        print("Vous entrez dans l'école.")
                    elif random_event == 2:  # hospital
                        player.modify_energy(20)
                        player.modify_thirst(-10)
                        print("Vous entrez dans l'hôpital.")
                    elif random_event == 3:  # police station
                        player.modify_energy(5)
                        print("Vous entrez dans le poste de police.")
                    elif random_event == 4:  # house store
                        player.modify_hunger(-15)
                        player.modify_thirst(-10)
                        print("Vous entrez dans le magasin.")
                    break
                elif reponse in ("no", "n", "non"):
                    print("Vous continuez votre chemin.")
                    break
                else:
                    print("Réponse invalide. Tapez 'yes' ou 'no'.")
        elif choice == "q":
            print("Quit.")
            break
        else:
            print("Choix invalide, réessayez.")
            continue

        show_cli_status(player, day_survived)


        if day_survived == 60:
            print(f"Félicitations! {player.name} a survécu 60 jours!")
            break

        if not player.is_alive:
            print(f"{player.name} est mort. Fin du jeu.")
            break
