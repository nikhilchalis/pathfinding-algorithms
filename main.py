# implement here
import pygame as pg
from setup import *

def main():
    pg.init()
    screen = pg.display.set_mode((COLS * GRID_SIZE, ROWS * GRID_SIZE))
    pg.display.set_caption("Pathfinding algorithm visualisations")
    clock = pg.time.Clock()
    screen.fill(BLACK)

    grid = make_grid()
    display_grid(screen, grid)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        if pg.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pg.mouse.get_pos()

            row = mouse_y // GRID_SIZE
            col = mouse_x // GRID_SIZE

            if grid[col][row].return_state() == 'free' or grid[col][row].return_state() == 'start':
                grid[col][row].change_state('end')
        
        if pg.mouse.get_pressed()[2]:
            mouse_x, mouse_y = pg.mouse.get_pos()

            row = mouse_y // GRID_SIZE
            col = mouse_x // GRID_SIZE

            if grid[col][row].return_state() == 'free' or grid[col][row].return_state() == 'end':
                grid[col][row].change_state('start')
        
        screen.fill(BLACK)
        clock.tick(FPS)
        display_grid(screen, grid)
        pg.display.update()
        
        

if __name__=="__main__":
    main()