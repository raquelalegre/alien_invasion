class Alien:
    '''
    Represents one of the aliens invading the world.
    We need to count the number of moves to exit on 10K moves.
    '''
    def __init__(self, id):
        self.id = id
        self.moves = 0

    def move(self):
        self.moves += 1
