import pygame as pg
import random
from node import *


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