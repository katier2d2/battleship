
class Ship:

    def __init__(self):

        self.ship_id = {
            'Carrier': 1,
            'Battleship': 2,
            'Cruiser': 3,
            'Submarine': 4,
            'Destroyer': 5
        }

        self.spec = {
            'Carrier': 5,
            'Battleship': 4,
            'Cruiser': 3,
            'Submarine': 3,
            'Destroyer': 2
        }

        self.status = {
            'Carrier': 0,
            'Battleship': 0,
            'Cruiser': 0,
            'Submarine': 0,
            'Destroyer': 0
        }

    def specs(self, ship):

        return self.spec.get(ship)

    def id(self, ship):

        return self.ship_id.get(ship)

    def hit(self, id):

        for k,v in self.ship_id.iteritems():
            if id == v:
                ship = k

                self.status[ship] += 1

        if self.status[ship] == self.spec[ship]:
            print('Sunk {}'.format(ship))
            self.ship_id.pop(ship)
