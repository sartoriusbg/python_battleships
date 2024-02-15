import pygame
import sys

class Text_input:

    def __init__(self, text, font, size, position, screen: pygame.Surface):
        self.screen = screen
        self.constr_text = text
        self.constr_font = font
        self.constr_size = size
        self.constr_position = position
        title_font = pygame.font.Font(font, size)
        self.text = title_font.render(text, True, "red")
        self.textRect = self.text.get_rect()
        self.textRect.center = position
    
    def show(self):
        self.screen.blit(self.text, self.textRect)
