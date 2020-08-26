
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.inventory = []

    def get_place_name(self, places):
        return places[self.x][self.y].name

    def move(self, command):
        if command == "w":
            self.y -= 1
        elif command == "s":
            self.y += 1
        elif command == "a":
            self.x -= 1
        elif command == "d":
            self.x += 1
        else:
            return

    def look(self, places):
        current_place = places[self.x][self.y]
        return "The weather at this place is " + current_place.weather.lower() + ".\n"\
               + "The people at this place speak the strange language of "\
               + current_place.language + "\nand the view is " + current_place.veiw.lower()\
               + " as far as the eye can see."

    def listen(self, places):
        current_place = places[self.x][self.y]
        return "If you listen closely, you can hear " + current_place.sound
