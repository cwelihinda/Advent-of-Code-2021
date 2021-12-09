lines = open("day9_in.txt", "r").read().split("\n")
def init_grid(lines):
    grid = []
    for line in lines:
        grid.append(list(line))
    return grid

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

def check_point(grid):
    low_points = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(check_surroundings(grid, i, j)):
                low_points.append(int(grid[i][j]))
    return low_points            

def get_risk_level(low_points):
    risk_level = 0
    for i in low_points:
        risk_level += (i + 1)
    return risk_level

low_points = check_point(init_grid(lines))

print(get_risk_level(low_points))