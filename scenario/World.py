class World:
    '''
    The world is implemented as a graph where cities are nodes linked by edges
    pointing to boundary cities.
    '''
    def __init__(self):
        '''
        At the beginning the world is empty.
        '''
        self.cities = {}

    def add_city(self, city):
        '''
        We'll keep a dictionary where city names will be keys and their
        correspondent values are city objects containing all the city data.
        '''
        self.cities[city.name] = city

    def step(self):
        '''
        Check conditions for end of world, end of iterations, etc.
        '''
        pass
