import random


def daylies_event(player):
    events = [
        {"description": "Il pleut abondamment, votre soif diminue.", "thirst_effect": -10, "hunger_effect": 0,
         "energy_effect": 0},
        {"description": "Il fait très chaud, votre soif augmente.", "thirst_effect": 15, "hunger_effect": 0,
         "energy_effect": -5},
        {"description": "Temps nuageux, rien ne change.", "thirst_effect": 0, "hunger_effect": 0, "energy_effect": 0},
        {"description": "Vous trouvez une source d'eau, votre soif diminue.", "thirst_effect": -20, "hunger_effect": 0,
         "energy_effect": 5},
        {"description": "Vous marchez sous le soleil, votre soif augmente et votre énergie diminue.",
         "thirst_effect": 10, "hunger_effect": 0, "energy_effect": -10},
        {"description": "Vous trouvez de la nourriture, votre faim diminue.", "thirst_effect": 0, "hunger_effect": -15,
         "energy_effect": 5},
        {"description": "Vous êtes épuisé, votre énergie diminue fortement.", "thirst_effect": 0, "hunger_effect": 0,
         "energy_effect": -20},
    ]

    event = random.choice(events)
    print(event["description"])
    player.modify_thirst(event["thirst_effect"])
    player.modify_hunger(event["hunger_effect"])
    player.modify_energy(event["energy_effect"])
