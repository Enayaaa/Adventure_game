import place

class World:

    def __init__(self):
        self.places = [[],[]]
        self.create()

    def create(self):
        self.places[0].append(place.Place("North West", "Cool", "Northy", "Snow white"))
        self.places[1].append(place.Place("North East", "Chilly", "Northy", "oeof"))
        self.places[0].append(place.Place("South West", "Sunny", "piefp", "Green trees"))
        self.places[1].append(place.Place("South East", "Flamming hot", "persain", "Desert"))


