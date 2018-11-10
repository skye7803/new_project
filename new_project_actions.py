from new_project_world import World

world = World()

class Actions:
    def __init__(self):
        self.current_location = world.world[2][2]

    def movene(self, coordinate):
        if self.current_location[coordinate] + 1 > 4 or self.current_location[coordinate] - 1 < 0:
            print('You can\'t go this way!')
        else:
            self.current_location[coordinate] += 1

    def movesw(self, coordinate):
        if self.current_location[coordinate] + 1 > 4 or self.current_location[coordinate] - 1 < 0:
            print('You can\'t go this way!')
        else:
            self.current_location[coordinate] -= 1


