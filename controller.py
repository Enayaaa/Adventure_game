import world
import player
import sys


# Initialize Game Variables
w = world.World()
p = player.Player(0, 0)

print()
print("𝕎𝕖𝕝𝕔𝕠𝕞𝕖 𝕥𝕠 𝕋𝕙𝕚𝕤 𝕒𝕕𝕧𝕖𝕟𝕥𝕦𝕣𝕖 𝕘𝕒𝕞𝕖!")
print("_________________________________________")
print("Ｕｓｅ ｔｈｅ ｆｏｌｌｏｗｉｎｇ ｃｏｍｍａｎｄｓ ｔｏ ｅｘｐｌｏｒｅ ｔｈｅ ｗｏｒｌｄ：")
print(
    "w - move up\ns - move down\na - move left\nd - move right\nlook - explore the current place"
    "\nlisten - listen for sounds\ndestroy - destroy building at current place"
    "\nitems - list items at current place\ninventory - list items in inventory"
    "\nplace item [index] - place item at index from inventory at place"
    "\npickup item [index] - pickup item at index from item into inventory"
    "\nquit - quit game"
)
print("_________________________________________")


def handle_event():
    command = input().lower()

    if command == "quit":
        sys.exit()
    elif command == "look":
        print(p.look(w.places))
    elif command == "listen":
        print(p.listen(w.places))
    elif command == "destroy":
        print(w.destroy_build(p.x, p.y))
    elif command == "items":
        print(w.places[p.x][p.y].items)
    elif command == "inventory":
        print(p.inventory)
    elif command.startswith("place item") and len(command) > len("place item") + 1:
        p.place_item(w.places, int(command.split(" ")[-1]))
    elif command.startswith("pickup item") and len(command) > len("pickup item") + 1:
        p.pickup_item(w.places, int(command.split(" ")[-1]))
    else:
        p.move(command)


# Main program loop
while True:
    print()
    print("Current place %s (%d, %d)" % (p.get_place_name(w.places), p.x, p.y))

    # Handle commands
    handle_event()

    # Handle index out of range
    if p.x < 0:
        p.x = len(w.places) - 1
    if p.x > len(w.places) - 1:
        p.x = 0
    if p.y < 0:
        p.y = len(w.places[0]) - 1
    if p.y > len(w.places[0]) - 1:
        p.y = 0
