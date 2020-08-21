
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.inventory = []

    def get_place_name(self, places):
        return places[self.x][self.y].name