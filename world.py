import place


class World:
    def __init__(self):
        self.places = []
        self.create(2)

    def create(self, height):
        for x in range(height):
            self.places.append([])
        self.places[0].append(place.Place("North West", "cool", "Norse", "snow white", "snow pattering"))
        self.places[1].append(place.Place("North East", "chilly", "Swedish", "small bushes", "wind howling"))
        self.places[0].append(place.Place("South West", "sunny", "Spanish", "green trees", "birds chirping"))
        self.places[1].append(place.Place("South East", "flaming hot", "Persian", "desert", "vultures calling"))
