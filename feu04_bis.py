import sys
from random import random

# Générateur de plateau
def plat_generator(x, y, density):
    plateau = []
    for i in range(y):
        row = []
        for j in range(x):
            cell = ['x' if random() > density else '.']
            row.append(cell)
        plateau.append(row)
    return plateau

def plateau_to_file(board, height):
    with open('plateau.txt', 'w') as file:
        file.write(f'{height}.xo')
        file.write('\n')
        for rows in board:
            for colums in rows:
                file.write("".join(colums))
            file.write('\n')

if len(sys.argv) != 4:
    sys.exit('Params needed x y density')

x = int(sys.argv[1])
y = int(sys.argv[2])
density = float(sys.argv[3])

plateau = plat_generator(x, y, density)
plateau_to_file(plateau, y)

f = open('plateau.txt', 'r')
print(f.read())
f.close()
