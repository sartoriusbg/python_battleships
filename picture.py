import pygame


#background = pygame.image.load('battleships.jpg')
#background = pygame.transform.scale(background, (800, 500))



class Picture:

    def a__init__(self, *args, **kwargs):
        print(args)
        print(kwargs)

    def __init__(self, image, transformation, position, screen : pygame.Surface):
        self.screen = screen
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, transformation)
        self.position = position

    def show(self):
        self.screen.blit(self.image, self.position)