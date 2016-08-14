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

    def battlecry(self):
        return self.sound.upper()

class Store():
    open = 9
    close = 5

    def hours(self):
        return ("We're open from {} to {}".format(self.open, self.close))