import pygame
import button
import tkinter
import tkinter.filedialog
import screenviews
import textbox

pygame.init()
pygame.display.set_caption('Battleships')
def dummy():
    print("dummy")
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800
button_font = pygame.font.SysFont("freesansbold.ttf", 35)
background = pygame.image.load('battleships.jpg')
background = pygame.transform.scale(background, (800, 500))
#button_surface = pygame.image.load("button.webp")
#button_surface = pygame.transform.scale(button_surface, (200, 50))
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
def place_ships_manually():
    print("in place ships m")
button_solo = button.Button(button.button_surface, 400, 250, "Solo")
button_multy = button.Button(button.button_surface, 400, 350, "Multy")
button_quit = button.Button(button.button_surface, 400, 450, "Quit")
button_back = button.Button(button.button_surface, 400, 450, "Back")
button_place_from_file = button.Button(button.button_surface, 400, 350, "From file")
button_place_manually = button.Button(button.button_surface, 400, 250, "Manually")

def prompt_file():
    """Create a Tk file dialog and cleanup when finished"""
    top = tkinter.Tk()
    top.withdraw()  # hide window
    file_name = tkinter.filedialog.askopenfilename(parent=top)
    top.destroy()
    print(file_name)

def debug_print(text):
	print(text)




def place_ships_better():

    title_font = pygame.font.Font('freesansbold.ttf', 35)
    text = title_font.render('How do you want to place your ships?', True, "black")
    textRect = text.get_rect()
    textRect.center = (400, 100)
    place_ships_text = textbox.Text(text, textRect, screen)
    place_ships_view = screenviews.View(screen, background, [button_place_from_file, button_place_manually, button_back], [place_ships_text])
    place_ships_view.run()


# def place_ships():
#     print("in solo")
#     title_font = pygame.font.Font('freesansbold.ttf', 35)
#     text = title_font.render('How do you want to place your ships?', True, "black")
#     textRect = text.get_rect()
#     textRect.center = (400, 100)
#     ship_placement_running = True
#     while ship_placement_running:
#         screen.fill("black")
#         screen.blit(background, (0,0))
#         screen.blit(text, textRect)
#         button_place_manually.update()
#         button_place_manually.changeColor(pygame.mouse.get_pos())
#         button_place_from_file.update()
#         button_place_from_file.changeColor(pygame.mouse.get_pos())
#         button_back.update()
#         button_back.changeColor(pygame.mouse.get_pos())
#         pygame.display.update()
#         for event in pygame.event.get():
#             if not ship_placement_running:
#                 break
#             if event.type == pygame.QUIT:
#                 ship_placement_running = False
#                 break
#                 #pygame.quit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
                
#                 if button_place_from_file.checkForInput(pygame.mouse.get_pos()):
#                     print(prompt_file())
#                     #place_ships()
#                 if button_place_manually.checkForInput(pygame.mouse.get_pos()):
#                     #debug_print("manually")
#                     place_ships_manually()
#                 if button_back.checkForInput(pygame.mouse.get_pos()):
#                     print("back")
#                     main_menu()
#                     ship_placement_running = False
#                     break
        
                
            
        
    #pygame.quit()
def multy():
    print("multy")

def quit_game():
    pass

def main_menu_better():
    title_font = pygame.font.Font('freesansbold.ttf', 70)
    text = title_font.render('Battleships', True, "black")
    textRect = text.get_rect()
    textRect.center = (400, 100)
    main_menu_text = textbox.Text(text, textRect, screen)
    main_menu_view = screenviews.View(screen, background, [button_solo, button_multy, button_quit], [main_menu_text])
    main_menu_view.run()

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
#                    place_ships_better()
#                    running = False
#                    break
#                 if button_multy.checkForInput(pygame.mouse.get_pos()):
#                     debug_print("multy")
#                 if button_quit.checkForInput(pygame.mouse.get_pos()):
#                     #pygame.quit()
#                     running = False
#                     break
button_solo.set_action(place_ships_better)
button_multy.set_action(multy)
button_quit.set_action(quit_game)
button_place_manually.set_action(place_ships_manually)
button_place_from_file.set_action(prompt_file)
button_back.set_action(main_menu_better)
main_menu_better()
pygame.quit()
