import pygame

pygame.init()
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800
button_font = pygame.font.SysFont("freesansbold.ttf", 35)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
button_surface = pygame.image.load("button.webp")
button_surface = pygame.transform.scale(button_surface, (200, 50))
button_cell_surface = pygame.image.load("cell.png")
button_cell_surface = pygame.transform.scale(button_cell_surface, (30, 30))
button_selected_cell_surface = pygame.image.load("selected_cell.png")
button_selected_cell_surface = pygame.transform.scale(button_selected_cell_surface, (30, 30))
class Button():
	def __init__(self, image, x_pos, y_pos, text_input = ""):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = button_font.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self):
		screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)
	
	def set_action(self, action, parameters = []):
		self.action = action
		self.parameters = parameters
		return self
	
	def exec_action(self):
		self.action(*self.parameters)
	
	def checkForInput(self, position):
		return position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom)
			

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = button_font.render(self.text_input, True, "green")
		else:
			self.text = button_font.render(self.text_input, True, "white")
	
	def show(self):
		self.update()
		self.changeColor(pygame.mouse.get_pos())

	def __eq__(self, other):
		return self.x_pos == other.x_pos and self.y_pos == other.y_pos