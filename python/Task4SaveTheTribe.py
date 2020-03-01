from random import randrange
from Map import Map
from Task4Soldier import Task4Soldier
from Spring import Spring
from Merchant import Merchant
from Task4Monster import Task4Monster


class SaveTheTribe:
    def __init__(self):
        self.map = Map()
        self.soldier = Task4Soldier()
        self.spring = Spring()
        self.merchant = Merchant()
        self.monsters = [None] * 7
        self.game_enabled = True

    def initialize(self):
        self.monsters[0] = Task4Monster(1, randrange(30, 71, 10))
        self.monsters[0].set_pos(4, 1)
        self.monsters[0].add_drop_item(2)
        self.monsters[0].add_drop_item(3)

        self.monsters[1] = Task4Monster(2, randrange(30, 71, 10))
        self.monsters[1].set_pos(3, 3)
        self.monsters[1].add_drop_item(3)
        self.monsters[1].add_drop_item(6)
        self.monsters[1].add_hint(1)
        self.monsters[1].add_hint(5)

        self.monsters[2] = Task4Monster(3, randrange(30, 71, 10))
        self.monsters[2].set_pos(5, 3)
        self.monsters[2].add_drop_item(4)
        self.monsters[2].add_hint(1)
        self.monsters[2].add_hint(2)

        self.monsters[3] = Task4Monster(4, randrange(30, 71, 10))
        self.monsters[3].set_pos(5, 5)
        self.monsters[3].add_hint(3)
        self.monsters[3].add_hint(6)

        self.monsters[4] = Task4Monster(5, randrange(30, 71, 10))
        self.monsters[4].set_pos(1, 4)
        self.monsters[4].add_drop_item(2)
        self.monsters[4].add_drop_item(6)

        self.monsters[5] = Task4Monster(6, randrange(30, 71, 10))
        self.monsters[5].set_pos(3, 5)
        self.monsters[5].add_drop_item(4)
        self.monsters[5].add_drop_item(7)
        self.monsters[5].add_hint(2)
        self.monsters[5].add_hint(5)

        self.monsters[6] = Task4Monster(7, randrange(30, 71, 10))
        self.monsters[6].set_pos(4, 7)
        self.monsters[6].add_drop_item(-1)
        self.monsters[6].add_hint(6)

        self.map.add_object(self.monsters)

        self.soldier.set_pos(1, 1)
        self.soldier.add_keys(1)
        self.soldier.add_keys(5)

        self.map.add_object(self.soldier)

        self.spring.set_pos(7, 4)

        self.map.add_object(self.spring)

        self.merchant.set_pos(7, 7)

        self.map.add_object(self.merchant)

    def start(self):
        print('=> Welcome to the desert!')
        print('=> Now you have to defeat the monsters and find the artifact to save the tribe.\n')

        while self.game_enabled:
            self.map.display_map()
            self.soldier.display_information()

            move = input('\n=> What is the next step? (W = Up, S = Down, A = Left, D = Right.) Input: ')

            pos = self.soldier.get_pos()
            new_row = old_row = pos.get_row()
            new_column = old_column = pos.get_column()

            if move.upper() == 'W':
                new_row = old_row - 1
            elif move.upper() == 'S':
                new_row = old_row + 1
            elif move.upper() == 'A':
                new_column = old_column - 1
            elif move.upper() == 'D':
                new_column = old_column + 1
            else:
                print('=> Illegal move!\n')
                continue

            if self.map.check_move(new_row, new_column):
                occupied_object = self.map.get_occupied_object(new_row, new_column)

                if occupied_object is not None:
                    occupied_object.action_on_soldier(self.soldier)
                else:
                    self.soldier.move(new_row, new_column)
                    self.map.update(self.soldier, old_row, old_column, new_row, new_column)
                    print('\n')
            else:
                print('=> Illegal move!\n')

            if self.soldier.get_health() <= 0:
                print('=> You died.')
                print('=> Game over.\n')
                self.game_enabled = False

            if -1 in self.soldier.get_keys():
                print('=> You found the artifact.')
                print('=> Game over.\n')
                self.game_enabled = False


game = SaveTheTribe()
game.initialize()
game.start()
