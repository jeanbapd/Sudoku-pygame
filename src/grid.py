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