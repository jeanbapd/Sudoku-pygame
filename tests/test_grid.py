from src.grid import Grid

print("Test 1: Creating new grid")
grid = Grid()
print("Grid created")

print("Test 2: Create new game with different difficulty ")
grid.generate_new_game("easy")
print("Grid created")

grid.generate_new_game("medium")
print("Grid created")

grid.generate_new_game("hard")
print("Grid created")

print("Test 3: Select cells")
grid.select_cell(0,0)
assert grid.selected == (0,0),"Selected cell should be (0,0)"
print("The selection works")
