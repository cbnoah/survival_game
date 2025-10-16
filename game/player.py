class Player:
    def __init__(self, name, hunger=0, thirst=0, energy=0):
        self.name = name
        self.hunger = hunger
        self.thirst = thirst
        self.energy = energy
        self.is_alive = True

    def modify_hunger(self, hunger):
        self.hunger += hunger
        if self.hunger > 100:
            self.hunger = 100
            self.is_alive = False
        if self.hunger < 0:
            self.hunger = 0
        return

    def modify_thirst(self, thirst):
        self.thirst += thirst
        if self.thirst > 100:
            self.thirst = 100
            self.is_alive = False
        if self.thirst < 0:
            self.thirst = 0
        return

    def modify_energy(self, energy):
        self.energy += energy
        if self.energy > 100:
            self.energy = 100
        if self.energy < 0:
            self.energy = 0
            self.is_alive = False
        return

    def fish(self):
        self.modify_hunger(-30)
        self.modify_energy(-20)


    def look_for_water(self):
        self.modify_thirst(-20)
        self.modify_energy(-15)

    def sleep(self):
        self.modify_energy(60)
        self.modify_hunger(20)
        self.modify_thirst(20)