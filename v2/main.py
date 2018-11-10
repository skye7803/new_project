from world import World
from player import Player


class Main:

    actions = {
        'help': {
            'commands': ['h', 'help'],
            'description': 'Show this help text',
        },
        'north': {
            'commands': ['n', 'north'],
            'description': 'Move in a north direction',
        },
        'south': {
            'commands': ['s', 'south'],
            'description': 'Move in a south direction',
        },
        'east': {
            'commands': ['e', 'east'],
            'description': 'Move in a east direction',
        },
        'west': {
            'commands': ['w', 'west'],
            'description': 'Move in a west direction',
        },
        'quit': {
            'commands': ['q', 'quit'],
            'description': 'End the game',
        },
    }

    world_size = 4

    def __init__(self):
        self.world = World(Main.world_size)

        self.player = Player()
        self.player.x = int(Main.world_size / 2)
        self.player.y = int(Main.world_size / 2)

    def mainloop(self):
        print('Welcome to the game...creatively named:')
        print('''
 _   _ _______        ______  ____   ___      _ _____ ____ _____
| \ | | ____\ \      / /  _ \|  _ \ / _ \    | | ____/ ___|_   _|
|  \| |  _|  \ \ /\ / /| |_) | |_) | | | |_  | |  _|| |     | |
| |\  | |___  \ V  V / |  __/|  _ <| |_| | |_| | |__| |___  | |
|_| \_|_____|  \_/\_/  |_|   |_| \_\\\___/ \___/|_____\____| |_|
''')

        self.show_help()

        print(self.world)  # debug

        while True:
            location = self.player_location()

            print(f'location: ({self.player.x + 1}, {self.player.y + 1})')  # debug (add one to make counting easy)

            print(f'You are in a {location}, it is {location.description()}')  # could use location.biome also
            command = input('What would you like to do? ')

            if command in Main.actions['help']['commands']:
                self.show_help()
            elif command in Main.actions['north']['commands']:
                self.move('north')
            elif command in Main.actions['south']['commands']:
                self.move('south')
            elif command in Main.actions['east']['commands']:
                self.move('east')
            elif command in Main.actions['west']['commands']:
                self.move('west')
            elif command in Main.actions['quit']['commands']:
                self.quit()

        print('_' * 79)

    def show_help(self):
        print('Available Commands:')
        for name, action in Main.actions.items():

            commands = ','.join(action['commands'])
            description = action['description']

            # example of one way to have multiple prints show up on one line (set the "end" to something else)
            # print(commands, end=': ')
            # print(description)

            # better way to print help (lines everything up nicely by adding spaces so commands is always 8 chars wide)
            # https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals
            print(f'{commands:8} ->  {description}')

        print()  # extra newline

    def player_location(self):
        return self.world.grid[self.player.x][self.player.y]

    def show_blockage(self, direction):
        print(f"You can't go {direction} because {self.player_location().blockage()}")

    def move(self, direction):
        if direction == 'north':
            if self.player.x == 0:
                self.show_blockage(direction)
            else:
                self.player.x -= 1
        elif direction == 'south':
            if self.player.x == self.world_size - 1:  # account for 0-index arrays
                self.show_blockage(direction)
            else:
                self.player.x += 1
        elif direction == 'east':
            if self.player.y == self.world_size - 1:  # account for 0-index arrays
                self.show_blockage(direction)
            else:
                self.player.y += 1
        elif direction == 'west':
            if self.player.y == 0:
                self.show_blockage(direction)
            else:
                self.player.y -= 1

    def quit(self):
        confirm = input("Are you sure you want to quit the game? ('y' or 'yes' to end): ")

        if confirm not in ['y', 'yes']:
            return

        print('''
 ____             _
| __ ) _   _  ___| |
|  _ \| | | |/ _ \ |
| |_) | |_| |  __/_|
|____/ \__, |\___(_)
       |___/
    ''')
        exit(0)


Main().mainloop()
