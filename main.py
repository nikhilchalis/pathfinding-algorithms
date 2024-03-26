# implement here
import pygame as pg
import random
from setup import *

def main():
    pg.init()
    screen = pg.display.set_mode((COLS * GRID_SIZE, ROWS * GRID_SIZE))
    pg.display.set_caption("Pathfinding algorithm visualisations")
    clock = pg.time.Clock()

    screen.fill(BLACK)

    grid = make_grid()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        screen.fill(BLACK)
        clock.tick(FPS)
        display_grid(screen, grid)
        pg.display.update()
        

if __name__=="__main__":
    main()