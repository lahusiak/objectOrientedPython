from character import Character
from monster import Goblin
from monster import Goose
from monster import Troll
from monster import Witch

class Game:
    def set_up(self):
        self.player = Character()
        self.monsters = [
            Goblin(),
            Goose(),
            Troll(),
            Witch()
        ]
        self.monster = self.get_next_monster()

    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        # check to see if monster attacks
        if self.monsters.attack == True:
            print(input("Would you like to dodge? Y/n" ))
            if input == 'y':


        # If so, tell the player
            # Check if the player wants to dodge
            # If so, see if the dodge is successful
        # If it's not, remove one player hit point
        # If the monster isn't attacking tell that to the player too.

    def player_turn(self):
        # let the player attack, rest, or quit
        # If they attack:
            # See if attack is successful
            # If it is, see if the monster dodges
            # If not dodged, subtract the right num of hit points from the monster
            # If not a good attack, tell the player
        # If they rest:
            # call player.rest()
        # If the quit:
            # Exit the game
        # If they pick anything else, rerun player_turn

    def clean_up(self):
        # If the monster has not more hit points:
        # Up the players experience
        # print a message
        # get a new monster

    def __init__(self):
        print(self.player)
        self.set_up()

        while self.player and (self.monster or self.monsters):
            self.monster.turn()
            self.player_turn()
            self.clean_up()

        if self.player.hit_points:
            print("You win!")
        elif self.monsters or self.monster:
            print("You lose!")




