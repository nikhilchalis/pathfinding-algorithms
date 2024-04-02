import pygame as pg
import random
from node import *


def make_grid(barrier_chance=0.25):
    grid = []
    for i in range(COLS):
        grid.append([])
        for j in range(ROWS):
            if (i+j)%2 == 1:
                node = Node(i, j, state='none')
                grid[i].append(node)
            else:
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
            if node.state != 'none':
                node.draw(screen)
    
    pg.display.update()