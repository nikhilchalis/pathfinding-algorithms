import pygame as pg
import random


# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)

GRID_SIZE = 20
NODE_SIZE = 19
ROWS = 40
COLS = 60
FPS = 25


NODE_STATES = {
    'start': GREEN,
    'end': RED,
    'barrier': BLACK,
    'path': YELLOW,
    'search': GREY,
    'free': WHITE
}


class Node:
    def __init__(self, row, col, state='free'):
        self.row = row
        self.col = col
        self.x = row * GRID_SIZE
        self.y = col * GRID_SIZE
        self.state = state
        self.colour = NODE_STATES[state]
        self.neighbours = []
        self.distance = float('inf')
        self.prev = None
    
    def draw(self, screen):
        pg.draw.rect(screen, self.colour, (self.x, self.y, NODE_SIZE, NODE_SIZE))
    
    def change_state(self, new_state):
        self.state = new_state
        self.colour = NODE_STATES[new_state]
    
    def return_state(self):
        return self.state

    def is_barrier(self) -> bool:
        return self.state == 'barrier'


def make_grid(barrier_chance=0.3):
    grid = []
    for i in range(COLS):
        grid.append([])
        for j in range(ROWS):
            node = Node(i, j)
            # randomly assigning barrier
            random_number = random.random()
            if random_number < barrier_chance:
                node.change_state('barrier')

            grid[i].append(node)
    
    return grid
    

def display_grid(screen, grid):
    for row in grid:
        for node in row:
            node.draw(screen)
    
    pg.display.update()