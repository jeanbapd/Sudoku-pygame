import pygame

import sys

from src.grid import Grid

from src.constant import WINDOW_HEIGHT,WINDOW_WIDTH

def main():
    """
    Main function of the game.
    :return:
    """

    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))#Create window

    pygame.display.set_caption("Sudoku Game")#Set window caption

    clock = pygame.time.Clock()#Create clock for FPS

    game = Grid()#Create the grid

    game.generate_new_game()#Generate the game
    running = True
    while running:
        #Handle pygame.QUIT event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game.draw(screen)#Call game.draw to render
        pygame.display.flip()#Update display

        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()