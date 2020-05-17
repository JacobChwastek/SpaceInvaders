import pygame
from colors import Color


def button(msg, x, y, w, h, color, on_hover_color, win, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(win, on_hover_color, (x, y, w, h))

        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(win, color, (x, y, w, h))

    font = pygame.font.Font("freesansbold.ttf", 32)
    text_button = font.render(msg, True, Color.Black())
    win.blit(text_button, (x + 50, y + 10))
