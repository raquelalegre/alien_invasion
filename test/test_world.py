from ..scenario.World import World


class TestWorld:
    def test_small_world(self):
        '''
        There's 28 cities in the small world map.
        '''
        world = World()
        world.build('resources/world_map_small.txt')
        n_cities = len(world.cities.keys())
        assert n_cities == 28

    def test_medium_world(self):
        '''
        There's 6763 cities in the medium world map.
        '''
        world = World()
        world.build('resources/world_map_medium.txt')
        n_cities = len(world.cities.keys())
        assert n_cities == 6763
