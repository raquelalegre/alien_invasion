import random
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
            line_elems = line.replace('\n', '').split(' ')
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
        Make aliens move to next randome city.
        Check conditions for end of world, end of iterations, etc.
        '''
        destinations = ['north', 'east', 'west', 'south']
        # for city in self.cities.values():
        #     if city.alien:
        #         for dest in destinations:
        #             if hasattr(city, dest):
        #                 possible_destinations.append(dest)
        #         random_dest = random.choice(possible_destinations)
        #         random_city_name = getattr(city, random_dest)
        #         random_city = self.cities[random_city_name]
        #         if not random_city.destroyed():
        #             if random_city.alien:
        #                 random_city.destroy()


    def populate(self, n_aliens):
        for alien_id in range(n_aliens):
            random_city_name = random.choice(list(self.cities.keys()))
            random_city = self.cities[random_city_name]
            if not random_city.destroyed:
                # If there is already an alien, destroy city. Otherwise, add it.
                if random_city.alien:
                    random_city.destroy(alien_id)
                else:
                    random_city.alien = alien_id
            else:
                # Search for another city
                # TODO should have a list of all non destroyed cities
                random_city_name = random.choice(list(self.cities.keys()))

    def update(self, city_name):
        pass
