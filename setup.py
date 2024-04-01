import pygame as pg
import random
from node import *


def make_grid(barrier_chance=0.25):
    grid = []
    for i in range(COLS):
        grid.append([])
        for j in range(ROWS):
            if (i+j)%2 == 1:
                grid[i].append(None)
            else:
                if i % 2 == 0:
                    node = Node(i, j, offset=False)
                else:
                    node = Node(i, j, offset=True)
                
                # randomly assigning barrier
                random_number = random.random()
                if random_number < barrier_chance:
                    node.change_state('barrier')

                grid[i].append(node)
    
    return grid
    

def display_grid(screen, grid):
    for row in grid:
        for node in row:
            if node is not None:
                node.draw(screen)
    
    pg.display.update()