from collections import deque

grid = []
with open("input.txt", 'r') as file:    # open the file

    for line in file:
        grid.append(list(line.strip()))     # create a 2D matrix

# create a list for moving in all eight adjacent directions
direction = [
    (-1,-1), 
    (-1,0), 
    (-1,1), 
    (0,-1), 
    (0,1), 
    (1,-1), 
    (1,0), 
    (1,1)]

def checkNeighbors(grid, direction, r,c):

    row = len(grid)
    col = len(grid[0])

    rollCount = 0

    for dr, dc in direction:
        new_r , new_c = r+dr, c+dc

        if 0 <= new_r < row and 0 <= new_c < col and grid[new_r][new_c] == '@':
            rollCount += 1
    return rollCount


def findRolls(grid, direction):

    row = len(grid)
    col = len(grid[0])

    queue  = deque()

    for r in range(row):
        for c in range(col):
            # rollCount = 0
            
            if grid[r][c] != '@':
                continue

            if checkNeighbors(grid, direction, r, c) < 4:
                queue.append((r,c))

            
    removed = 0

    while queue:
        r,c = queue.popleft()

        # check if also removed
        if grid[r][c] != '@':
            continue

        # Remove this roll
        grid[r][c] = '.'
        removed += 1

        for dr, dc in direction:
            new_r, new_c = r+dr, c+dc 

            if 0 <= new_r < row and 0 <= new_c < col and grid[new_r][new_c] == '@':

                # check if neighbor became accessible
                if checkNeighbors(grid, direction, new_r, new_c) < 4:
                    queue.append((new_r, new_c))
    return removed 

       
print(findRolls(grid, direction))


