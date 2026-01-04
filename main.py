"""
Main file of the game.
"""
import sys
import pygame

from src.button import Button
from src.grid import Grid

from src.constant import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    GRID_PX,
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    BUTTON_SPACING,
    BUTTON_Y,
    BUTTON_COLOR,
    BUTTON_HOVER_COLOR,
    MESSAGE_DURATION
)
from src.menu import Menu


def main():
    """
    Main function of the game.
    :return:
    """

    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))#Create window

    pygame.display.set_caption("Sudoku Game")#Set window caption

    clock = pygame.time.Clock()#Create clock for FPS

    #Game state
    state_menu = "menu"
    state_game = "game"
    current_state = state_menu

    menu = Menu(screen)

    game = None

    grid_px = GRID_PX
    offset_x = (WINDOW_WIDTH - grid_px) // 2 - 1

    buttons_configs = ["New Game","Check","Solve","Restart"]

    buttons = []

    for i,button in enumerate(buttons_configs):
        btn = Button(
            offset_x+ i * (BUTTON_WIDTH + BUTTON_SPACING),
            BUTTON_Y,
            BUTTON_WIDTH,
            BUTTON_HEIGHT,
            button,
            BUTTON_COLOR,
            BUTTON_HOVER_COLOR
        )
        buttons.append(btn)

    new_button,check_button,solve_button,restart_button = buttons

    message = ""
    message_timer = 0

    running = True
    while running:
        #Handle pygame.QUIT event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif current_state == state_menu:
                difficulty = menu.handle_event(event)
                if difficulty:
                    game = Grid()
                    game.generate_new_game(difficulty)
                    current_state = state_game
            elif current_state == state_game:
                match event.type:
                    case pygame.MOUSEBUTTONDOWN:
                        #Get mouse position
                        pos = pygame.mouse.get_pos()

                        if new_button.is_clicked(pos):
                            current_state = state_menu
                            message_timer = 0
                            message = ""
                        elif check_button.is_clicked(pos):
                            if game.is_completed():
                                message = "Congratulations! You have completed the SUDOKU!"
                                message_timer += MESSAGE_DURATION
                            else:
                                message = "Not yet completed or errors present"
                                message_timer += MESSAGE_DURATION
                        elif solve_button.is_clicked(pos):
                            game.solve_grid()
                            message = "Sudoku has been solved and it is the solution!"
                            message_timer += MESSAGE_DURATION
                        elif restart_button.is_clicked(pos):
                            game.reset()
                            message = "Restarting Sudoku"
                            message_timer += MESSAGE_DURATION
                        else:
                            cell = game.get_cell_from_pos(pos)

                            if cell:#Select cell if valid
                                row, col = cell
                                game.select_cell(row,col)
                    case pygame.KEYDOWN:
                        #Number keys 1-9
                        match event.key:
                            case pygame.K_1 | pygame.K_KP1:
                                game.place_number(1)
                            case pygame.K_2 | pygame.K_KP2:
                                game.place_number(2)
                            case pygame.K_3 | pygame.K_KP3:
                                game.place_number(3)
                            case pygame.K_4 | pygame.K_KP4:
                                game.place_number(4)
                            case pygame.K_5 | pygame.K_KP5:
                                game.place_number(5)
                            case pygame.K_6 | pygame.K_KP6:
                                game.place_number(6)
                            case pygame.K_7 | pygame.K_KP7:
                                game.place_number(7)
                            case pygame.K_8 | pygame.K_KP8:
                                game.place_number(8)
                            case pygame.K_9 | pygame.K_KP9:
                                game.place_number(9)
                            #Clear keys
                            case pygame.K_BACKSPACE | pygame.K_DELETE | pygame.K_0 | pygame.K_KP0:
                                game.clear_cells()
                            #Arrow key
                            case pygame.K_UP if game.selected:
                                row, col = game.selected
                                game.select_cell(max(0,row-1),col)
                            case pygame.K_DOWN if game.selected:
                                row, col = game.selected
                                game.select_cell(min(8,row + 1),col)
                            case pygame.K_LEFT if game.selected:
                                row, col = game.selected
                                game.select_cell(row,max(0,col - 1))
                            case pygame.K_RIGHT if game.selected:
                                row, col = game.selected
                                game.select_cell(row,min(8,col + 1))

        if current_state == state_menu:
            menu.update()
            menu.draw()
        elif current_state == state_game:
            if message_timer > 0:
                message_timer -=1
                if message_timer == 0:
                    message = ""
            pos = pygame.mouse.get_pos()
            for btn in buttons:
                btn.check_hover(pos)
            game.draw(screen)#Call game.draw to render

            for button in buttons:
                button.draw(screen)

            if message:
                text =  pygame.font.SysFont("Arial",35)
                text_surface = text.render(message,True,(255,0,0))
                text_rect = text_surface.get_rect(center=( offset_x + GRID_PX/2,GRID_PX/2))
                screen.blit(text_surface,text_rect)
        pygame.display.flip()#Update display

        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
