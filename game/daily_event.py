import random


def daily_event(player):
    events = [
        {"description": "It's raining cats and dogs out there, your thirst goes down", "thirst_effect": -10, "hunger_effect": 0,
         "energy_effect": 0, "type": "passive"},
        {"description": "It's really hot, you're getting dehydrated and tired", "thirst_effect": 15, "hunger_effect": 0,
         "energy_effect": -5, "type": "passive"},
        {"description": "Cloudy sky today, nothing changes", "thirst_effect": 0, "hunger_effect": 0, "energy_effect": 0,
         "type": "passive"},
        {"description": "You've found a drinkable water source, your thirst goes down", "thirst_effect": -20, "hunger_effect": 0,
         "energy_effect": 5, "type": "passive"},
        {"description": "You're walking under the sun for hours, you feel very thirsty and tired.",
         "thirst_effect": 10, "hunger_effect": 0, "energy_effect": -10, "type": "passive"},
        {"description": "You've found food, your hunger goes down", "thirst_effect": 0, "hunger_effect": -15,
         "energy_effect": 5, "type": "passive"},
        {"description": "You are really tired, your energy goes down significantly", "thirst_effect": 0, "hunger_effect": 0,
         "energy_effect": -20, "type": "passive"},
        {"description": "You have encountered a wild animal!", "type": "hunt"}
    ]

    event = random.choice(events)
    print(event["description"])

    if event["type"] == "passive":
        player.modify_thirst(event["thirst_effect"])
        player.modify_hunger(event["hunger_effect"])
        player.modify_energy(event["energy_effect"])
    elif event["type"] == "hunt":
        while True:
            choice = input("Do you want to hunt it? (yes/no): ").strip().lower()
            if choice in ("yes", "y", "oui", "o"):
                player.modify_energy(-15)
                print("You attempt to hunt the animal...")
                if random.random() < 0.5:
                    print("You successfully hunted the animal and gained food! (your hunger decreases)")
                    player.modify_hunger(-25)
                else:
                    print("The animal got away!")
                break
            elif choice in ("no", "n", "non"):
                print("You let the animal go.")
                break
            else:
                print("Invalid choice. Please enter yes or no.")
