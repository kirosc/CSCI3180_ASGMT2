from Pos import Pos
from random import randint


class Soldier:
    def __init__(self):
        self.health = 100
        self.num_elixirs = 2
        self.pos = Pos()
        self.keys = set()

    def get_health(self):
        return self.health

    def lose_health(self):
        self.health -= 10
        return self.health <= 0

    def recover(self, healing_power):
        total_health = healing_power + self.health
        self.health = 100 if total_health >= 100 else total_health

    def get_pos(self):
        return self.pos

    def set_pos(self, row, column):
        self.pos.set_pos(row, column)

    def move(self, row, column):
        self.set_pos(row, column)

    def get_keys(self):
        return self.keys

    def add_keys(self, key):
        self.keys.add(key)

    def get_num_elixirs(self):
        return self.num_elixirs

    def add_elixir(self):
        self.num_elixirs += 1

    def use_elixir(self):
        self.recover(randint(15, 20))
        self.num_elixirs -= 1

    def display_information(self):
        print('Health:', self.health)
        print('Position (row, column): ({}, {}).'.format(self.pos.get_row(), self.pos.get_column()))
        print('Keys:', self.keys)
        print('Elixirs:', self.num_elixirs)

    def display_symbol(self):
        print('S')
