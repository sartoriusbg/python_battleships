import pygame
import button
import textbox
import picture
import textinput

# def main_menu():
#     print("in main")
#     title_font = pygame.font.Font('freesansbold.ttf', 70)
#     text = title_font.render('Battleships', True, "black")
#     textRect = text.get_rect()
#     textRect.center = (400, 100)
#     running = True
#     while running:
#         screen.fill("black")
#         screen.blit(background, (0,0))
#         screen.blit(text, textRect)
#         button_solo.update()
#         button_solo.changeColor(pygame.mouse.get_pos())
#         button_multy.update()
#         button_multy.changeColor(pygame.mouse.get_pos())
#         button_quit.update()
#         button_quit.changeColor(pygame.mouse.get_pos())
#         pygame.display.update()
#         for event in pygame.event.get():
#             if not running:
#                 break
#             if event.type == pygame.QUIT:
#                 #pygame.quit()
#                 running = False
#                 break
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if button_solo.checkForInput(pygame.mouse.get_pos()):
#                    place_ships()
#                    running = False
#                    break
#                 if button_multy.checkForInput(pygame.mouse.get_pos()):
#                     debug_print("multy")
#                 if button_quit.checkForInput(pygame.mouse.get_pos()):
#                     #pygame.quit()
#                     running = False
#                     break


class View:

    def __init__(self, screen : pygame.Surface, background : pygame.Surface, buttons: list[button.Button], text_boxes : list[textbox.Text], pictures : list[picture.Picture] = [], text_input : textinput.Text_input = None):
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
                
            