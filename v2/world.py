from location import Location

from pprint import pprint,pformat


class World:
    # default world size to 5x5 but allow it to be customized (e.g. World(10))
    def __init__(self, size=5):
        # initialize each world location to a new Location object
        self.grid = [[Location() for i in range(size)] for j in range(size)]

    def __repr__(self):
        return pformat(self.grid, indent=3)
