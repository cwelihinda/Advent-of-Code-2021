lines = open("day11_in.txt", "r").read().split("\n")
def get_new_day_flashes(grid):
    flashes = []
    for row in grid:
        flash_row = [False] * len(row)
        flashes.append(flash_row)
    return flashes
 
def init_grid(lines):
    grid = []
    for line in lines:
        grid.append([int(num) for num in list(line)])
    return grid

def increase_power_level(grid):
    new_grid = []
    for row in grid:
        new_row  = []
        for item in row:
            new_row.append(item + 1)
        new_grid.append(new_row)
    return new_grid

def flash_top_right(grid,row, col, flashes):
    if(row - 1 < 0 or col + 1 >= len(grid[row]) or flashes[row - 1][col + 1]):
        return
    else:
        grid[row - 1][col + 1] = grid[row - 1][col + 1] + 1
            
def flash_top_left(grid,row, col, flashes):
    if(row - 1 < 0 or col -1 < 0 or flashes[row - 1][col - 1]):
        return
    else:
        grid[row - 1][col - 1] = grid[row - 1][col -1] + 1
            
def flash_bottom_right(grid,row, col, flashes):
    if(row + 1 >= len(grid) or col + 1 >= len(grid[row])or flashes[row + 1][col + 1]):
        return
    else:
        grid[row + 1][col + 1] = grid[row + 1][col + 1] + 1
            
def flash_bottom_left(grid,row, col, flashes):
    if(row + 1 >= len(grid) or col - 1 < 0 or flashes[row + 1][col - 1]):
        return
    else:
        grid[row + 1][col - 1] = grid[row + 1][col -1] + 1
            
def flash_up(grid, row, col, flashes):
   if(row - 1  < 0 or flashes[row - 1][col]):
        return
   else:
        grid[row - 1][col] = grid[row - 1][col] + 1
            
def flash_down(grid, row, col, flashes):
   if(row + 1  >= len(grid) or flashes[row + 1][col]):
        return
   else:
        grid[row + 1][col] = grid[row + 1][col] + 1
            
def flash_left(grid, row, col, flashes):
    if(col - 1 < 0 or flashes[row ][col - 1]):
        return
    else:
        grid[row][col - 1] = grid[row][col -1] + 1

def flash_right(grid, row, col, flashes):
    if(col + 1 >= len(grid[row]) or flashes[row][col + 1]):
        return
    else:
        grid[row][col + 1] = grid[row][col + 1] + 1
        
def do_flash(grid, row, col, flashes):
    
    flash_top_left(grid, row, col, flashes)
    flash_up(grid, row, col, flashes)
    flash_top_right(grid, row, col, flashes)

    flash_left(grid, row, col, flashes)
    flash_right(grid,row,col, flashes)
    
    flash_bottom_left(grid, row, col, flashes)
    flash_down(grid, row, col, flashes)
    flash_bottom_right(grid, row, col, flashes)
    grid[row][col] = 0
    
def check_power_level(grid, flashes):
    hasNewFlash = False
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j] > 9 and not flashes[i][j]):
                do_flash(grid, i, j, flashes)
                flashes[i][j] = True
                hasNewFlash = True
                count+= 1
    return hasNewFlash, count
        
grid = init_grid(lines)

total = 0
for i in range(100):
    new_grid = increase_power_level(grid)
    flashes = get_new_day_flashes(grid)
    has_new_flash, count = check_power_level(new_grid, flashes)
    total += count
    while(has_new_flash):
        has_new_flash, count = check_power_level(new_grid, flashes)
        total += count
    grid = new_grid

print(total)