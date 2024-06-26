import pygame as pg
import random

### CONSTANTS ####

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_RED = (150, 20, 20)
GREEN = (0, 255, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)
LIGHT_GREY = (211, 211, 211)
DARK_GREEN = (1, 50, 32)
LIGHT_GREEN = (144, 238, 144)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)

# Display constants
GRID_SIZE = 20
NODE_SIZE = 19
ROWS = 60
COLS = 60
FPS = 60
BARRIER_CHANCE = 0.3

# section sizes
EXTRA_WIDTH_PX = 200
WIDTH_OFFSET_PX = 50
HEIGHT_OFFSET_PX = 50
PADDING_PX = 40
BUTTON_PADDING = 40
ACTUAL_WIDTH = COLS * GRID_SIZE + 2*WIDTH_OFFSET_PX + EXTRA_WIDTH_PX + PADDING_PX
ACTUAL_HEIGHT = ROWS * GRID_SIZE + 2*HEIGHT_OFFSET_PX
GRID_ACTUAL_WIDTH = COLS * GRID_SIZE
GRID_ACTUAL_HEIGHT = ROWS * GRID_SIZE

# Button constants
BUTTON_HEIGHT = 60
BUTTON_WIDTH = EXTRA_WIDTH_PX
BUTTON_X = ACTUAL_WIDTH - (EXTRA_WIDTH_PX + PADDING_PX)
FIRST_BUTTON_Y = HEIGHT_OFFSET_PX
SECOND_BUTTON_Y = FIRST_BUTTON_Y + BUTTON_HEIGHT + BUTTON_PADDING
THIRD_BUTTON_Y = SECOND_BUTTON_Y + BUTTON_HEIGHT + BUTTON_PADDING

EXIT_BUTTON_Y = ACTUAL_HEIGHT - HEIGHT_OFFSET_PX - BUTTON_HEIGHT
REGEN_BUTTON_Y = EXIT_BUTTON_Y - BUTTON_HEIGHT - BUTTON_PADDING
RESET_BUTTON_Y = REGEN_BUTTON_Y - BUTTON_HEIGHT - BUTTON_PADDING
# states
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
        self.x = row * GRID_SIZE + WIDTH_OFFSET_PX
        self.y = col * GRID_SIZE + HEIGHT_OFFSET_PX
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