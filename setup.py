import pygame as pg
import random


# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)
LIGHT_GREY = (211, 211, 211)
DARK_GREEN = (1, 50, 32)
LIGHT_GREEN = (144, 238, 144)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)

GRID_SIZE = 20
NODE_SIZE = 19
ROWS = 30
COLS = 60
FPS = 60
BARRIER_CHANCE = 0.35


NODE_STATES = {
    'start': GREEN,
    'end': RED,
    'barrier': BLACK,
    'path': YELLOW,
    'search': GREY,
    'free': WHITE,
    'current': LIGHT_GREY,
    'debug1': DARK_GREEN,
    'debug2': LIGHT_GREEN,
    'debug3': PURPLE,
    'debug4': PINK
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
        self.previous = None
    
    def draw(self, screen):
        pg.draw.rect(screen, self.colour, (self.x, self.y, NODE_SIZE, NODE_SIZE))

    def change_state(self, new_state):
        self.state = new_state
        self.colour = NODE_STATES[new_state]
    
    def return_state(self):
        return self.state

    def is_barrier(self) -> bool:
        return self.state == 'barrier'

    def update_neighbours(self, grid):
        if self.row < COLS - 1 and not grid[self.row + 1][self.col].is_barrier():
            # BELOW
            self.neighbours.append(grid[self.row + 1][self.col])
        
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            # ABOVE
            self.neighbours.append(grid[self.row - 1][self.col])

        if self.col < ROWS - 1 and not grid[self.row][self.col + 1].is_barrier():
            # RIGHT
            self.neighbours.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            # LEFT
            self.neighbours.append(grid[self.row][self.col - 1])


def make_grid(barrier_chance=0.25):
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