from Cell import Cell


class Map:
    def __init__(self):
        self.cells = [[Cell() for j in range(7)] for i in range(7)]

    def add_object(self, object):
        if type(object) == list:
            for monster in object:
                pos = object.get_pos
                self.cells[pos.get_row() - 1][pos.get_column() - 1].set_occupied_object(monster)
        else:
            pos = object.get_pos()
            self.cells[pos.get_row() - 1][pos.get_column() - 1].set_occupied_object(object)

    def display_map(self):
        print('   | 1 | 2 | 3 | 4 | 5 | 6 | 7 |')
        print('--------------------------------')
        for i, row in enumerate(self.cells):
            print(' {} |'.format(i + 1), end='')
            for cell in row:
                occupied_object = cell.get_occupied_object()
                if occupied_object is not None:
                    print(' ', end='')
                    occupied_object.display_symbol()
                    print(' |', end='')
                else:
                    print('   |', end='')
            print('')
            print('--------------------------------')
        print('')

    def get_occupied_object(self, row, column):
        return self.cells[row - 1][column - 1].get_occupied_object()

    def check_move(self, row, column):
        return (1 <= row <= 7) and (1 <= column <= 7)

    def update(self, soldier, old_row, old_column, new_row, new_column):
        self.cells[old_row - 1][old_column - 1].set_occupied_object(None)
        self.cells[new_row - 1][new_column - 1].set_occupied_object(soldier)
