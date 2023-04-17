# Get the first empty spot (= 0) and return it's position/index
def get_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j   # raw, col
    # if there is no more empty spots
    return None, None


# Check if the number is valid =>  
# each column, each row, and each of the nine 3 × 3 subgrids that compose the grid contain all of the digits from 1 to 9 (no duplicates)
def is_valid(grid, num, row, col):
    # Check rows
    for y in range(9):
        if grid[row][y] == num:
            return False
    
    # Check columns
    for x in range(9):
        if grid[x][col] == num:
            return False

    # Check 3*3 Box
    # Divide the 9*9 grid in 3*3 subgrids, so we could iterate over them
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if grid[i][j] == num:
                return False

    # if we pass all conditions => the number is valid
    return True


# Solve a sudoku-grid using backtracking
def solve(grid):
    # start from the first empty spot
    row, col = get_empty(grid)

    # if no more empty spot => done
    if row is None:
        return True

    # if there is empty spots => choose a number from 1 to 9 (start with 1)    
    for num in range(1, 10):
        # check if the number is valid
        if is_valid(grid, num, row, col):
            # if number is valid => put it on the grid
            grid[row][col] = num
            # recursively call the function and return true if solvable
            if solve(grid):
                return True
        # if the number doesn't solve the sudoku then reset it's value to 0 (empty spot) 
        # plus backtrack to the last spot and try a new number
        grid[row][col] = 0
    
    # if the sudoku is unsolvable
    return False


# function to print the sudoku            
def print_grid(grid):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("------------------------")
        
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")



# sudoku puzzle example
# 0 = empty spot
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
        

print_grid(sudoku_grid)
print("\nSolution :\n")
solve(sudoku_grid)
print_grid(sudoku_grid)
