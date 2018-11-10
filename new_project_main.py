from new_project_actions import Actions
from new_project_world import World
import pprint

actions = Actions()
world = World()

print(world.world)

class Main:
    def __init__(self):
        self.helplist = ['help, north, east, west']

    def mainloop(self):
        print('The world is yours, conquer it!')
        print('You are in a ' + actions.current_location['biome'])
        self.command = input('What would you like to do?')

        if self.command == 'north':
            actions.movene('y')
        elif self.command == 'south':
            actions.movesw('y')
        elif self.command == 'east':
            actions.movene('x')
        elif self.command == 'west':
            actions.movesw('x')

main = Main()

while True:
    main.mainloop()

