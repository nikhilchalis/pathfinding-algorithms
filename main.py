# implement here
import pygame as pg

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GREY = (128, 128, 128)

HEIGHT = 800
WIDTH = 1200
FPS = 25



def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Pathfinding algorithm visualisations")
    clock = pg.time.Clock()

    screen.fill(BLACK)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        clock.tick(FPS)
        pg.display.flip()
        screen.fill(BLACK)

if __name__=="__main__":
    main()