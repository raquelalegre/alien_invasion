from .City import City

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


    def build(self, input_file):
        '''
        Go through input file. Each line looks like this:
        city_name north=Mu south=Aninige east=Dimilu west=Asmismu
        Parse it and create a city object, then add it to world.
        '''
        try:
            f = open(input_file, 'r')
        except FileNotFoundError:
            print("Input file {} doesn't exist.".format(input_file))
            return

        for line in f:
            line_elems = line.split(' ')
            # First element is the city name
            city = City(line_elems[0])
            # Rest of elements are the boundaries and can vary in number.
            boundaries = line_elems[1:]
            for boundary in boundaries:
                # Boundaries are in the form 'norht|south|west|east=city_name'
                coord, destination = boundary.split('=')
                # Add neighbouring city to currect city
                setattr(city, coord, destination)
            self._add_city(city)


    def _add_city(self, city):
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


    def populate_world_from_file():
        world = World()

        f = open(path, 'r')
        for line in f:
            # E north=Mu south=Aninige east=Dimilu west=Asmismu
            line_elems = line.split(' ')
            city = City(line_elems[0])
            boundaries = line_elems[1:]
            for boundary in boundaries:
                coord, destination = boundary.split('=')
                setattr(city, coord, destination)
            world.add_city(city)
        print(world.__dict__)
