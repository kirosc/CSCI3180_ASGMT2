from Pos import Pos


class Spring:
    def __init__(self):
        self.num_chance = 1
        self.healing_power = 100
        self.pos = Pos()

    def set_pos(self, row, column):
        self.pos.set_pos(row, column)

    def get_pos(self):
        return self.pos

    def talk(self):
        print('Spring@: You have {} chance to recover 100 health.\n'.format(self.num_chance))

    def action_on_soldier(self, soldier):
        self.talk()
        if self.num_chance == 1:
            soldier.recover(self.healing_power)
            self.num_chance -= 1

    def display_symbol(self):
        print('@')
