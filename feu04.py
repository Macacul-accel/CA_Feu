import sys

def get_plateau(file):
    plateau_board = []
    with open(f'{file}', 'r') as plateau_file:
        for rows in plateau_file:
            plateau_board.append(list(rows.strip()))
    return plateau_board

def find_square(board, max_size):
    obstacle = board[0][-2]
    found = False
    for x in range(1, len(board[1:]) - max_size + 2):
        for y in range (len(board[1]) - max_size + 1):
            if all(not obstacle in board[square + x][y:y + max_size]
                for square in range(max_size)):
                found = True
                return x, y, max_size
            found = False
    if not found:
        return find_square(board, max_size - 1)

def draw_square(board, pos):
    x = pos[0]
    y = pos[1]
    size = pos[2]
    empty_space = board[0][-3]
    square_form = board[0][-1]
    for rows in range(x, x + size):
        for cols in range(y, y + size):
            if board[rows][cols] == empty_space:
                board[rows][cols] = square_form
    return board[1:]

def check_rows_size(board):
    row_len = len(board[1])
    for row in board[2:]:
        if len(row) != row_len:
            return False
    return True

# Error handling
if len(sys.argv) != 2:
    sys.exit('You can only put one .txt file')
if sys.argv[1][-4:] != '.txt':
    sys.exit('Put plateau.txt')
if not check_rows_size(get_plateau(sys.argv[1])):
    sys.exit('Your board is not valid')

txt_file = sys.argv[1]

plateau = get_plateau(txt_file)
square_max_size = min(len(plateau[1:]), len(plateau[1]))
position = find_square(plateau, square_max_size)
result = draw_square(plateau, position)

for j in result:
    print(''.join(j))