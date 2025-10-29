# game/daylies_event.py
import random


def daylies_event(player):
    events = [
        {"description": "Il pleut abondamment, votre soif diminue.", "thirst_effect": -10, "hunger_effect": 0,
         "energy_effect": 0, "type": "passive"},
        {"description": "Il fait très chaud, votre soif augmente.", "thirst_effect": 15, "hunger_effect": 0,
         "energy_effect": -5, "type": "passive"},
        {"description": "Temps nuageux, rien ne change.", "thirst_effect": 0, "hunger_effect": 0, "energy_effect": 0,
         "type": "passive"},
        {"description": "Vous trouvez une source d'eau, votre soif diminue.", "thirst_effect": -20, "hunger_effect": 0,
         "energy_effect": 5, "type": "passive"},
        {"description": "Vous marchez sous le soleil, votre soif augmente et votre énergie diminue.",
         "thirst_effect": 10, "hunger_effect": 0, "energy_effect": -10, "type": "passive"},
        {"description": "Vous trouvez de la nourriture, votre faim diminue.", "thirst_effect": 0, "hunger_effect": -15,
         "energy_effect": 5, "type": "passive"},
        {"description": "Vous êtes épuisé, votre énergie diminue fortement.", "thirst_effect": 0, "hunger_effect": 0,
         "energy_effect": -20, "type": "passive"},
        {"description": "Vous rencontrez un animal sauvage!", "type": "hunt"}
    ]

    event = random.choice(events)
    print(event["description"])

    if event["type"] == "passive":
        player.modify_thirst(event["thirst_effect"])
        player.modify_hunger(event["hunger_effect"])
        player.modify_energy(event["energy_effect"])
    elif event["type"] == "hunt":
        while True:
            choice = input("Voulez-vous le chasser? (yes/no): ").strip().lower()
            if choice in ("yes", "y", "oui", "o"):
                player.modify_energy(-15)
                print("Vous chassez l'animal et perdez de l'énergie...")
                if random.random() < 0.5:
                    print("Vous avez attrapé l'animal! Votre faim diminue.")
                    player.modify_hunger(-25)
                else:
                    print("L'animal s'est échappé.")
                break
            elif choice in ("no", "n", "non"):
                print("Vous laissez l'animal partir.")
                break
            else:
                print("Réponse invalide. Tapez 'yes' ou 'no'.")
