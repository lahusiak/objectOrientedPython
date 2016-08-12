class Monster():

    def __init__(self, **kwargs):
        self.hit_point = kwargs.get('hit_point', 1)
        self.color = kwargs.get('color', 'yellow')
        self.weapon = kwargs.get('weapon', 'sword')
        self.sound = kwargs.get('sound', 'roar')

    def battlecry(self):
        return self.sound.upper()

class Store():
    open = 9
    close = 5

    def hours(self):
        return ("We're open from {} to {}".format(self.open, self.close))