import random
class Ship:

    def __init__(self, spaces : set):
        #spaces is set of coordinates of places where the ship is
        self.spaces = spaces


class Position:
    #holds the information abaout a position on the board
    NO_SHIP = 0
    def __init__(self, ship, is_shot):
        #ship is the position of a ship in the list of ships, if there is no ship on the position ship = -1
        self.ship = ship
        self.is_shot = is_shot

SIZE = 10

def check_board(board, ships):
    pass


class Game_info:
    #holds the information of a gamestate
    def __init__(self, board):
        self.board = board
        max_ship = 1
        self.shots = set()
        self.ships = []
        for row in self.board:
            for cell in row:
                max_ship = max(cell, max_ship)
        self.ships = []
        #print(self.board)
        #print(max_ship)
        for number in range(max_ship + 1):
            if number == 0:
                continue
            ship = Ship(set())
            for i in range(SIZE):
                for j in range(SIZE):
                    if number == self.board[i][j]:
                        ship.spaces.add((i,j))
            self.ships.append(ship)
            
    def shoot(self, position):
        self.shots.add(position)
        result = self.board[position[0]][position[1]]
        if result == 0:
            return Shot(position, False, False)
        else:
            return Shot(position, True, self.shots.issuperset(self.ships[result - 1].spaces))
    
    def over(self):
        #print(self.board)
        for ship in self.ships:
            if not self.shots.issuperset(ship.spaces):
                return False
        return True
    
    def ships_left(self):
        ships = dict.fromkeys([1, 2, 3, 4, 5, 6])
        for size in ships:
            ships[size] = 0
        for ship in self.ships:
            if not self.shots.issuperset(ship.spaces):
                ships[len(ship.spaces)] += 1
        return ships



class Shot:

    def __init__(self, position, succes, lethal):
        self.position = position
        self.succes = succes
        self.lethal = lethal


class Bot:
    #algorithm for solo mod
    def __init__(self):#, opposiotion_board : Game_info):
        #self.opposiotion_board = opposiotion_board
        self.options = set()
        #self.last_hit = None
        #self.successful_shots = []
        for i in range(10):
            for j in range(10):
                self.options.add((i, j))
        
    def choose_shot_random(self):
        shot = random.choice(tuple(self.options))
        self.options.remove(shot)
        return shot
        
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
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]#,
    #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    #print(visited)
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
                if ship_size > 6:
                    return False
                new_dict[ship_size] += 1
                counter += 1
    return new_dict == dict

def validate(board, dict):
    return validate_adjacency(board) and validate_dict_equivalence(board, dict)

def generate_board(ships : dict):
    #print(ships)
    board = [[0 for i in range(SIZE)] for j in range(SIZE)]
    for size in sorted(list(ships.keys()), reverse = True):
        placed = 0
        while placed !=  ships[size]:
            #print(size)
            i = random.choice(range(SIZE))
            j = random.choice(range(SIZE))
            orientation = random.choice(range(2))
            #board[i][j] = 1
            #placed += 1
            if orientation:   
                if i + size <= SIZE:
                    if all(map(lambda x: board[i + x][j] == 0, range(size))):
                        #print("ver")
                        for ic in range(size):
                            board[i+ic][j] = 1
                            
                            #print(i+ic, j)
                        #print(size)
                        placed += 1
                        #print(board)
                elif j + size <= SIZE:
                    if all(map(lambda x: board[i][j + x] == 0, range(size))):
                        #print("hor")
                        for jc in range(size):
                            board[i][j+jc] = 1
                        #print(size)  
                        placed += 1
                    #print(board)
            else:
                if j + size <= SIZE:
                    if all(map(lambda x: board[i][j + x] == 0, range(size))):
                        #print("hor")
                        for jc in range(size):
                            board[i][j+jc] = 1
                            
                            #print(i,j+jc)
                        #print(size)
                        placed += 1
                elif i + size <= SIZE:
                    if all(map(lambda x: board[i + x][j] == 0, range(size))):
                        #print("ver")
                        for ic in range(size):
                            board[i+ic][j] = 1
                            
                            #print(i+ic, j)
                        #print(size)
                        placed += 1
    #print(board)
    if not validate(board, ships):
        print("failed")
        return generate_board(ships)
    #print(board)
    return Game_info(board)
                

def getship(place: Position):
    return place.ship


# s = {1: 0, 2: 1, 3: 1, 4: 1, 5: 0, 6: 0}
# i = generate_board(s)
# print(i.board)
# print(i.ships_left())
# print(i.ships_left())
# print(i.board)

