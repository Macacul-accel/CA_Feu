# Générateur de labyrinthe

import sys
from random import randrange

def lab_generator(height, width, characters):
    empty_space = characters[1]
    wall = characters[0]
    gate_1 = characters[3]
    gate_2 = characters[4]
    labyrinthe = []
    entry_1 = randrange(width - 4) + 2
    entry_2 = randrange(width - 4) + 2
    labyrinthe.append(f'{height}x{width}{characters}')
    for x in range(height):
        row = []
        for y in range(width):
            if x == 0 and y == entry_1:
                row.append(gate_2)
            elif x == height - 1 and y == entry_2:
                row.append(gate_1)
            elif x in range(1, height - 1) and y in range(1, width - 1) and randrange(100) > 25:
                row.append(empty_space)
            else:
                row.append(wall)
        labyrinthe.append(row)
    return labyrinthe

def get_lab(laby):
    with open('labyrinthe.map', 'w') as file:
        for rows in laby:
            for colums in rows:
                file.write("".join(colums))
            file.write('\n')

#Error handling
if len(sys.argv) != 4:
    sys.exit("Params needed: height width 'characters'")
if len(sys.argv[-1]) < 4:
    sys.exit("Characters params needed: 'empty path wall gates'")

height = int(sys.argv[1])
width = int(sys.argv[2])
characters = sys.argv[3]

new_labyrinthe = lab_generator(height, width, characters)
get_lab(new_labyrinthe)

f = open('labyrinthe.txt', 'r')
print(f.read())
f.close()
# input should look like : "int int ' o12'"