# Day 4 Pt. 1

def countRolls(grid):

    row = len(grid)
    col = len(grid[0])
    count = 0

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

    for r in range(row):
        for c in range(col):
            rollCount = 0
            
            if grid[r][c] != '@':
                continue

            for dr, dc in direction:
                
                new_r , new_c = r+dr, c+dc

                if 0 <= new_r < row and 0 <= new_c < col and grid[new_r][new_c] == '@':
                    rollCount += 1

            if rollCount < 4:
                count += 1
    return count
    #print(count)

if __name__ == "__main__":

    grid = []             # create a 2D Matrix
    with open("input-day4.txt", 'r') as file:    # open the file
        
        for line in file:
            grid.append(list(line.strip()))   

    print(countRolls(grid))
    

