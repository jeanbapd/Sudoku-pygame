"""
Button class for Ui button
"""
import pygame

import src.constant


class Button:
    """
    Class to create a button object
    """
    def __init__(self,x,y,width,height,text,color,hover_color,font_size):
        """
        Constructor for button object
        :param x: Position of the top left corner of the button
        :param y: position of the top left corner of the button
        :param width: Width of the button
        :param height: Height of the button
        :param text: Text of the button
        :param color: Color of the button
        :param hover_color: Color of the hover button
        :param font_size: Font size of the button
        """
        self.rect = pygame.Rect(x,y,width,height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.SysFont("Arial",font_size)
        self.is_hovered = False

    def draw(self,screen):
        """
        Draw the button on the screen
        :param screen:
        :return: None
        """
        color = self.hover_color if self.is_hovered else self.color #Choose the color

        pygame.draw.rect(screen,color,self.rect)

        pygame.draw.rect(screen,self.hover_color,self.rect,2)#Draw border

        #Draw text
        text_surface = self.font.render(self.text,True,src.constant.FONT_COLOR)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface,text_rect)

    def check_hover(self,pos):
        """
        Function to check if the button has been hovered
        :param pos:  Position of the mouse
        :return: None
        """
        self.is_hovered = self.rect.collidepoint(pos)

    def is_clicked(self,pos):
        """
        Function to check if the button has been clicked
        :param pos: Position of the mouse
        :return: None
        """
        return self.rect.collidepoint(pos)

