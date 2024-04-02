from constants import *
import pygame as pg

# node state colours
NODE_STATES = {
    'start': START,
    'end': END,
    'barrier': BACKGROUND,
    'path': PATH,
    'search': PURPLE,
    'free': FREE,
    'current': LIGHT_GREY,
    'none': None,
    'debug1': DARK_GREEN,
    'debug2': LIGHT_GREEN,
    'debug3': PURPLE,
    'debug4': PINK
}


class Node:
    def __init__(self, row, col, state='free'):
        self.row = row
        self.col = col
        self.x = row * GRID_SIZE + WIDTH_OFFSET_PX
        self.y = col * GRID_SIZE * np.sqrt(3) + HEIGHT_OFFSET_PX
        self.state = state
        self.colour = NODE_STATES[state]
        self.neighbours = []
        self.distance = float('inf')
        self.previous = None


    
    def draw(self, screen):
        pg.draw.ellipse(screen, self.colour, (self.x, self.y, NODE_SIZE, NODE_SIZE))

    def change_state(self, new_state):
        self.state = new_state
        self.colour = NODE_STATES[new_state]
    
    def return_state(self):
        return self.state

    def is_barrier(self) -> bool:
        return self.state == 'barrier'

    def is_none(self) -> bool:
        return self.state == 'none'

    def update_neighbours(self, grid):
        if self.row < COLS - 1 and self.col < ROWS - 1 and (grid[self.row + 1][self.col + 1].is_barrier() == False and grid[self.row + 1][self.col + 1].is_none() == False):
            # LOWER RIGHT node
            self.neighbours.append(grid[self.row + 1][self.col + 1])
        
        if self.row < COLS - 2 and self.col < ROWS and (grid[self.row + 2][self.col].is_barrier() == False and grid[self.row + 2][self.col].is_none() == False):
            # RIGHT node
            self.neighbours.append(grid[self.row + 2][self.col])
        
        if self.row < COLS - 1 and self.col > 0 and (grid[self.row + 1][self.col - 1].is_barrier() == False and grid[self.row + 1][self.col - 1].is_none() == False):
            # UPPER RIGHT node
            self.neighbours.append(grid[self.row + 1][self.col - 1])
        
        if self.row > 0 and self.col < ROWS - 1 and (grid[self.row - 1][self.col + 1].is_barrier() == False and grid[self.row - 1][self.col + 1].is_none() == False):
            # LOWER LEFT
            self.neighbours.append(grid[self.row - 1][self.col + 1])
        
        if self.row > 1 and self.col < ROWS - 1 and (grid[self.row - 2][self.col].is_barrier() == False and grid[self.row  - 2][self.col].is_none() == False):
            # LEFT
            self.neighbours.append(grid[self.row - 2][self.col])
        
        if self.row > 0 and self.col < ROWS - 1 and (grid[self.row - 1][self.col - 1].is_barrier() == False and grid[self.row - 1][self.col - 1].is_none() == False):
            # TOP LEFT
            self.neighbours.append(grid[self.row - 1][self.col - 1])
        
        #if self.row < 0 and self.col

    def display_neighbours(self, screen):
        for neighbour in self.neighbours:
            neighbour.change_state('debug1')
            neighbour.draw(screen)