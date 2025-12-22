"""
This file contain all constant the Sudoku need.
"""
from pygame.examples.midi import BACKGROUNDCOLOR

#Windows dimensions
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 650

#Grid size
GRID_SIZE = 9 #Number of cell in a  row and a column
CELL_SIZE = WINDOW_WIDTH // GRID_SIZE

#Difficulty is the number of cell which must be removed
DIFFICULTY = {
    "easy": 30,
    "medium": 40,
    "hard": 50,
}

