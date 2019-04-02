import os
import sys
import argparse




def build_board():
    board = []

    for i in range(0,10):
        board.append([0 for x in range(0,10)])

    return board

def print_board(board):
    for row in board:
        print(row)

def check_placement(board, row, col):
    if not board[row][col] == 0:
        return False
    return True

def get_index(a):
    a_index = ['a','b','c','d','e','f','g','h','i','j']

    return a_index.index(a.lower())


def store_hit(board, row, col):
    pass

def put_ship(specs, board, store_ship):
    ship = specs[0]  # Destroyer
    dir = specs[1]   # right B3
    a = specs[2][0]   # B
    n = int(specs[2][-1])  # 3


    ship_specs = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
    ship_names = {'Carrier': 9, 'Battleship': 8, 'Cruiser': 5, 'Submarine': 3, 'Destroyer': 1}

    col = get_index(a)

    for i,x in enumerate(board):
        for j,a in enumerate(x):
            if dir == 'right':
                if i == n and (j in range(col, col + ship_specs[ship])):
                    if check_placement(board, i,j):
                        board[i][j] = ship_names[ship]
                        if store_ship.get(ship, None) is None:
                            store_ship[ship] = [i, j]
                        else:
                            store_ship[ship] = store_ship[ship].append([i, j])
                    else:
                        raise ValueError('invalid placement')
            elif dir == 'down':
                if j == col and (i in range(n, n + ship_specs[ship])):
                    if check_placement(board, i,j):
                        board[i][j] = ship_names[ship]
                    else:
                        raise ValueError('invalid placement')

    return board, store_ship

def fire(loc, board):
    a = loc[0]  # B
    n = int(loc[-1])  # 3

    row = n
    col = get_index(a)

    if not check_placement(board, row, col):
        print('HIT')
        store_hit(board, row, col)

    return board


board = build_board()
store_ship = {}

print('PLACE SHIPS')

# board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 9, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 9, 3, 0, 0, 0, 0, 0, 0, 0],
# [0, 9, 3, 0, 0, 0, 0, 0, 0, 0],
# [0, 9, 3, 0, 0, 0, 0, 0, 0, 0],
# [0, 9, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

for i in range(0, 2):
    place_ship = raw_input('') #PLACE_SHIP Destroyer right A1


    place_ship = place_ship.split(' ')
    if place_ship.pop(0) == 'PLACE_SHIP':
        board, store_ship = put_ship(place_ship, board, store_ship)
    else:
        raise ValueError('invalid command, must start with "PLACE_SHIP"')

# FIRE A4
print('\nFIRE ON SHIPS')

fire_loc = raw_input('')
fire_loc = fire_loc.split(' ')

if fire_loc.pop(0) == 'FIRE':
    board = fire(fire_loc[0], board)
else:
    raise ValueError('invalid command, must start with "PLACE_SHIP"')

print_board(board)
