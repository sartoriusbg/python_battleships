import pygame

pygame.init()
pygame.display.set_caption('Battleships')

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800
main_font = pygame.font.SysFont("cambria", 35)


class Button():
	def __init__(self, image, x_pos, y_pos, text_input):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = main_font.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self):
		screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		return position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom)
			

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = main_font.render(self.text_input, True, "green")
		else:
			self.text = main_font.render(self.text_input, True, "white")

button_surface = pygame.image.load("button.webp")
button_surface = pygame.transform.scale(button_surface, (200, 50))
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
button_solo = Button(button_surface, 400, 250, "Solo")
button_multy = Button(button_surface, 400, 350, "Multy")
button_quit = Button(button_surface, 400, 450, "Quit")

def debug_print(text):
	print(text)

background = pygame.image.load('battleships.jpg')
background = pygame.transform.scale(background, (800, 500))
font = pygame.font.Font('freesansbold.ttf', 70)
text = font.render('Battleships', True, "black")
textRect = text.get_rect()
textRect.center = (400, 100)
running = True
while running:
	
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_solo.checkForInput(pygame.mouse.get_pos()):
                debug_print("solo")
            if button_multy.checkForInput(pygame.mouse.get_pos()):
                debug_print("multy")
            if button_quit.checkForInput(pygame.mouse.get_pos()):
                 running = False
	
    screen.blit(background, (0,0))
    screen.blit(text, textRect)
    button_solo.update()
    button_solo.changeColor(pygame.mouse.get_pos())
    button_multy.update()
    button_multy.changeColor(pygame.mouse.get_pos())
    button_quit.update()
    button_quit.changeColor(pygame.mouse.get_pos())
    
    pygame.display.update()
pygame.quit()