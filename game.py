import pygame
import button
import tkinter
import tkinter.filedialog
import screenviews
import textbox
import picture
import textinput
import gamelogic
import json

GAME_SIZE = 10

pygame.init()
pygame.display.set_caption('Battleships')
def dummy():
    print("dummy")
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800
#button_font = pygame.font.SysFont("freesansbold.ttf", 35)
background = pygame.image.load('battleships.jpg')
background = pygame.transform.scale(background, (800, 500))
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

button_solo = button.Button(button.button_surface, 400, 250, "Solo")
button_multy = button.Button(button.button_surface, 400, 350, "Multy")
button_quit = button.Button(button.button_surface, 400, 450, "Quit")
button_back_to_main = button.Button(button.button_surface, 400, 450, "Back")
button_place_from_file = button.Button(button.button_surface, 400, 350, "From file")
button_place_manually = button.Button(button.button_surface, 400, 250, "Manually")
button_back_to_place_ships = button.Button(button.button_surface, 700, 400, "Back")
button_reset_board = button.Button(button.button_surface, 500, 400, "Reset Board")
button_confirm_board = button.Button(button.button_surface, 600, 460, "Confirm")
button_confirm_your_ip = button.Button(button.button_surface, 400, 350, "Confirm")
button_confirm_opponent_ip = button.Button(button.button_surface, 400, 350, "Confirm")

def file_reader(info : str):
    dict_str, list_str = info.split("&&&")
    data_dict = {int(key): value for key, value in json.loads(dict_str).items()}
    data_list = json.loads(list_str)
    #print(data_dict)
    if gamelogic.validate(data_list, data_dict):
        game_info = gamelogic.Game_info(data_list)
        battle_solo(game_info, game_info)
    else:
        place_ships()

def prompt_file():
    """Create a Tk file dialog and cleanup when finished"""
    top = tkinter.Tk()
    top.withdraw()  # hide window
    file_name = tkinter.filedialog.askopenfilename(parent=top)
    if file_name:
        with open(file_name, 'r') as file:
            file_contents = file.read()
            file_reader(file_contents)
    top.destroy()
    #print(file_name)

def debug_print(text):
	print(text)

def place_ships():

    place_ships_text = textbox.Text('How do you want to place your ships?', 'freesansbold.ttf', 35, (400, 100), screen)
    place_ships_view = screenviews.View(screen, background, [button_place_from_file, button_place_manually, button_back_to_main], [place_ships_text])
    place_ships_view.run()

def multy():
    print("multy")

def quit_game():
    pass

def confirm_board(cells : list[button.Button], selectors : list[button.Button]):
    arr = list(map(lambda x : 1 if x.image == button.button_selected_cell_surface else 0, cells))
    ships = {}
    for index, select in enumerate(selectors):
        if select.image == button.button_selected_cell_surface:
            ships[index % 6 + 1] = index // 6
    #print(ships)
    board = []
    for row in range(10):
        rowlist = []
        board.append(rowlist)
        for col in range(10):
            rowlist.append(arr[row * 10 + col])
    #print(board)
    #print(gamelogic.validate_adjacency(board))
    if gamelogic.validate(board, ships):
        b_info = gamelogic.generate_board(ships)
        p_info = gamelogic.Game_info(board)
        #print(info.ships_left())
        #info.print_ships()
        print("info")
        print(ships)
        #b_info = gamelogic.generate_board(ships)
        #print(board)
        bot = gamelogic.Bot()
        print(b_info.board)
        print("info")
        battle_solo(p_info, b_info, bot)
    else:
        place_ships_manually()

def cell_switch(cell : button.Button, cells, selectors):
    cell.image = button.button_selected_cell_surface if cell.image == button.button_cell_surface else button.button_cell_surface
    place_ships_manually(cells, selectors)

def generate_cells(start_x = 30, start_y = 180):
    cells = []
    #start_x = 30
    #start_y = 180
    for row in range(GAME_SIZE):
        for col in range(GAME_SIZE):
            cell = button.Button(button.button_cell_surface, start_x + col * 30, start_y + row * 30)
            cells.append(cell)
    return cells

def choose_ships(select : button.Button, cells, selectors):
    select.image = button.button_selected_cell_surface if select.image == button.button_cell_surface else button.button_cell_surface
    index = 0
    for selector in selectors:
        if selector == select:
            break
        index += 1
    col = index % 6
    #print(index)
    #print(col)
    while col < len(selectors):
        if col != index:
            selectors[col].image = button.button_cell_surface
        col += 6
    
    for mod in range(6):
        if all(map(lambda x: selectors[x].image == button.button_cell_surface, [x for x in range(30) if x % 6 == mod])):
            selectors[mod].image = button.button_selected_cell_surface
    place_ships_manually(cells, selectors)



def generate_ship_selection():
    buttons = []
    start_x = 420
    start_y = 190
    for row in range(5):
        for col in range(6):
            if(row == 0):
                select = button.Button(button.button_selected_cell_surface, start_x + col * 70, start_y + row * 40)
            else:
                select = button.Button(button.button_cell_surface, start_x + col * 70, start_y + row * 40)
            buttons.append(select)
    return buttons

#cells = generate_cells()

def reset_board(selectors):
    place_ships_manually([], selectors)

def place_ships_manually(cells : list[button.Button] = [], selectors : list[button.Button] = [], type = "solo"):
    if not cells:
        cells = generate_cells()
    if not selectors:
        selectors = generate_ship_selection()
    for cell in cells:
        cell.set_action(cell_switch, [cell, cells, selectors])
    for selector in selectors:
        selector.set_action(choose_ships, [selector, cells, selectors])
    buttons = list(cells)
    #print(len(selectors))
    buttons.append(button_back_to_place_ships)
    buttons.append(button_reset_board)
    buttons.append(button_confirm_board)
    buttons.extend(selectors)
    #button_confirm_board.set_action(confirm_board, [cells, selectors])
    button_confirm_board.set_action(confirm_board, [cells, selectors])
    button_reset_board.set_action(reset_board, [selectors])
    text_promp = textbox.Text("You need to place:", 'freesansbold.ttf', 35, (500, 100), screen)
    text_ship = textbox.Text("x1      x2      x3      x4      x5      x6",  'freesansbold.ttf', 25, (600, 150), screen)
    text_zero = textbox.Text("0",  'freesansbold.ttf', 25, (370, 190), screen)
    text_one = textbox.Text("1",  'freesansbold.ttf', 25, (370, 230), screen)
    text_two = textbox.Text("2",  'freesansbold.ttf', 25, (370, 270), screen)
    text_three = textbox.Text("3",  'freesansbold.ttf', 25, (370, 310), screen)
    text_four = textbox.Text("4",  'freesansbold.ttf', 25, (370, 350), screen)
    place_ships_manually_text = textbox.Text('Battleships', 'freesansbold.ttf', 70, (400, 50), screen)
    place_ships_manually_view = screenviews.View(screen, background, buttons, [place_ships_manually_text, text_promp, text_ship, text_zero, text_one, text_two, text_three, text_four])
    place_ships_manually_view.run()

def confirm_player_ip(view):
    print(view.text_result)
    multiplayer_other_ip(view.text_result)

def multiplayer_your_ip():
    main_text = textbox.Text('Battleships', 'freesansbold.ttf', 70, (400, 50), screen)
    prompt_text_yours = textbox.Text("Your IP:", "freesansbold.ttf", 35, (400, 150), screen)
    ip_input = textinput.Text_input('', 'freesansbold.ttf', 35, (400, 250), screen)
    text_picture = picture.Picture('textinput.webp', (600, 50), (100, 225), screen)
    multiplayer_view = screenviews.View(screen, background, [button_back_to_main, button_confirm_your_ip], [main_text, prompt_text_yours], [text_picture], ip_input)
    button_confirm_your_ip.set_action(confirm_player_ip, [multiplayer_view])
    multiplayer_view.run()

def multiplayer_other_ip(player_ip):
    print(player_ip)
    main_text = textbox.Text('Battleships', 'freesansbold.ttf', 70, (400, 50), screen)
    prompt_text_yours = textbox.Text("Opponents IP:", "freesansbold.ttf", 35, (400, 150), screen)
    ip_input = textinput.Text_input('', 'freesansbold.ttf', 35, (400, 250), screen)
    text_picture = picture.Picture('textinput.webp', (600, 50), (100, 225), screen)
    multiplayer_view = screenviews.View(screen, background, [button_back_to_main, button_confirm_opponent_ip], [main_text, prompt_text_yours], [text_picture], ip_input)
    multiplayer_view.run()

def generate_int_text(ships : dict, player):
    texts = []
    for size in ships:
        if player:
            texts.append(textbox.Text(ships[size].__str__(), 'freesansbold.ttf', 35, (350, 190 + 50 * (size - 1)), screen))
        else:
            texts.append(textbox.Text(ships[size].__str__(), 'freesansbold.ttf', 35, (450, 190 + 50 * (size - 1)), screen))
    return texts

def det_shot(player_board : gamelogic.Game_info, bot_board : gamelogic.Game_info, bot : gamelogic.Bot, first_turn, cell : button.Button, opponent_cells : list[button.Button], player_cells : list[button.Button]):
    cell.image = button.button_selected_cell_surface
    shoot(player_board, bot_board, bot, first_turn, opponent_cells, player_cells)

def shoot(player_board : gamelogic.Game_info, bot_board : gamelogic.Game_info, bot : gamelogic.Bot, first_turn, opponent_cells : list[button.Button], player_cells : list[button.Button]):
    for number, cell in enumerate(opponent_cells):
        if cell.image == button.button_selected_cell_surface:
            shot = bot_board.shoot((number // GAME_SIZE, number % GAME_SIZE))
            cell.image = button.button_cell_miss if bot_board.board[number // GAME_SIZE][number % GAME_SIZE] == 0 else button.button_cell_hit
            if shot.succes:
                battle_solo(player_board, bot_board, bot, True, opponent_cells, player_cells)
            else:
                battle_solo(player_board, bot_board, bot, False, opponent_cells, player_cells)

def battle_solo(player_board : gamelogic.Game_info, bot_board : gamelogic.Game_info, bot : gamelogic.Bot, firs_turn = True, opponent_cells = [], players_cells = []):
    if player_board.over() or bot_board.over():
        game_over(bot_board.over())
        return
    if not opponent_cells:
        opponent_cells = generate_cells()
    if not players_cells:
        players_cells = generate_cells(500, 180)
    
    for cell in opponent_cells:
        if cell.image == button.button_cell_surface:
            cell.set_action(det_shot, [player_board, bot_board, bot, False, cell, opponent_cells, players_cells])
        else:
            cell.set_action(battle_solo, [player_board, bot_board, bot, True, opponent_cells, players_cells])
    for cell in players_cells:
        cell.set_action(battle_solo, [player_board, bot_board, bot, True, opponent_cells, players_cells])
    for i in range(GAME_SIZE):
        for j in range(GAME_SIZE):
            if player_board.board[i][j] != 0 and players_cells[i * GAME_SIZE + j].image != button.button_cell_hit:
               players_cells[i * GAME_SIZE + j].image = button.button_selected_cell_surface
    if not firs_turn:
        coord = bot.choose_shot_random()
        shot = player_board.shoot(coord)
        players_cells[coord[0] * GAME_SIZE + coord[1]].image = button.button_cell_miss if player_board.board[coord[0]][coord[1]] == 0 else button.button_cell_hit
        while shot.succes:
            coord = bot.choose_shot_random()
            shot = player_board.shoot(coord)
            players_cells[coord[0] * GAME_SIZE + coord[1]].image = button.button_cell_miss if player_board.board[coord[0]][coord[1]] == 0 else button.button_cell_hit

    main_text = textbox.Text('Battleships', 'freesansbold.ttf', 70, (400, 50), screen)
    x1_text = textbox.Text('x1', 'freesansbold.ttf', 35, (400, 190), screen)
    x2_text = textbox.Text('x2', 'freesansbold.ttf', 35, (400, 240), screen)
    x3_text = textbox.Text('x3', 'freesansbold.ttf', 35, (400, 290), screen)
    x4_text = textbox.Text('x4', 'freesansbold.ttf', 35, (400, 340), screen)
    x5_text = textbox.Text('x5', 'freesansbold.ttf', 35, (400, 390), screen)
    x6_text = textbox.Text('x6', 'freesansbold.ttf', 35, (400, 440), screen)
    texts = [main_text, x1_text, x2_text, x3_text, x4_text, x5_text, x6_text]
    texts.extend(generate_int_text(player_board.ships_left(), True))
    texts.extend(generate_int_text(bot_board.ships_left(), False))
    buttons = []
    
    buttons.extend(players_cells)
    buttons.extend(opponent_cells)
    battle_view = screenviews.View(screen, background, buttons, texts)
    battle_view.run()

def game_over(win):
    main_text = textbox.Text('Battleships', 'freesansbold.ttf', 70, (400, 50), screen)
    if win:
        outcome = textbox.Text('You win!!!!!!', 'freesansbold.ttf', 70, (400, 150), screen)
    else:
        outcome = textbox.Text('You lose :(', 'freesansbold.ttf', 70, (400, 150), screen)
    game_over_view = screenviews.View(screen, background, [button_back_to_main], [main_text, outcome])
    game_over_view.run()

def main_menu():
    main_menu_text = textbox.Text('Battleships', 'freesansbold.ttf', 70, (400, 100), screen)
    main_menu_view = screenviews.View(screen, background, [button_solo, button_multy, button_quit], [main_menu_text])
    main_menu_view.run()

button_solo.set_action(place_ships)
button_multy.set_action(multiplayer_your_ip)
button_quit.set_action(quit_game)
button_place_manually.set_action(place_ships_manually)
button_place_from_file.set_action(prompt_file)
button_back_to_main.set_action(main_menu)
button_back_to_place_ships.set_action(place_ships)


main_menu()
pygame.quit()
