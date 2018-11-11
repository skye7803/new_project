import random

class World:
    def __init__(self):
        self.j = random.randint(1, 25)

        self.world = {

        }
        self.i = 0
        for self.y in range(5):
            self.world[self.y] = {

            }
            for self.x in range(5):
                self.world[self.y][self.x] = {
                    'x' : self.x,
                    'y' : self.y,
                }
                self.i += 1
                generation_num = random.choice([1, 2, 3, 4])
                self.biome_assignment(generation_num, self.y, self.x)

    def biome_assignment(self, generation_num, y, x):
        if generation_num == 1:
            self.world[y][x]['biome'] = 'swamp'
        elif generation_num == 2:
            self.world[y][x]['biome'] = 'forest'
        elif generation_num == 3:
            self.world[y][x]['biome'] = 'mountain'
        elif generation_num == 4:
            self.world[y][x]['biome'] = 'plains'
        self.world[y][x]['num'] = self.i
        if self.j == self.world[y][x]['num']:
            self.world[y][x]['biome'] = 'town'