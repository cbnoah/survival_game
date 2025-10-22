from game.player import Player
import random


def print_status(p: Player):
    print(f"\nÉtat de {p.name} - faim: {p.hunger}, soif: {p.thirst}, énergie: {p.energy}, vivant: {p.is_alive}\n")


def main():
    player = Player("Survivant")
    while True:
        print("=" * 30)
        print("Statut actuel:")
        print_status(player)
        print("=" * 30)
        print("Choisissez une action :")
        print("1 - fish")
        print("2 - sleep")
        print("3 - look for water")
        print("4 - random event")
        print("q - quitter")
        choice = input("Votre choix: ").strip().lower()

        if choice == "1":
            player.fish()
        elif choice == "2":
            player.sleep()
        elif choice == "3":
            player.look_for_water()
        elif choice == "4":
            random_event = random.randint(0, 4)
            player.explore(random_event)

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

        print_status(player)

        if not player.is_alive:
            print(f"{player.name} est mort. Fin du jeu.")
            break
