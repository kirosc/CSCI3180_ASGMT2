from Soldier import Soldier


class Task4Soldier(Soldier):
    def __init__(self):
        super().__init__()
        self.num_coins = 0
        self.defense_value = 0

    def add_shield(self):
        self.defense_value += 5

    def get_coin(self):
        return self.num_coins

    def add_coin(self):
        self.num_coins += 1

    def use_coin(self, number):
        self.num_coins -= number

    def display_information(self):
        super().display_information()
        print('Defence:', self.defense_value)
        print('Coins:', self.num_coins)

    def lose_health(self):
        self.health += min(self.defense_value, 10)
        return super().lose_health()
