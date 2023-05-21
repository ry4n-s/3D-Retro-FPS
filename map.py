import pygame as pg

q = False
mini_map= [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, q, q, q, q, q, q, q, q, q, q, q, q, q, q, 1],
    [1, q, q, 3, 3, 3, 3, q, q, q, 2, 2, 2, q, q, 1],
    [1, q, q, q, q, q, 4, q, q, q, q, q, 2, q, q, 1],
    [1, q, q, q, q, q, 4, q, q, q, q, q, 2, q, q, 1],
    [1, q, q, 3, 3, 3, 3, q, q, q, q, q, q, q, q, 1],
    [1, q, q, q, q, q, q, q, q, q, q, q, q, q, q, 1],
    [1, q, q, q, 4, q, q, q, 4, q, q, q, q, q, q, 1],
    [1, 1, 1, 3, 1, 3, 1, 1, 1, 3, q, q, 3, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 3, q, q, 3, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 3, q, q, 3, 1, 1, 1],
    [1, 1, 3, 1, 1, 1, 1, 1, 1, 3, q, q, 3, 1, 1, 1],
    [1, 4, q, q, q, q, q, q, q, q, q, q, q, q, q, 1],
    [3, q, q, q, q, q, q, q, q, q, q, q, q, q, q, 1],
    [1, q, q, q, q, q, q, q, q, q, q, q, q, q, q, 1],
    [1, q, q, 2, q, q, q, q, q, 3, 4, q, 4, 3, q, 1],
    [1, q, q, 5, q, q, q, q, q, q, 3, q, 3, q, q, 1],
    [1, q, q, 2, q, q, q, q, q, q, q, q, q, q, q, 1],
    [1, q, q, q, q, q, q, q, q, q, q, q, q, q, q, 1],
    [3, q, q, q, q, q, q, q, q, q, q, q, q, q, q, 1],
    [1, 4, q, q, q, q, q, q, 4, q, q, 4, q, q, q, 1],
    [1, 1, 3, 3, q, q, 3, 3, 1, 3, 3, 1, 3, 1, 1, 1],
    [1, 1, 1, 3, q, q, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 3, 3, 4, q, q, 4, 3, 3, 3, 3, 3, 3, 3, 3, 1],
    [3, q, q, q, q, q, q, q, q, q, q, q, q, q, q, 3],
    [3, q, q, q, q, q, q, q, q, q, q, q, q, q, q, 3],
    [3, q, q, q, q, q, q, q, q, q, q, q, q, q, q, 3],
    [3, q, q, 5, q, q, q, 5, q, q, q, 5, q, q, q, 3],
    [3, q, q, q, q, q, q, q, q, q, q, q, q, q, q, 3],
    [3, q, q, q, q, q, q, q, q, q, q, q, q, q, q, 3],
    [3, q, q, q, q, q, q, q, q, q, q, q, q, q, q, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.rows = len(self.mini_map)
        self.cols = len(self.mini_map[0])
        self.get_map()
    
    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value
    
    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
        for pos in self.world_map]