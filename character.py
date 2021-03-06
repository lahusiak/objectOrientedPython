import random
from combat import(Combat)

class Character(Combat):

    experience = 0
    base_hit_points = 10
    attack_limit = 10

    def attack(self):
        roll = random.randint(1, self.attack_limit)
        print(roll)
        if self.weapon == 'sword':
            roll += 1
        elif self.weapon == 'axe':
            roll += 2
        return roll > 4

    def get_weapon(self):
        self.weapon = raw_input("Weapon: [S]word, [A]xe, [B]ow >> ").lower()
        if self.weapon == "s":
            return "sword"
        elif self.weapon == "a":
            return "axe"
        elif self.weapon == "b":
            return "bow"
        else:
            self.get_weapon()

    def __init__(self, **kwargs):
        self.name = raw_input("Name: ")
        self.weapon = self.get_weapon()
        self.hit_points = self.base_hit_points

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return "{}, HP: {}, XP: {}".format(self.name, self.hit_points, self.experience)

    def rest(self):
        if self.hit_points < 10:
            self.hit_points += 1

    def leveled_up(self):
        return self.experience >= 5
