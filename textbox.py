import pygame

class Text:

    def __init__(self, text, textRect : pygame.Rect, screen : pygame.Surface):
        self.text  = text
        self.textRect = textRect
        self.screen = screen
    
    def show(self):
        self.screen.blit(self.text, self.textRect)


