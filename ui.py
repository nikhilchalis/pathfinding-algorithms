import pygame as pg
from setup import *

pg.font.init()
font = pg.font.Font("fonts\Outfit-Regular.ttf", 32)

class Button:
    def __init__(self, x, y, width, height, text, colour):
        self.rect = pg.Rect(x, y, width, height)
        self.text = text
        self.colour = colour

    def draw(self, screen):
        pg.draw.rect(screen, self.colour, self.rect)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def is_clicked(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:  # Check if left mouse button is pressed
                pos = pg.mouse.get_pos()
                if self.rect.collidepoint(pos):
                    self.clicked = True
        elif event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:  # Check if left mouse button is released
                self.clicked = False
                pos = pg.mouse.get_pos()
                if self.rect.collidepoint(pos):
                    return True  # Return True only if the button was clicked


def display_buttons(screen, buttons_list: list[Button]) -> None:
    for button in buttons_list:
        button.draw(screen)

    pg.display.update()

'''
# Text input class
class TextInput:
    def __init__(self, x, y, width, height):
        self.rect = pg.Rect(x, y, width, height)
        self.text = ''
        self.active = False

    def draw(self, surface):
        pg.draw.rect(surface, GREY if self.active else WHITE, self.rect)
        text_surface = font.render(self.text, True, BLACK)
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicks on the text input rect, activate it
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        elif event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)  # You can process the input here
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
'''