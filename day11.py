import copy

def adjacentOccupied(row, col, grid):
    occupied = 0
    for x in range(row - 1, row + 2):
        for y in range(col - 1, col + 2):
            if (
                x in range(len(grid))
                and y in range(len(grid[0]))
                and not (x == row and y == col)
                and grid[x][y] == '#'
            ):
                occupied += 1
    return occupied

def visibleOccupied(row, col, grid):
    occupied = 0
    x = row
    for y in range(col + 1, len(grid[0])):
        if grid[x][y] in 'L#':
            if grid[x][y] == '#':
                occupied += 1
            break
    for y in range(col - 1, -1, -1):
        if grid[x][y] in 'L#':
            if grid[x][y] == '#':
                occupied += 1
            break
    y = col
    for x in range(row + 1, len(grid)):
        if grid[x][y] in 'L#':
            if grid[x][y] == '#':
                occupied += 1
            break
    for x in range(row - 1, -1, -1):
        if grid[x][y] in 'L#':
            if grid[x][y] == '#':
                occupied += 1
            break
    for x in range(row + 1, len(grid)):
        y = x + col - row
        if y in range(len(grid[0])) and grid[x][y] in 'L#':
            if grid[x][y] == '#':
                occupied += 1
            break
    for x in range(row + 1, len(grid)):
        y = row + col - x
        if y in range(len(grid[0])) and grid[x][y] in 'L#':
            if grid[x][y] == '#':
                occupied += 1
            break
    for x in range(row - 1, -1, -1):
        y = x + col - row
        if y in range(len(grid[0])) and grid[x][y] in 'L#':
            if grid[x][y] == '#':
                occupied += 1
            break
    for x in range(row - 1, -1, -1):
        y = row + col - x
        if y in range(len(grid[0])) and grid[x][y] in 'L#':
            if grid[x][y] == '#':
                occupied += 1
            break
    return occupied

def change(tolerance, grid, part):
    if part == 1:
        checkOccupied = adjacentOccupied
    elif part == 2:
        checkOccupied = visibleOccupied
    changed = 0
    newGrid = copy.deepcopy(grid)
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (grid[x][y] == 'L'
            and checkOccupied(x, y, grid) == 0):
                newGrid[x][y] = '#'
                changed += 1
            if (grid[x][y] == '#'
            and checkOccupied(x, y, grid) > tolerance):
                newGrid[x][y] = 'L'
                changed += 1    
    return [newGrid, changed]

def occupied(grid):
    occupied = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == '#':
                occupied += 1
    return occupied

oriGrid = []
with open('input/day11.txt') as f:
    for line in f:
        row = list(line.rstrip('\n'))
        oriGrid.append(row)

# Part One
grid = copy.deepcopy(oriGrid)
changed = 1
while changed != 0:
    lastchange = change(3, grid, 1)
    grid = lastchange[0]
    changed = lastchange[1]
print(occupied(grid))

# Part Two
grid = copy.deepcopy(oriGrid)
changed = 1
while changed != 0:
    lastchange = change(4, grid, 2)
    grid = lastchange[0]
    changed = lastchange[1]
print(occupied(grid))