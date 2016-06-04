# Alien Invasion Simulation

This is an exercise to run a simulation of an alien invasion in an imaginary world described in an input file.

# Design

## Data structures and OOD
I've chosen to represent the world scenario in a graph where each city is a node and is linked to other cities/nodes via edges that can be north, south, east and west.

To implement that graph in Python, I have created a dictionary which contains one element per city with the id being the city name and the value an instance of a city object. 

When a city is destroyed, I considered completely removing it from the data structure, but the cost in performance of updating all the edges in the rest of the cities was too high, so I decided to make cities have a boolean attribute to indicate where they are destroyed or not. This way, when aliens move around, they just need to check first if the city is destroyed or not. 


# Problems
* The simulation is unfinished because I run out of time. The world is created successfully from input world map files and the aliens are assigned to their random cities, destroying the ones where there was already another alien. However, I couldn't finish the implementation of the aliens moving around the world. 

* Aliens that are randomly sent to a destroyed city should keep on trying to find another city that is not destroyed. This is not a good approach. I should have kept a list of cities that are not destroyed and randomize those instead of the full list of cities.

* The code needs more texts as well as more exception control. For example, if the input file doesn't exist, the program should raise an exception and it's not doing it at the moment.

* During the move step, I need to keep track if an alien has been moved in this iteration or not in order not to move it twice in the same iteration. I didn't have to implement this either.

* Latest changes that won't work are in the development branch in this repo.


# Usage:

To obtain this repo:

`git clone https://github.com/raquel-ucl/alien_invasion.git`

To run the simulation of the invasion, you need to execute `main.py` which receives two arguments. See help:

```bash
cd alien_invasion
python main.py -h
```

For 100 aliens in the small world example:
```bash
python main.py 100 resources/resources/world_map_small.txt
```

# Testing 

There was only time for two short tests which can be run with py.test, for example.
You can install it like this:
`pip install -r requirements.txt`

The run the tests:
`py.test -v`
