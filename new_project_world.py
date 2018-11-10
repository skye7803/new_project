import random

class World:
    def __init__(self):
        self.world = {

        }

        for y in range(5):
            self.world[y] = {

            }
            for x in range(5):
                self.world[y][x] = {
                    'x' : x,
                    'y' : y,
                }
                generation_num = random.choice([1, 2, 3, 4])
                self.biome_assignment(generation_num, y, x)


    def biome_assignment(self, generation_num, y, x):
        if generation_num == 1:
            self.world[y][x]['biome'] = 'swamp'
        elif generation_num == 2:
            self.world[y][x]['biome'] = 'forest'
        elif generation_num == 3:
            self.world[y][x]['biome'] = 'mountain'
        elif generation_num == 4:
            self.world[y][x]['biome'] = 'plains'