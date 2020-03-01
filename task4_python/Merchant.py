from Pos import Pos


class Merchant:
    def __init__(self):
        self.elixir_price = 1
        self.shield_price = 2
        self.pos = Pos()

    def action_on_soldier(self, soldier):
        buy_enabled = True

        while buy_enabled:
            self.talk('Do you want to buy something? (1. Elixir, 2. Shield, 3. Leave.) Input: ')

            choice = input()

            if choice == '1':
                if soldier.get_coin() >= self.elixir_price:
                    soldier.use_coin(self.elixir_price)
                    soldier.add_elixir()
                    print('You have bought an Elixir.\n')
                else:
                    self.talk('You don\'t have enough coins.\n\n')
                buy_enabled = False
            elif choice == '2':
                if soldier.get_coin() >= self.shield_price:
                    soldier.use_coin(self.shield_price)
                    soldier.add_shield()
                    print('You have bought a Shield.\n')
                else:
                    self.talk('You don\'t have enough coins.\n\n')
                buy_enabled = False
            elif choice == '3':
                buy_enabled = False
            else:
                print('=> Illegal choice!\n')

    def get_pos(self):
        return self.pos

    def set_pos(self, row, column):
        self.pos.set_pos(row, column)

    def talk(self, text):
        print('Merchant$:', text, end='')

    def display_symbol(self):
        print('$', end='')
