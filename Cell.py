class Cell:
    def __init__(self):
        self.occupied_object = None

    def get_occupied_object(self):
        return self.occupied_object

    def set_occupied_object(self, occupied_object):
        self.occupied_object = occupied_object
