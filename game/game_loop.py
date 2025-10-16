
from game.player import Player

def print_status(p: Player):
    print(f"\nÉtat de {p.name} - faim: {p.hunger}, soif: {p.thirst}, énergie: {p.energy}, vivant: {p.is_alive}\n")

def main():
    player = Player("Survivant")
    while True:
        print("="*30)
        print("Statut actuel:")
        print_status(player)
        print("="*30)
        print("Choisissez une action :")
        print("1 - fish")
        print("2 - sleep")
        print("3 - look for water")
        print("q - quitter")
        choice = input("Votre choix: ").strip().lower()

        if choice == "1":
            player.fish()
        elif choice == "2":
            player.sleep()
        elif choice == "3":
            player.look_for_water()
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


