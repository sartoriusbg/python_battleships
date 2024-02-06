import pygame

class Text:

    def __init__(self, text, font, size, position, screen: pygame.Surface):
        self.screen = screen
        title_font = pygame.font.Font(font, size)
        self.text = title_font.render(text, True, "red")
        self.textRect = self.text.get_rect()
        self.textRect.center = position

    def show(self):
        self.screen.blit(self.text, self.textRect)