# implement here
import pygame as pg
from setup import *
from dijkstra import *
from astar import *
from ui import *

def main():
    pg.init()
    screen = pg.display.set_mode((ACTUAL_WIDTH, ACTUAL_HEIGHT))
    pg.display.set_caption("Pathfinding algorithm visualisations")
    clock = pg.time.Clock()
    screen.fill(BACKGROUND)

    grid = make_grid(barrier_chance=BARRIER_CHANCE)
    display_grid(screen, grid)

    start_button = Button(BUTTON_X, FIRST_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT, "Find Path", PATH)
    reset_button = Button(BUTTON_X, RESET_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT, "Reset", GREY)
    regen_button = Button(BUTTON_X, REGEN_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT, "Regen", GREY)
    exit_button = Button(BUTTON_X, EXIT_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT, "EXIT", LIGHT_RED)
    toggle_button = Button(BUTTON_X, TOGGLE_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT, "Toggle", LIGHT_GREY)

    buttons = [reset_button, regen_button, start_button, exit_button, toggle_button]

    search = False
    start_created = False
    end_created = False
    start = None
    end = None
    use_dijkstra = False

    display_buttons(screen, buttons_list=buttons)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif toggle_button.is_clicked(event):
                use_dijkstra = not use_dijkstra 
            elif reset_button.is_clicked(event):
                    for row in grid:
                        for node in row:
                            if not node.is_barrier() and not node.is_none():
                                node.change_state('free')
                                node.distance = float('inf')
                                node.previous = None

                    search = False
                    start_created = False
                    end_created = False
                    start = None
                    end = None
            elif regen_button.is_clicked(event) and not start_created and not end_created:
                grid = make_grid(barrier_chance=BARRIER_CHANCE)
            elif start_button.is_clicked(event) and start_created and end_created and not search:
                search = True
                if use_dijkstra:
                    dijkstra(screen, grid, start=start, end=end)
                else:
                    path = astar(screen, grid, start=start, end=end, search_aggression=3)
                    if len(path) == 0:
                        print('no path found')
                    else:
                        for node in path[1:]:
                            node.change_state('path')
                            node.draw(screen)
 
            elif exit_button.is_clicked(event): 
                running=False

            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = pg.mouse.get_pos()
                    if mouse_x > WIDTH_OFFSET_PX and mouse_x < (WIDTH_OFFSET_PX + GRID_ACTUAL_WIDTH) and mouse_y > HEIGHT_OFFSET_PX and mouse_y < (HEIGHT_OFFSET_PX + GRID_ACTUAL_HEIGHT):
                        row = int((mouse_y - HEIGHT_OFFSET_PX) // (GRID_SIZE* np.sqrt(3)))
                        col = int((mouse_x - WIDTH_OFFSET_PX) // (GRID_SIZE))
                        if not start_created:
                            if grid[col][row].return_state() == 'free' or grid[col][row].return_state() == 'end':
                                grid[col][row].change_state('start')
                                start_created = True
                                start = grid[col][row]
                                #start.update_neighbours(grid)
                                #start.display_neighbours(screen)

                
                if event.button == 3:
                    if mouse_x > WIDTH_OFFSET_PX and mouse_x < (WIDTH_OFFSET_PX + GRID_ACTUAL_WIDTH) and mouse_y > HEIGHT_OFFSET_PX and mouse_y < (HEIGHT_OFFSET_PX + GRID_ACTUAL_HEIGHT):
                        mouse_x, mouse_y = pg.mouse.get_pos()
                        row = int((mouse_y - HEIGHT_OFFSET_PX) // (GRID_SIZE* np.sqrt(3)))
                        col = int((mouse_x - WIDTH_OFFSET_PX) // (GRID_SIZE))
                        if not end_created:
                            if grid[col][row].return_state() == 'free' or grid[col][row].return_state() == 'start':
                                grid[col][row].change_state('end')
                                end_created = True
                                end = grid[col][row]


        #screen.fill(BACKGROUND)
        #clock.tick(FPS)
        display_grid(screen, grid)
        display_buttons(screen, buttons_list=buttons)
        


if __name__ == "__main__":
    main()