import pygame
import button

#import gamelogic
pygame.init()

button_quit = button.Button(button.button_surface, 400, 450, "Quit")
class Ship_placement:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen

    def run(self):
        background = pygame.image.load('battleships.jpg')
        background = pygame.transform.scale(background, (800, 500))
        running = True
        while running:
	
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_quit.checkForInput(pygame.mouse.get_pos()):
                        running = False
                
            
            self.screen.blit(background, (0,0))
            button_quit.update()
            button_quit.changeColor(pygame.mouse.get_pos())
            pygame.display.update()
            
        #pygame.quit()

    
