"""
This file contain all constant the Sudoku need.
"""

#Windows dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 850

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
BG_COLOR = (255,255,255)#White
GRID_COLOR = (0,0,0)#Black
CASE_COLOR = (211,211,211)#Lightgrey
FIXED_NUMBERS_COLOR = (0,0,0)
USER_NUMBERS_COLOR = (0,0,255)
ERROR_COLOR = (255,0,0)#Red
BUTTON_COLOR = (144,238,144)#Lightgreen
BUTTON_HOVER_COLOR = (39,174,96)#Darkgreen
SELECTED_CASE_COLOR = (173,216,230)#Lightblue
FONT_COLOR = (255,255,255)
ERROR_BG_COLOR = (255,200,200)#Lightred

#Font
FONT_SIZE = 23

#Button dimensions
GRID_PX = CELL_SIZE * 9#Total width of the grid
BUTTON_HEIGHT = 40
BUTTON_SPACING = 10
BUTTON_WIDTH = (GRID_PX - 3 * BUTTON_SPACING) // 4
BUTTON_Y = GRID_PX + 10 #Ten pixels above the grid

MESSAGE_DURATION = 100
