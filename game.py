import string


class Run():

    def __init__(self):

        self.board = self.make_board()
        self.carrier = 5
        self.battleship = 4
        self.cruiser = 4
        self.submarine = 3
        self.destroyer = 2
        self.targets = []
        game_on = True

        print("Fire bombs by inputting row, col location (A2)")

        while game_on:
            fire_input = input("FIRE: ")
            fire = list(fire_input)

            if not len(fire) == 2:
                print("Invalid, incorrect input length, need char followed by number")
                continue
            if not isinstance(fire[0], str):
                print("Invalid, first item must be string")
                continue
            if not fire[1].isdigit():
                print("Invalid, second item must be integer")
                continue
            if fire_input in self.targets:
                print("Invalid, shot already taken")
                continue

            self.shoot_bomb(fire[0].lower(), int(fire[1]))

            if self.carrier == 0 and self.battleship == 0 and self.cruiser == 0 and self.submarine == 0 and self.destroyer == 0:
                game_on = False

        print("Game Over finally")

    def shoot_bomb(self, col, row):
        col_index = string.ascii_lowercase.index(col)
        self.targets.append(col + str(row))

        target = self.board[row][col_index]

        if target == 1:
            self.carrier -= 1
            print("HIT carrier! ", str(self.carrier))
            self.check_sunk(self.carrier)
        elif target == 2:
            self.battleship -= 1
            print("HIT battleship! ", str(self.battleship))
            self.check_sunk(self.battleship)
        elif target == 3:
            self.cruiser -= 1
            print("HIT cruiser! ", str(self.cruiser))
            self.check_sunk(self.cruiser)
        elif target == 4:
            self.submarine -= 1
            print("HIT submarine! ", str(self.submarine))
            self.check_sunk(self.submarine)
        elif target == 5:
            self.destroyer -= 1
            print("HIT destroyer! ", str(self.destroyer))
            self.check_sunk(self.destroyer)
        else:
            print("MISS ", str(self.targets))

    def check_sunk(self, ship):
        if ship == 0:
            print("SUNK!")

    @staticmethod
    def make_board():

        print('assembling board...')
        return [
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 2, 0, 0, 0],
            [3, 3, 3, 3, 1, 0, 2, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 4, 4, 4, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 5, 5, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

if __name__ == "__main__":
    Run()
