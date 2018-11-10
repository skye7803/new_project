import random


class Location:

    # all possible biomes
    biomes = {
        'swamp': {
            'adjectives': ['smelly', 'putrid', 'disgusting', 'muggy', 'swampy', 'dreary'],
            'blockage': 'the swamp is too putrid to pass through',
        },
        'forest': {
            'adjectives': ['green', 'leafy', 'chirpy', 'dark', 'eerie'],
            'blockage': 'the forest is too dense to go that way',
        },
        'mountain': {
            'adjectives': ['steep', 'craggy', 'cold', 'windy', 'treacherous', 'airy'],
            'blockage': 'the mountain is too steep to climb',
        },
        'plains': {
            'adjectives': ['plain', 'grassy', 'breezy', 'warm', 'pleasant', 'boring'],
            'blockage': 'the plains seem to go on forever in that direction and you lose hope and turn back',
        },
    }

    def description(self):
        adjective = random.choice(Location.biomes[self.biome]['adjectives'])
        return f"it is {adjective} here"

    def blockage(self):
        return Location.biomes[self.biome]['blockage']

    def __init__(self):
        # assign a random biome on creation of this location
        self.biome = random.choice(list(Location.biomes))

    def __repr__(self):
        return self.biome
