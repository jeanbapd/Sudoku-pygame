"""
File who create the SUDOKU grid
"""

import random as rnd
import src.solver
from src.constant import DIFFICULTY

def remove_numbers(grid,difficulty):
    """
    Function to remove numbers to the grid
    :param grid: Grid of cells
    :param difficulty: Numbers of cells to be removed
    :return: None
    """
    removed = 0

    while removed < difficulty:
        row = rnd.randint(0,len(grid)-1)
        col = rnd.randint(0,len(grid[0])-1)

        if grid[row][col] != 0:

            removed += 1
            grid[row][col] = 0


def fill_grid(grid):
    """
    Function to fill the grid with the numbers
    :param grid: Grid of cells initialize to zero
    :return: True if grid is filled
    """
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                num = list(range(1,10))
                rnd.shuffle(num)

                for n in num:
                    if src.solver.is_valid(grid,n,row,col):
                        grid[row][col] = n

                        if fill_grid(grid):
                            return True

                        grid[row][col] = 0
                return False

    return True

def generate_sudoku(difficulty="medium"):
    """
    Generate a sudoku grid
    :param difficulty: "easy", "medium", "hard"
    :return: Grid of sudoku
    """
    grid = [[0 for _ in range(9)] for _ in range(9)]

    fill_grid(grid)

    remove_numbers(grid,DIFFICULTY.get(difficulty))

    return grid


def copy_grid(grid):
    """
    Function to copy grid into a new grid
    :param grid: The grid to be copied
    :return: New grid with copied grid
    """
    return [row[:] for row in grid]