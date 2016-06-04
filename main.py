'''
This is the entry point of the exercise.
'''

from scenario.City import City
from scenario.World import World


def main():
    '''
    Create world reading from file.
    Populate world with aliens.
    Loop through time steps and update world's status until world is destroyed
    or one alien has moved 10K times.
    '''
    # TODO: take path to world map file as input.
    input_file = 'resources/world_map_small.txt'
    print("Starting world...")
    world = World()
    world.build(input_file)
    print("The world has {} cities.".format(len(world.cities.keys())))

    # TODO: take number of aliens as input
    print("The aliens are coming...")
    N = 100
    world.populate(N)
    print("Aliens are ready in their initial destinations")

    for city in world.cities.values():
        print(city.__dict__)

    # TODO: Go over list of cities and move aliens around
    # TODO: Check for destructions and update cities and world


if __name__ == '__main__':
    main()
