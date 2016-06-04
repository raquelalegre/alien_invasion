class City:
    '''
    Represents each node in the world graph structure.
    Node's id is city's name, and the edges are the boundary cities.
    We need to mark each node as destroyed or not, and know how many aliens
    there are in a city at a given time (2 or more aliens destroy the city).
    When the city is destroyed, it is not removed from the world, it's kept
    so that we don't have to loop through the whole structure to remove all
    edges pointint to the destroyed city. This way it should be more performant.
    '''
    def __init__(self, name):
        self.name = name
        self.destroyed = False
        self.alien = None

    def destroy(self, incoming_alien):
        '''
        Alien incoming_alien has arrived to a previously occupied city.
        Mark city as destroyed and print message.
        '''
        self.destroyed = True
        print("{} has been destroyed by alien {} and alien {}!".format(
            self.name,
            self.alien,
            incoming_alien
            )
        )
