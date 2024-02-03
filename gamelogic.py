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
    

class Game_info:
    #holds the information of a gamestate, ships are all 4x1 rectangles

    def __init__(self, size, ships:list):
        self.size = size
        self.ships = ships
        self.board = []
        for row in range(size):
            self.board.append([])
            for _ in range(size):
                self.board[row].append(Position( Position.NO_SHIP, False))

        for ship in enumerate(ships):
            for place in ship[1].spaces:
                self.board[place[0]][place[1]].ship = ship[0]
    
    def _get_ship(self, place: Position):
        return place.ship
    
    def _get_shot(self,place: Position):
        if place.is_shot:
            return place.ship
        else:
            return "?"

    def print_player_board(self):
        for row in self.board:
            list_row = list(map(self._get_ship, row))
            print(list_row)
    
    def print_oponent_board(self):
        for row in self.board:
            list_row = list(map(self._get_shot, row))
            print(list_row)
    
    def game_over(self):
        for ship in self.ships:
            for position in ship.spaces:
                if not position.is_shot:
                    return False
        return True

class Shot:

    def __init__(self, position, succes, lethal):
        self.position = position
        self.succes = succes
        self.lethal = lethal


class Bot:
    #algorithm for solo mod
    def __init__(self, oposiotion_board : Game_info):
        self.oposiotion_board = oposiotion_board
        self.options = set()
        
        
    def _choose_shot_random(self):
        pass

    def _choose_shot_neighbour(self, last_hit: Shot):
        pass
    def action(self, last_hit:Shot):
        #last_hit contains the info about the last succesful Shot (position and if it was fatal)
        
        

class Game:
    #main logic of the game
    def __init__(self, type) -> None:
        self.type = type
    
    def solo(self, player_board: Game_info):
        pass

    def multyplayer(self):
        pass

    def play(self):
        if type == "solo":
            self.solo()
        else:
            self.multyplayer()

def getship(place: Position):
    return place.ship

ship1 = Ship([(1,2), (1,3), (1,4)])
ship2 = Ship([(3,0), (4,0), (5,0)])

test = Game_info(10, [ship1, ship2])
test.board[1][1].is_shot = True
test.print_player_board()
test.print_oponent_board()
