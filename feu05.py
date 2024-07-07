import sys
from collections import defaultdict, deque
import math
import heapq

def get_maze(file):
    maze_board = []

    with open(f'{file}', 'r') as maze_file:
        for rows in maze_file:
            maze_board.append(list(rows[:-1]))
        maze_board.pop(0)
    return maze_board

def find_starting_point(maze_board):
    for id_row, row in enumerate(maze_board):
        for id_col, elmt in enumerate(row):
            if elmt == '1':
                entry = (id_row, id_col)
            if elmt == '2':
                way_out = (id_row, id_col)
    return entry, way_out


def manhattan_distance(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

def a_star(maze, start, goal):
    rows = len(maze)
    cols = len(maze[0])
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    came_from = {}
    
    g_score = defaultdict(lambda: math.inf)
    g_score[start] = 0
    
    f_score = defaultdict(lambda: math.inf)
    f_score[start] = manhattan_distance(start, goal)
    
    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        for moving in movement(current, rows, cols):
            if maze[moving[0]][moving[1]] == '*':
                continue
            
            tentative_gscore = g_score[current] + 1

            if tentative_gscore < g_score[moving]:
                came_from[moving] = current
                g_score[moving] = tentative_gscore
                f_score[moving] = tentative_gscore + manhattan_distance(moving, goal)
                if moving not in [i[1] for i in open_set]:
                    heapq.heappush(open_set, (f_score[moving], moving))
    if not open_set:
        return sys.exit('There is no path')
    
def movement(pos, rows, cols):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    empty_space = []
    for next_row, next_col in direction:
        new_row, new_col = pos[0] + next_row, pos[1] + next_col
        if 0 <= new_row < rows and 0 <= new_col < cols:
            empty_space.append((new_row, new_col))
    return empty_space

def reconstruct_path(came_from, current):
    path = deque([current])
    while current in came_from:
        current = came_from[current]
        path.appendleft(current)
    return list(path)

def display_result(maze, path_len):
    for row in maze:
        print(''.join(row))
    print(f'Sortie atteinte en {path_len} coups !!!!')

def set_final_board(path, maze):
    o_count = 0
    with_path = []
    for id_row, row in enumerate(maze):
        row = list(row)
        for id_col, elmt in enumerate(row):
            if (id_row, id_col) in path and elmt not in ('1', '2'):
                row[id_col] ='o'
                o_count += 1
        with_path.append(list(row))
    return with_path, o_count

def check_rows_size(board):
    row_len = len(board[1])
    for row in board[2:]:
        if len(row) != row_len:
            return False
    return True

if len(sys.argv) != 2:
    sys.exit('You can only put one .txt file')
if sys.argv[1][-4:] != '.txt':
    sys.exit('Put labyrinthe.txt')
if not check_rows_size(get_maze(sys.argv[1])):
    sys.exit('Your board is not valid')

maze = get_maze(sys.argv[1])
start, goal = find_starting_point(maze)
path = a_star(maze, start, goal)
maze_with_path, path_len = set_final_board(path, maze)

display_result(maze_with_path, path_len)