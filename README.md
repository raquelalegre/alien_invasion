# Alien Invasion Simulation

This is an exercise to run a simulation of an alien invasion in an imaginary world described in an input file.

# Design



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
