import sys


def get_array(txt_file):
    the_board = []
    with open(f"{txt_file}", "r") as file:
        for line in file:
            cleaned_line = [elmt.replace(" ", "-") for elmt in line]
            the_board.append((list(cleaned_line)))
    for lines in the_board:
        for line_break in lines:
            if line_break == "\n":
                lines.pop(lines.index(line_break))
    return the_board

def removing_elmt(board, to_find):
    for lines in range(len(board)):
        for cols in range(len(board[lines])):
            if all(not board[lines][cols] in elmt
                   for rows in range(len(to_find))
                   for elmt in to_find[rows]):
                board[lines][cols] = "-"
    return board

def localisation(board, to_find):
    found = False
    for x in range(len(board) - len(to_find) + 1):
        for y in range(len(board[x]) - len(to_find[0]) + 1):
            for x_to_find in range(len(to_find)):
                if board[x + x_to_find][y: y + len(to_find[x_to_find])] == to_find[x_to_find]:
                    found = True
                else:
                    found = False
            if found:
                print("Trouvé !")
                return y, x
    if not found:
        print(board)
        return "Introuvable"

if len(sys.argv) != 3:
    print("Put only two .txt files")
    sys.exit()
if sys.argv[1][-4:] != ".txt" or sys.argv[2][-4:] != ".txt":
    print("You should put two .txt files")
    sys.exit()

board_file = sys.argv[1]
to_find_file = sys.argv[2]

to_find = get_array(to_find_file)
board = removing_elmt(get_array(board_file), to_find)

resultat = localisation(board, to_find)
print("Coordonnées :", resultat)