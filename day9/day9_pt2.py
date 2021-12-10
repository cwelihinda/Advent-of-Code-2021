lines = open("day9_in.txt", "r").read().split("\n")
def init_grid(lines):
    visited = []
    grid = []
    for line in lines:
        visited.append([False] * len(list(line)))
        grid.append(list(line))
    return grid, visited

def check_left(grid, row, col):
    if ((col - 1) < 0):
        return True
    left = int(grid[row][col - 1])
    if(left > int(grid[row][col])):
        return True
    return False

def check_right(grid, row, col):
    if ((col + 1) >= len(grid[row])):
        return True
    right = int(grid[row][col + 1])
    if(right > int(grid[row][col])):
        return True
    return False

def check_up(grid, row, col):
    if ((row - 1) < 0):
        return True
    up = int(grid[row - 1][col])
    if(up > int(grid[row][col])):
        return True
    return False

def check_down(grid, row, col):
    if ((row + 1) >= len(grid)):
        return True
    down = int(grid[row + 1][col])
    if(down > int(grid[row][col])):
        return True
    return False

def check_surroundings(grid, row, col):
    return check_left(grid, row, col) and check_right(grid, row, col) and check_up(grid, row, col) and check_down(grid, row, col)

def can_go_left(grid, row, col, visited):
     if((col - 1) < 0 or grid[row][col - 1] == '9' or visited[row][col - 1]):
         return False
     return True
 
def can_go_right(grid, row, col, visited):
    if((col + 1) >= len(grid[row]) or grid[row][col + 1] == '9' or visited[row][col + 1]):
         return False
    return True 

def can_go_up(grid, row, col, visited):
    if((row - 1) < 0 or grid[row - 1][col] == '9' or visited[row - 1][col]):
         return False
    return True 

def can_go_down(grid, row, col, visited):
    if((row + 1) >= len(grid) or grid[row + 1][col] == '9' or visited[row + 1][col]):
         return False
    return True 

def go_left(grid, row, col, stack, visited):
    stack.append(grid[row][col - 1])
    visited[row][col - 1] = True
    return traverse_basin(grid, row, col - 1, stack, "left", visited)
    
def go_right(grid, row, col, stack, visited):
    stack.append(grid[row][col + 1])
    visited[row][col + 1] = True
    return traverse_basin(grid, row, col + 1, stack, "right", visited)
    
def go_up(grid, row, col, stack, visited):
    stack.append(grid[row - 1][col])
    visited[row - 1][col] = True
    return traverse_basin(grid, row - 1, col, stack, "up", visited)
    
def go_down(grid, row, col, stack, visited):
    stack.append(grid[row + 1][col])
    visited[row + 1][col] = True
    return traverse_basin(grid, row + 1, col, stack, "down", visited)

def get_basin(grid, row, col,visited):
    stack = []
    stack.append(grid[row][col])
    visited[row][col] = True
    if(can_go_right(grid, row, col, visited)):
        stack = go_right(grid, row, col, stack, visited)
    if(can_go_left(grid, row, col, visited)):
        stack = go_left(grid, row, col, stack, visited)
    if(can_go_up(grid, row, col, visited)):
        stack = go_up(grid, row, col, stack, visited)
    if(can_go_down(grid, row, col, visited)):
        stack = go_down(grid, row, col, stack, visited)
    return stack

def traverse_basin(grid, row, col, stack, direction, visited):
    if(direction == "right"):
        if(can_go_right(grid, row, col, visited)):
            stack = go_right(grid, row, col, stack, visited)
        if(can_go_up(grid, row , col, visited)):
            stack = go_up(grid, row, col, stack, visited)
        if(can_go_down(grid, row, col, visited)):
            stack = go_down(grid, row, col, stack, visited)
        return stack
    if(direction == "left"):
        if(can_go_left(grid, row, col, visited)):
            stack = go_left(grid, row, col, stack, visited)
        if(can_go_up(grid, row , col, visited)):
            stack = go_up(grid, row, col, stack, visited)
        if(can_go_down(grid, row, col, visited)):
            stack = go_down(grid, row, col, stack, visited)
        return stack
    if(direction == "up"):
        if(can_go_up(grid, row, col, visited)):
            stack = go_up(grid, row, col, stack, visited)
        if(can_go_right(grid, row , col, visited)):
            stack = go_right(grid, row, col, stack, visited)
        if(can_go_left(grid, row, col, visited)):
            stack = go_left(grid, row, col, stack, visited)
        return stack
    if(direction == "down"):
        if(can_go_down(grid, row, col, visited)):
            stack = go_down(grid, row, col, stack, visited)
        if(can_go_right(grid, row , col, visited)):
            stack = go_right(grid, row, col, stack, visited)
        if(can_go_left(grid, row, col, visited)):
            stack = go_left(grid, row, col, stack, visited)
        return stack
    
def check_point(grid, visited):
    basins = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(check_surroundings(grid, i, j)):
                basin = get_basin(grid, i, j, visited)
                basins.append(len(basin))
    return sorted(basins)            

grid, visited = init_grid(lines)
basins = check_point(grid, visited)
print(basins[-1] * basins[-2] * basins[-3])
