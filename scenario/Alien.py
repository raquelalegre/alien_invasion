class Alien:
    '''
    Represents one of the aliens invading the world.
    We need to count the number of moves to exit on 10K moves.
    '''
    def __init__(self, id):
        self.id = id
        self.moves = 0

    def move(self):
        '''
        When alien reaches 10K moves, raise exception so it can be catched from
        world and iterations stop.
        '''
        if self.moves < 10000:
            self.moves += 1
        else:
            raise
