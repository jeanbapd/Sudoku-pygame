"""
This file contain all constant the Sudoku need.
"""

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

#Colors for the User Interface
BG_COLOR = 0xFFFFFF#White
GRID_COLOR = 0x000000#Black
CASE_COLOR = 0xD3D3D3#Lightgrey
FIXED_NUMBERS_COLOR = 0x000000
UER_NUMBERS_COLOR = 0xADD8E6#Lightblue
ERROR_COLOR = 0xFF0000#Red
BUTTON_COLOR = 0x90EE90#Lightgreen
SELECTED_CASE_COLOR = 0xADD8E6
FONT_COLOR = 0xFFFFFF

#Font
FONT_SIZE = 10
