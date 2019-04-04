
class BattleShip:

    def __init__(self, board):
        self.board = board
        self.store_ship = {}

        self.ship_specs = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
        self.ship_names = {'Carrier': 9, 'Battleship': 8, 'Cruiser': 5, 'Submarine': 3, 'Destroyer': 1}

    def put_ship(self, specs):
        ship = specs[0]
        dir = specs[1]
        row = int(specs[2][-1])
        col = self.get_index(specs[2][0])

        for i, x in enumerate(self.board):
            for j, a in enumerate(x):
                if dir == 'right':
                    if i == row and (j in range(col, col + self.ship_specs[ship])):
                        if self.check_placement(i, j):
                            self.board[i][j] = self.ship_specs[ship]
                            # store_ship = ship_store(self.ship, i, j)
                        else:
                            raise ValueError('invalid placement')
                elif dir == 'down':
                    if j == col and (i in range(row, row + self.ship_specs[ship])):
                        if self.check_placement(i, j):
                            self.board[i][j] = self.ship_names[ship]
                        else:
                            raise ValueError('invalid placement')

        print('Placed {}'.format(ship))

    def fire(self, location):

        row = int(location[-1])
        col = self.get_index(location[0])

        if not self.check_placement(row, col):
            print('Hit')
            self.store_hit()
            # return board, False   ## test for game over

        else:
            print('Miss')


    def store_hit(self):
        pass

    def check_placement(self, row, col):
        if not self.board[row][col] == 0:
            return False
        return True

    def get_index(self, col):
        col_index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        return col_index.index(col.lower())

    def ship_store(self, ship, row, col):
        pass

    def print_board(self):
        for row in self.board:
            print(row)


if __name__ == '__main__':

    game_on = True

    board = []
    for i in range(0, 10):
        board.append([0 for x in range(0, 10)])


    battleship = BattleShip(board)

    print('PLACE SHIPS')

    for i in range(0, 1):
        place_ship_input = raw_input('')  # PLACE_SHIP Destroyer right A1
        place_ship_input = place_ship_input.split(' ')

        if place_ship_input.pop(0) == 'PLACE_SHIP':
            battleship.put_ship(place_ship_input)
        else:
            raise ValueError('invalid command, must start with "PLACE_SHIP"')

        battleship.print_board()


    # FIRE A4
    print('\nFIRE ON SHIPS')

    while game_on == True:
        fire_loc = raw_input('')
        fire_loc = fire_loc.split(' ')

        if fire_loc.pop(0) == 'FIRE':
            battleship.fire(fire_loc[0])
        else:
            raise ValueError('invalid command, must start with "FIRE"')

        battleship.print_board()

    print('Game Over')



"""
PLACE_SHIP Destroyer right A1
PLACE_SHIP Carrier down B2
PLACE_SHIP Battleship down J4
PLACE_SHIP Submarine right E6
PLACE_SHIP Cruiser right H10

FIRE A4
FIRE B7
FIRE B3
FIRE H5

"""