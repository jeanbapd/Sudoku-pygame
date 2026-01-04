"""
File who represent the grid logic
"""
import pygame

from src.generator import copy_grid,generate_sudoku
from src.solver import find_empty,is_valid,solve
from src.constant import (
WINDOW_WIDTH,
WINDOW_HEIGHT,
CELL_SIZE,
FONT_SIZE,
GRID_PX,
BG_COLOR,
GRID_COLOR,
CASE_COLOR,
FIXED_NUMBERS_COLOR,
USER_NUMBERS_COLOR,
ERROR_COLOR,
SELECTED_CASE_COLOR,
ERROR_BG_COLOR
)

class Grid:
    """
    Class to represent a grid
    """

    def __init__(self):
        """Initialize the grid """

        self.grid = [[0 for _ in range(9)] for _ in range(9)]

        self.original = copy_grid(self.grid)

        self.selected = None

        self.errors = []

    def generate_new_game(self,difficulty="medium"):
        """
        Function to generate a new game
        :param difficulty: The difficulty of the game
        :return: None
        """
        self.grid = generate_sudoku(difficulty)

        self.original = copy_grid(self.grid)

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
        self.grid = copy_grid(self.original)

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
        #Erase cells with errors
        for row,col in self.errors:
            if not self.is_original(row,col):
                self.grid[row][col] = 0

        self.errors = []

        grid_copy = copy_grid(self.grid)

        if solve(grid_copy):

            self.grid = copy_grid(grid_copy)

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
        if not is_valid(self.grid,num,row,col):
            #Add to the errors list if invalid
            if (row,col) not in self.errors:
                self.errors.append((row,col))

            return False

        #Remove from the errors list if now valid
        if (row,col) in self.errors:

            self.errors.remove((row,col))
        return True

    def is_completed(self):
        """
        Check if the grid is completed and valid
        :return: True if the grid is resolved correctly, False otherwise
        """
        if find_empty(self.grid) is not None:#Check if an empty cell exists
            return False

        if len(self.errors)>0:
            return False

        solution = copy_grid(self.original)
        if not solve(solution):
            return False
        return self.grid == solution

    def get_cell_from_pos(self, pos):
        """
        Convert a mouse position to a coordinate cell
        :param pos: Tuple (x,y) of the mouse position
        :return: (row, col) or None if no cell found
        """
        x, y = pos

        if 0 <= x < WINDOW_WIDTH and 0 <= y < WINDOW_HEIGHT:
            col = x // CELL_SIZE
            row = y // CELL_SIZE
            return (row, col)
        return None

    def draw(self, screen):
        """
        Draw the SUDOKU grid on screen
        :param screen: Pygame screen surface
        :return: None
        """
        screen.fill(BG_COLOR)

        # Number rendering
        font = pygame.font.Font(None, FONT_SIZE)

        grid_px = GRID_PX
        offset_x = (WINDOW_WIDTH - grid_px) // 2 - 1
        offset_y = offset_x
        for row in range(9):
            for col in range(9):

                x = offset_x + col * CELL_SIZE
                y = offset_y + row * CELL_SIZE

                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

                pygame.draw.rect(screen, CASE_COLOR, rect)

                if (row,col) in self.errors:#Highlight error cells with light red background
                    pygame.draw.rect(screen, ERROR_BG_COLOR, rect)
                elif self.selected and self.selected == (row, col):#Highlight selected cell with SELECTED_CASE_COLOR
                    pygame.draw.rect(screen, SELECTED_CASE_COLOR, rect)


        for i in range(10):
            thickness = 4 if i%3 == 0 else 1

            #Horizontal lines
            pygame.draw.line(
                screen,
                GRID_COLOR,
                (offset_x,offset_y + i*CELL_SIZE),
                (offset_x + grid_px,offset_y + i*CELL_SIZE),
                thickness
            )

            #Vertical lines
            pygame.draw.line(
                screen,
                GRID_COLOR,
                (offset_x + i * CELL_SIZE,offset_y),
                (offset_x + i * CELL_SIZE,offset_y + grid_px),
                thickness
            )

        pygame.draw.rect(
            screen,
            GRID_COLOR,
            (offset_x,offset_y,grid_px,grid_px),
            4
        )


        for row in range(9):
            for col in range(9):
                num = self.grid[row][col]

                if num != 0:
                    x = offset_x + col * CELL_SIZE + CELL_SIZE//2
                    y = offset_y + row * CELL_SIZE + CELL_SIZE//2

                    if (row,col) in self.errors:
                        color = ERROR_COLOR
                    elif self.is_original(row,col):
                        color = FIXED_NUMBERS_COLOR
                    else:
                        color = USER_NUMBERS_COLOR

                    text = font.render(str(num), True, color)
                    text_rect = text.get_rect(center=(x,y))
                    screen.blit(text, text_rect)
