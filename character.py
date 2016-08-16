class Character:

    experience = 0
    hit_points = 10

    def get_weapon(self):
        self.weapon = input("Weapon: [S]word, [A]xe, [B]ow ").lower()
        if self.weapon in ('sab'):
            if self.weapon == 's':
                return 'sword'
            elif self.weapon == 'a':
                return 'axe'
            elif self.weapon == 'b':
                return 'bow'
            else:
                self.get_weapon()

    def __init__(self, **kwargs):
        self.name = input("Name: ")
        self.weapon = self.get_weapon()

        for key, value in kwargs.items():
            setattr(self, key, value)
