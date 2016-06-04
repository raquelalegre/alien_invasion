'''
This is the entry point of the alien invasion.
'''

import argparse
from scenario.City import City
from scenario.World import World


def main():
    '''
    Create world reading from file.
    Populate world with given number of aliens.
    Loop through time steps and update world's status until world is destroyed
    or one alien has moved 10K times.
    '''

    # Read input from user
    parser = argparse.ArgumentParser(description='Aliens invasion simulations.')
    parser.add_argument('n_aliens',
                        type=int,
                        help='Number of aliens invading')
    parser.add_argument('world_map',
                        help='File containing world map description.')
    args = parser.parse_args()

    input_file = args.world_map
    print("Starting world...")
    world = World()
    world.build(input_file)
    print("The world has {} cities.".format(len(world.cities.keys())))

    print("The aliens are coming...")
    N = args.n_aliens
    world.populate(N)
    print("Aliens are ready in their initial destinations")

    print ("This is how the world looks like: ")
    for city in world.cities.values():
        print(city.__dict__)

    # TODO: Go over list of cities and move aliens around
    # TODO: Check for destructions and max moves, and update cities and world
    while world.cities:
        try:
            world.step()
        except:
            print ("World is over! An alien took 10K moves.")
    


if __name__ == '__main__':
    main()
