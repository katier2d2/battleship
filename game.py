import random
from ship import Ship

class Game:

    def __init__(self, board):
        self.board = board
        self.store_ship = {}

        self.ship = Ship()

    def put_ship(self, specs):
        name = specs[0]
        dir = specs[1]
        row = int(specs[2][-1])
        col = get_index(specs[2][0])

        for i, x in enumerate(self.board):
            for j, a in enumerate(x):
                if dir == 'right':
                    if i == row and (j in range(col, col + self.ship.specs(name))):
                        if self.check_placement(i, j) is False:
                            self.board[i][j] = self.ship.id(name)
                            # store_ship = ship_store(self.name, i, j)
                        else:
                            raise ValueError('invalid placement')
                elif dir == 'down':
                    if j == col and (i in range(row, row + self.ship.specs(name))):
                        if self.check_placement(i, j) is False:
                            self.board[i][j] = self.ship.id(name)
                        else:
                            raise ValueError('invalid placement')

        print('Placed {}'.format(name))

    def update_board(self, row, col, outcome):

        self.board[row][col] = outcome


    def fire(self, location):

        row = int(location[-1])
        col = get_index(location[0])

        ship_id = self.check_placement(row, col)

        if isinstance(ship_id, int):
            if ship_id == 0:
                self.update_board(row, col, 'M')
                print('Miss!')
            else:
                print('Hit!')
                self.ship.hit(ship_id)
                self.update_board(row, col, 'H')

    def check_placement(self, row, col):
        if self.board[row][col] == 0:
            return False
        return self.board[row][col]

    def print_board(self):
        for row in self.board:
            for col in row:
                print '{}'.format(col),
            print '\n',


def get_index(col):
    col_index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    return col_index.index(col.lower())

def get_letter(num):
    col_index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    return col_index[num]

if __name__ == '__main__':

    game_on = True

    board = []
    for i in range(0, 10):
        board.append([0 for x in range(0, 10)])


    battleship = Game(board)

    print('PLACE SHIPS')

    # for i in range(0, 5):
    #     place_ship_input = raw_input('')  # PLACE_SHIP Destroyer right A1

    list_of_commands = [
        'PLACE_SHIP Destroyer right A1',
        'PLACE_SHIP Carrier down B2',
        'PLACE_SHIP Battleship down J4',
        'PLACE_SHIP Submarine right E6',
        'PLACE_SHIP Cruiser right H10']

    for place_ship_input in list_of_commands:
        place_ship_input = place_ship_input.split(' ')

        if place_ship_input.pop(0) == 'PLACE_SHIP':
            battleship.put_ship(place_ship_input)
        else:
            raise ValueError('invalid command, must start with "PLACE_SHIP"')

    battleship.print_board()


    # FIRE A4
    print('\nFIRE ON SHIPS')

    while len(battleship.ship.ship_id) > 0:
        # fire_loc = raw_input('')
        fire_loc = 'FIRE {}{}'.format(get_letter(random.randint(0,9)).upper(),random.randint(0,9))
        print fire_loc

        fire_loc = fire_loc.split(' ')

        if fire_loc.pop(0) == 'FIRE':
            battleship.fire(fire_loc[0])
        else:
            raise ValueError('invalid command, must start with "FIRE"')

    battleship.print_board()

    print('Game Over')
