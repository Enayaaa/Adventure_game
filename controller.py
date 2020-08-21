import world
import player
import pprint

# main loop
# skapa värld med places
# låt användaren ge input

w = world.World()
p = player.Player(0, 0)

while True:
    print("You are at %s" % p.get_place_name(w.places))
    print("Coordinates: (%d, %d)" % (p.x, p.y))
    command = input("___________\nCommands:\n___________\nw - move up\ns - move down\na - move left\nd - move right\nquit - quit game\n").lower()
    '''
    print("Debug")
    for i in range(len(w.places)):
        for j in range(len(w.places[i])):
            print(j, i, w.places[j][i].name)
    '''
    if command == "quit":
        break
    elif command == "w":
        p.y -= 1
    elif command == "s":
        p.y += 1
    elif command == "a":
        p.x -= 1
    elif command == "d":
        p.x += 1
    else:
        continue

    if p.x < 0:
        p.x = len(w.places) - 1
    if p.x > len(w.places) - 1:
        p.x = 0
    if p.y < 0:
        p.y = len(w.places[0]) - 1
    if p.y > len(w.places[0]) - 1:
        p.y = 0