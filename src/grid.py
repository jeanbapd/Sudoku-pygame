import pygame

import src.generator
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

        if 0 <= row < 9 and 0 <= col < 9:
            self.selected = (row,col)
