def tok_to_coord(tok):
    coord1 = tok[0].strip().split(",")
    coord2 = tok[1].strip().split(",")
    return [int(coord1[0]), int(coord1[1])], [int(coord2[0]), int(coord2[1])]

def coords_is_valid(coord1, coord2):
    if (coord1[0] == coord2[0]):
        return True, "V"
    elif(coord1[1] == coord2[1]):
        return True, "H"
    return True, "D"

def get_valid_coords(lines):
    valid_coords = []
    for line in lines:
        tok = line.split("->")
        coord1, coord2 = tok_to_coord(tok)
        valid, direction = coords_is_valid(coord1, coord2)
        if(valid):
            valid_coords.append([coord1, coord2, direction])
    return valid_coords

def init_board():
    SIZE = 1000
    return [[0 for j in range(SIZE)] for i in range(SIZE)]

def plot_lines(board, coords):
    for coord in coords:
        if(coord[2] == "V"):
            board = plot_vertical_line(board, coord)
        elif(coord[2] == "H"):
            board = plot_horizontal_line(board, coord)
        elif(coord[2] == "D"):
            board = plot_diagonal_line(board, coord)
    return board
            
def plot_diagonal_line(board, coords):
    coord1 = coords[0]
    coord2 = coords[1]
    dir1 = 1
    dir2 = 1
    if(coord1[0] > coord2[0]):
        dir1 = -1
    if(coord1[1] > coord2[1]):
        dir2 = -1
    j = coord1[1]
    for i in range(coord1[0], coord2[0] + dir1, dir1):
        board[j][i] += 1
        j += dir2
    return board

def plot_vertical_line(board, coords):
    coord1 = coords[0]
    coord2 = coords[1]
    dir1 = 1
    if(coord1[1] > coord2[1]):
        dir1 = -1
    for i in range(coord1[1], coord2[1] + dir1, dir1):
        board[i][coord1[0]] += 1      
    return board
            
def plot_horizontal_line(board, coords):
    coord1 = coords[0]
    coord2 = coords[1]
    dir1 = 1
    if(coord1[0] > coord2[0]):
        dir1 = -1
    for i in range(coord1[0], coord2[0] + dir1, dir1):
        board[coord1[1]][i] += 1
    return board
    
def count_intersections(board):
    count = 0
    for row in board:
        for col in row:
            if (col > 1):
                count += 1
    return count

lines = open("day5_in.txt", "r").read().split("\n")
valid_coords = get_valid_coords(lines)
final_board = plot_lines(init_board(), valid_coords)

print(count_intersections(final_board))

        