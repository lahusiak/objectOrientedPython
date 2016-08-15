import random

COLORS = ['yellow', 'red', 'green', 'blue', 'purple']


class Monster():
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1
    weapon = 'sword'
    sound = 'roar'

    def __init__(self, **kwargs):
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
        self.experience = random.randint(self.min_experience, self.max_experience)
        self.colors = random.choice(COLORS)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return('{}, {} HP: {} XP: {}'.format(self.color.title(),
                                             self.__class__.__name__,
                                             self.hit_points,
                                             self.experience)

        )

    def battlecry(self):
        return self.sound.upper()

class Goblin(Monster):
    min_hit_points = 1
    max_hit_points = 4
    sound = 'squak'

class Troll(Monster):
    min_hit_points = 1
    max_hit_points = 4
    sound = 'heheheheh'

class Goose(Monster):
    min_hit_points = 3
    max_hit_points = 9
    sound = 'blarg'

class Witch(Monster):
    min_hit_points = 2
    max_hit_points = 7
    sound = 'eeeeee'
    color = 'purple'

class Store():
    open = 9
    close = 5

    def hours(self):
        return ("We're open from {} to {}".format(self.open, self.close))