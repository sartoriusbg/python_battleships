import random
import copy
class Ship:

    def __init__(self, spaces):
        #spaces is list of coordinates of places where the ship is
        self.spaces = spaces


class Position:
    #holds the information abaout a position on the board
    NO_SHIP = -1
    def __init__(self, ship, is_shot):
        #ship is the position of a ship in the list of ships, if there is no ship on the position ship = -1
        self.ship = ship
        self.is_shot = is_shot

SIZE = 10

def check_board(board, ships):
    pass


# class Game_info:
#     #holds the information of a gamestate

#     def __init__(self, size, ships:list):
#         self.size = size
#         self.ships = ships
#         self.board = []
#         for row in range(size):
#             self.board.append([])
#             for _ in range(size):
#                 self.board[row].append(Position( Position.NO_SHIP, False))

#         for ship in enumerate(ships):
#             for place in ship[1].spaces:
#                 self.board[place[0]][place[1]].ship = ship[0]
    
#     def get_ship(self, place: Position):
#         return place.ship
    
#     def get_shot(self,place: Position):
#         if place.is_shot:
#             return place.ship
#         else:
#             return "?"

#     def print_player_board(self):
#         for row in self.board:
#             list_row = list(map(self._get_ship, row))
#             print(list_row)
    
#     def print_oponent_board(self):
#         for row in self.board:
#             list_row = list(map(self._get_shot, row))
#             print(list_row)
    
#     def game_over(self):
#         for ship in self.ships:
#             for position in ship.spaces:
#                 if not position.is_shot:
#                     return False
#         return True

class Shot:

    def __init__(self, position, succes, lethal):
        self.position = position
        self.succes = succes
        self.lethal = lethal


# class Bot:
#     #algorithm for solo mod
#     def __init__(self, opposiotion_board : Game_info):
#         self.opposiotion_board = opposiotion_board
#         self.options = set()
#         self.last_hit = None
#         for i in range(10):
#             for j in range(10):
#                 self.options.add((i, j))
        
        
#     def _choose_shot_random(self):
#         return random.choice(tuple(self.options))
        

#     def _choose_shot_neighbour(self):
#         if self.last_hit.lethal:
#             return self._choose_shot_random()
#         else:
#             if self.opposiotion_board._get_shot(self.last_hit.position + (1, 0)) == '?':
#                 return self.last_hit.position + (1,0)
#             if self.opposiotion_board._get_shot(self.last_hit.position + (-1, 0)) == '?':
#                 return self.last_hit.position + (-1,0)
#             if self.opposiotion_board._get_shot(self.last_hit.position + (0, -1)) == '?':
#                 return self.last_hit.position + (0, -1)
#             if self.opposiotion_board._get_shot(self.last_hit.position + (0, 1)) == '?':
#                 return self.last_hit.position + (0, 1)
        


#     def action(self, last_shot:Shot):
#         #last_hit contains the info about the last succesful Shot (position and if it was fatal)
#         if last_shot.succes():
#             self.last_hit = last_shot
#         if not self.last_hit:
#             return self._choose_shot_random()
#         else:
#             return self._choose_shot_neighbour()
        
def validate_adjacency(board):

    if not isinstance(board, list):
        return False

    if not board or not isinstance(board[0], list):
        return False

    rows = len(board)
    cols = len(board[0])

    if rows < 1 or cols < 1:
        return False

    if any(len(row) != cols for row in board):
        return False

    valid_characters = {0, 1}
    for row in board:
        for cell in row:
            if cell not in valid_characters:
                return False


    for row in range(rows):
        for col in range(cols):

            if row - 1 < 0 or row + 1 >= rows or col - 1 < 0 or col + 1 >= cols or board[row][col] != 1:
                continue

            up = board[row - 1][col] if row - 1 >= 0 else False
            down = board[row + 1][col - 1] if row + 1 < rows else False
            left = board[row][col - 1] if col - 1 >= 0 else False
            right = board[row][col + 1] if col + 1 < cols else False

            horizontal = any([up, down])
            vertical = any([left, right])

            if horizontal & vertical:
                return False

    return True

def validate_dict_equivalence(board, dict):

    visited = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print(visited)
    new_dict = {key:0 for key in dict.keys()}

    rows = len(board)
    cols = len(board[0])
    counter = 1
    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != 1 or visited[row][col] == -1:
            return 0

        visited[row][col] = -1
        if board[row][col] == 1:
            board[row][col] = counter
        size = 1
        size += dfs(row + 1, col)
        size += dfs(row - 1, col)
        size += dfs(row, col + 1)
        size += dfs(row, col - 1)
        return size

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                ship_size = dfs(i, j)
                if ship_size == 0:
                    continue
                new_dict[ship_size] += 1
                counter += 1
    return new_dict == dict

def validate(board, dict):
    return validate_adjacency(board) & validate_dict_equivalence(board, dict)

def getship(place: Position):
    return place.ship
