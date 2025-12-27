"""
File who represent the grid logic
"""
import pygame

import src.generator
import src.solver
import src.constant

class Grid:
    """
    Class to represent a grid
    """

    def __init__(self):
        """Initialize the grid """

        self.grid = [[0 for _ in range(9)] for _ in range(9)]

        self.original = src.generator.copy_grid(self.grid)

        self.selected = None

        self.errors = []

    def generate_new_game(self,difficulty="medium"):
        """
        Function to generate a new game
        :param difficulty: The difficulty of the game
        :return: None
        """
        self.grid = src.generator.generate_sudoku(difficulty)

        self.original = src.generator.copy_grid(self.grid)

        self.selected = None
        self.errors = []

    def select_cell(self,row,col):
        """
        Select a cell
        :param row: The row of the cell
        :param col: The column of the cell
        :return: None
        """
        if 0 <= row < 9 and 0 <= col < 9:
            self.selected = (row,col)

    def is_original(self,row,col):
        """
        Verify if the cell is original
        :param row: The row of the cell
        :param col: The column of the cell
        :return: True if cell is original, False otherwise
        """
        return self.original[row][col] != 0

    def reset(self):
        """
        Reset the grid
        :return: None
        """
        self.selected = None
        self.errors = []
        self.grid = src.generator.copy_grid(self.original)

    def clear_cells(self):
        """
        Clear the cell selected
        :return: None
        """
        if self.selected is None:#Check if cell is selected
            return

        if not self.is_original(*self.selected):
            self.grid[self.selected[0]][self.selected[1]] = 0

            if self.selected in self.errors:#Remove from list of error if exist
                self.errors.remove(self.selected)

    def solve_grid(self):
        """
        Solve the grid
        :return: True if the grid is solved, False otherwise
        """
        grid_copy = src.generator.copy_grid(self.grid)

        if src.solver.solve(grid_copy):

            self.grid = src.generator.copy_grid(grid_copy)

            self.errors = []

            return True
        return False

    def place_number(self,num):
        """
        Place a number in the selected cell
        :param num: The number to be placed
        :return: True if the number is placed, False otherwise
        """
        if self.selected is None:#Check if a cell is selected
            return False

        row, col = self.selected

        if self.is_original(row,col):#Check if the cell is not original
            return False

        self.grid[row][col] = num
        # Validate the movement
        if not src.solver.is_valid(self.grid,num,row,col):
            #Add to the errors list if invalid
            if (row,col) not in self.errors:
                self.errors.append((row,col))

            return False
        else:
            #Remove from the errors list if now valid
            if (row,col) in self.errors:

                self.errors.remove((row,col))
            return True

    def is_completed(self):
        """
        Check if the grid is completed and valid
        :return: True if the grid is resolved correctly, False otherwise
        """
        if src.solver.find_empty(self.grid) is None:#Check if an empty cell exists
            return False

        if len(self.errors)>0:
            return False

        solution = src.solver.solve(self.original)
        #Check if the current grid is the solution
        for row in range(9):
            for col in range(9):
                if solution[row][col] != self.grid[row][col]:
                    return False
        return True

    def get_cell_from_pos(self, pos):
        """
        Convert a mouse position to a coordinate cell
        :param pos: Tuple (x,y) of the mouse position
        :return: (row, col) or None if no cell found
        """
        x, y = pos

        if x < src.constant.WINDOW_WIDTH and y < src.constant.WINDOW_HEIGHT:
            col = x // src.constant.CELL_SIZE
            row = y // src.constant.CELL_SIZE
            return (row, col)
        return None