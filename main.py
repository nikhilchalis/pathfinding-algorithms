# implement here
import pygame as pg
from setup import *
from dijkstra import *

def main():
    pg.init()
    screen = pg.display.set_mode((COLS * GRID_SIZE, ROWS * GRID_SIZE))
    pg.display.set_caption("Pathfinding algorithm visualisations")
    clock = pg.time.Clock()
    screen.fill(BLACK)

    grid = make_grid(barrier_chance=BARRIER_CHANCE)
    display_grid(screen, grid)

    search = False
    start_created = False
    end_created = False
    start = None
    end = None

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    if start_created and end_created and not search:
                        search = True
                        dijkstra(screen, grid, start=start, end=end)
                elif event.key == pg.K_r and start_created and end_created:
                    for row in grid:
                        for node in row:
                            if not node.is_barrier():
                                node.change_state('free')
                                node.distance = float('inf')
                                node.previous = None
                    search = False
                    start_created = False
                    end_created = False
                    start = None
                    end = None
                elif event.key == pg.K_g and not start_created and not end_created:
                    grid = make_grid(barrier_chance=BARRIER_CHANCE)
                    display_grid(screen, grid)


        if pg.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pg.mouse.get_pos()

            row = mouse_y // GRID_SIZE
            col = mouse_x // GRID_SIZE
            if not start_created:
                if grid[col][row].return_state() == 'free' or grid[col][row].return_state() == 'end':
                    grid[col][row].change_state('start')
                    start_created = True
                    start = grid[col][row]
        
        if pg.mouse.get_pressed()[2]:
            mouse_x, mouse_y = pg.mouse.get_pos()

            row = mouse_y // GRID_SIZE
            col = mouse_x // GRID_SIZE
            if not end_created:
                if grid[col][row].return_state() == 'free' or grid[col][row].return_state() == 'start':
                    grid[col][row].change_state('end')
                    end_created = True
                    end = grid[col][row]
         

        screen.fill(BLACK)
        #clock.tick(FPS)
        display_grid(screen, grid)
        pg.display.update()
        
        

if __name__=="__main__":
    main()