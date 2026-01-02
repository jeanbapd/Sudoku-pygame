"""
Menu system for Sudoku
"""


import pygame
from src.button import Button
from src.constant import *

class Menu:
    """
    Menu system for Sudoku
    """

    def __init__(self,screen):
        """
        Initialize the menu system
        :param screen: Pygame screen surface
        """
        self.screen = screen
        self.select_difficulty = None

        offset_x = (WINDOW_WIDTH - GRID_PX) // 2

        self.title_font = pygame.font.SysFont("Arial", 60,bold=True,italic=True)
        self.sub_title_font = pygame.font.SysFont("Arial", 30)

        button_width = 200
        button_height = 50
        button_spacing = 20

        top_left_x = (WINDOW_WIDTH - button_width) // 2
        top_left_y = WINDOW_HEIGHT // 2 - 100

        self.easy_button = Button(top_left_x,top_left_y,button_width,button_height,"Easy",(0,255,0),(0,100,0),30)

        self.medium_button = Button(top_left_x,top_left_y + button_height + button_spacing,button_width,button_height,"Medium",(0,0,255),(0,0,100),30)

        self.hard_button = Button(top_left_x,top_left_y + 2 * (button_height + button_spacing),button_width,button_height,"Hard",(255,0,0),(100,0,0),30)

    def handle_event(self,event):
        """
        Handle event for menu system
        :param event: Pygame event
        :return: Selected difficulty or None
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if self.easy_button.is_clicked(pos):
                return "easy"
            elif self.medium_button.is_clicked(pos):
                return "medium"
            elif self.hard_button.is_clicked(pos):
                return "hard"
        return None

    def update(self):
        """
        Update menu system
        :return:
        """
        mouse_pos = pygame.mouse.get_pos()
        self.easy_button.check_hover(mouse_pos)
        self.medium_button.check_hover(mouse_pos)
        self.hard_button.check_hover(mouse_pos)

    def draw(self):
        """
        Draw menu system
        :return: None
        """
        self.screen.fill((255,255,224))

        #Draw title
        title = self.title_font.render("Sudoku",True,(0,0,0))
        title_rect = title.get_rect(center=(WINDOW_WIDTH//2,150))
        self.screen.blit(title,title_rect)

        #Draw subtitle
        sub_title = self.sub_title_font.render("Choose your difficulty",True,(100,100,100))
        sub_title_rect = sub_title.get_rect(center=(WINDOW_WIDTH//2,220))
        self.screen.blit(sub_title,sub_title_rect)

        self.easy_button.draw(self.screen)
        self.medium_button.draw(self.screen)
        self.hard_button.draw(self.screen)