import random

from game.player import Player


class Environment:
    def __init__(self, player: Player, is_in_cli: bool = True):
        self.player = player
        self.is_in_cli = is_in_cli

    def random_event(self):
        event = random.randint(0, 2)
        match event:
            case 0:
                self.rain()
                if self.is_in_cli:
                    # CLI feedback
                    pass
                else:
                    pass
            case 1:
                if self.is_in_cli:
                    # CLI feedback
                    pass
                else:
                    pass
                self.animal_encounter(True)
            case 2:
                if self.is_in_cli:
                    # CLI feedback
                    pass
                else:
                    pass
                self.new_resources()

    def rain(self):
        self.player.modify_thirst(-20)

    def animal_encounter(self, fight: bool):
        result = random.randint(0, 50)
        if result > 25:
            if fight: # The player fought the animal and won
                self.player.modify_energy(-20)
                self.player.modify_hunger(-20)
            else: # The player ran away from the animal successfully
                self.player.modify_energy(-30)
                self.player.modify_thirst(20)
        else:
            if fight: # The player fought the animal and lost
                self.player.modify_energy(-40)
                self.player.modify_hunger(10)
                self.player.modify_thirst(10)
            else: # The player ran away from the animal but got hurt
                self.player.modify_energy(-60)
                self.player.modify_hunger(20)
                self.player.modify_thirst(30)


    def new_resources(self):
        result = random.randint(0, 50)
        if result > 25: # The player found new food
            self.player.modify_hunger(-30)
        else:
            self.player.modify_hunger(30)