import sys

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
    def got_hit(self):
        self.player.hit_points -= 1

    def monster_turn(self):
        # check to see if monster attacks
        if self.monster.attack():
            print("{} is attacking!".format(self.monster))

            if raw_input("Would you like to dodge? Y/n > ").lower() == 'y':
                if self.player.dodge():
                    print("You dodged the attack!")
                else:
                    print("{} hit you anyway".format(self.monster))
                    self.got_hit()
            else:
                print("{} hit you for 1 point".format(self.monster))
                self.got_hit()

    def player_turn(self):
        player_action = raw_input("What would you like to do? [A]ttack, [R]est, [Q]uit > ").lower()

        if player_action == 'a':
            print("You've attacked {}!".format(self.monster))

            if self.player.attack():
                if self.monster.dodge():
                    print("{} dodged your attack".format(self.monster))
                else:
                    print("You attacked {} with your {}".format(self.monster, self.player.weapon))
                    if self.player.leveled_up():
                        self.monster.hit_points -=2
                    else:
                        self.monster.hit_points -=1
            else:
                print("You missed!")

        elif player_action == 'r':
            print("You've decided to take a rest")
            self.player.rest()
        elif player_action =='q':
            print("Thanks for playing")
            sys.exit()
        else:
            self.player_turn()

    def clean_up(self):
        if self.monster.hit_points <= 0:
            self.player.experience += self.monster.experience
            print("You killed {}".format(self.monster))
            self.monster = self.get_next_monster()

    def __init__(self):
        self.set_up()

        while self.player and (self.monster or self.monsters):
            print('\n'+'='*20)
            print(self.player)
            self.monster_turn()
            print('\n' + '=' * 20)
            self.player_turn()
            self.clean_up()
            print('\n' + '=' * 20)

        if self.player.hit_points:
            print("You win!")
        elif self.monsters or self.monster:
            print("You lose!")
        sys.exit()

Game()


