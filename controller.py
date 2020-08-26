import world
import player
import sys

w = world.World()
p = player.Player(0, 0)

print()
print("𝕎𝕖𝕝𝕔𝕠𝕞𝕖 𝕥𝕠 𝕋𝕙𝕚𝕤 𝕒𝕕𝕧𝕖𝕟𝕥𝕦𝕣𝕖 𝕘𝕒𝕞𝕖!")
print("_________________________________________")
print("Ｕｓｅ ｔｈｅ ｆｏｌｌｏｗｉｎｇ ｃｏｍｍａｎｄｓ ｔｏ ｅｘｐｌｏｒｅ ｔｈｅ ｗｏｒｌｄ：")
print(
    "w - move up\ns - move down\na - move left\nd - move right\nlook - explore the current place"
    "\nlisten - listen for sounds\nquit - quit game"
)
print("_________________________________________")


def handle_command():
    command = input().lower()

    if command == "quit":
        sys.exit()
    elif command == "look":
        print(p.look(w.places))
    elif command == "listen":
        print(p.listen(w.places))
    else:
        p.move(command)


# Main program loop
while True:
    print()
    print("Current place %s (%d, %d)" % (p.get_place_name(w.places), p.x, p.y))
    '''
        print("Debug")
        for i in range(len(w.places)):
            for j in range(len(w.places[i])):
                print(j, i, w.places[j][i].name)
        '''

    # Handle commands
    handle_command()

    # Handle index out of range
    if p.x < 0:
        p.x = len(w.places) - 1
    if p.x > len(w.places) - 1:
        p.x = 0
    if p.y < 0:
        p.y = len(w.places[0]) - 1
    if p.y > len(w.places[0]) - 1:
        p.y = 0
