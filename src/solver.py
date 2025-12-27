"""
File containing all algorithms to find the solution
"""

def find_empty(grid):
    """
    Function to find an empty cell
    :param grid: The grid of cells
    :return: Returns the empty cell or None if no cell exists
    """
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return (row, col)
    return None

def is_valid(grid,num,row,col):
    """
    Function to check if a cell is valid
    :param grid: List of cells in 2D
    :param num: Number to be checked
    :param row: Position of cell in grid
    :param col: Position of cell in grid
    :return: True if the cell placement is valid, False otherwise
    """
    valid_mv = True

    if grid[row].count(num) > 1 or grid[:][col].count(num) > 1:
        valid_mv = False

    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for r in range(box_row,box_row + 3):#Check if
        for c in range(box_col,box_col + 3):
            if grid[r][c] == num and (r,c) != (row,col):
                valid_mv = False

    return valid_mv

def solve(grid):
    """
    Function to find the solution
    :param grid: List of cells in 2D
    :return: True if solution is found, False otherwise
    """
    empty = find_empty(grid)

    if empty is None:
        return True

    row, col = empty

    for num in range(1,10):
        if is_valid(grid,num,row,col):
            grid[row][col] = num

            if solve(grid):
                return True

            grid[row][col] = 0

    return False
