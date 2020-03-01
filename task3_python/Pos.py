class Pos:
    def __init__(self, row=None, column=None):
        self.row = row
        self.column = column

    def set_pos(self, row, column):
        self.row = row
        self.column = column

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column
