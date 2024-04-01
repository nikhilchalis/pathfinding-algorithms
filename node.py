from constants import *
import pygame as pg
import numpy as np

# node state colours
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
    def __init__(self, row, col, offset, state='free'):
        self.row = row
        self.col = col
        
        self.y = col * GRID_SIZE + GRID_SIZE * np.sqrt(3)/2 + HEIGHT_OFFSET_PX
        self.state = state
        self.colour = NODE_STATES[state]
        self.neighbours = []
        self.distance = float('inf')
        self.previous = None

        if offset:
            self.x = row * GRID_SIZE + WIDTH_OFFSET_PX + GRID_SIZE/2
        else:
            self.x = row * GRID_SIZE + WIDTH_OFFSET_PX

    
    def draw(self, screen):
        pg.draw.circle(screen, self.colour, (self.x, self.y), NODE_SIZE/2)

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