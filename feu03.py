import sys

#Sudoku
def to_solve(unsolved_txt):
    board = []
    with open(unsolved_txt, "r") as uncomplet:
        for rows in uncomplet:
            cleaned_row = [int(num) if num.isdigit() else 0 for num in rows]
            print(cleaned_row[:9])
            board.append(list(cleaned_row[:9]))
    return board

def check_number(board, num, pos):
    for colums in range(len(board[0])):
        if board[pos[0]][colums] == num and pos[1] != colums:
            return False
    for rows in range(len(board)):
        if board[rows][pos[1]] == num and pos[0] != rows:
            return False
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for rows in range(box_y*3, box_y*3 + 3):
        for colums in range(box_x*3, box_x*3 + 3):
            if board[rows][colums] == num and (rows, colums) != pos:
                return False
    return True

def is_empty(board):
    for rows in range(len(board)):
        for cols in range(len(board[0])):
            if board[rows][cols] == 0:
                return (rows, cols)
    return None

def solving(board):
    to_fill = is_empty(board)
    if not to_fill:
        return True
    row, col = to_fill
    for num in range(1, 10):
        if check_number(board, num, (row, col)):
            board[row][col] = num
            if solving(board):
                return True
            board[row][col] = 0
    return False

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- " * 11)
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

if len(sys.argv) != 2:
    sys.exit("You can only put one file")
if sys.argv[1][-4:] != ".txt":
    sys.exit("You have to put one .txt file")
if len(to_solve(sys.argv[1])) != 9:
    sys.exit("You have to put a 9x9 format")

board = to_solve(sys.argv[1])

print("Sudoku Board Before Solving:")
print_board(board)
solving(board)
print("\nSudoku Board After Solving:")
print_board(board)