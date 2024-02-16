import pygame
import button
import textbox
import picture
import textinput

class View:

    def __init__(self, screen : pygame.Surface, background : pygame.Surface, buttons: list[button.Button], text_boxes : list[textbox.Text] = [], pictures : list[picture.Picture] = [], text_input : textinput.Text_input = None):
        self.screen = screen
        self.background = background
        self.buttons = buttons
        self.text_boxes = text_boxes
        self.pictures = pictures
        self.text_input = text_input
        self.text_result = ''
    
    def run(self):
        running = True
        while running:
            self.screen.fill("black")
            self.screen.blit(self.background, (0,0))
            for text_box in self.text_boxes:
                text_box.show()
            for button in self.buttons:
                button.show()
            for picture in self.pictures:
                picture.show()
            if self.text_input != None:
                self.text_input.show()
            pygame.display.update()
            for event in pygame.event.get():
                if not running:
                    break
                if event.type == pygame.QUIT:
                    #pygame.quit()
                    running = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        if button.checkForInput(pygame.mouse.get_pos()):
                            button.exec_action()
                            running = False
                            break  
                if self.text_input != None:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            self.text_input = textinput.Text_input(self.text_input.constr_text[:-1], self.text_input.constr_font, self.text_input.constr_size, self.text_input.constr_position, self.text_input.screen)
                            self.text_result = self.text_result[:-1]
                        else:
                            self.text_input = textinput.Text_input(self.text_input.constr_text + event.unicode, self.text_input.constr_font, self.text_input.constr_size, self.text_input.constr_position, self.text_input.screen)
                            self.text_result = self.text_input.constr_text + event.unicode
                
            