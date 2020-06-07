import pygame
from colors import Color
from images import Images


def button(msg, x, y, w, h, color, on_hover_color, win, action=None):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse_x > x and y + h > mouse_y > y:
        pygame.draw.rect(win, on_hover_color, (x, y, w, h))

        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(win, color, (x, y, w, h))

    text_button = Images.FONT.render(msg, True, Color.BLACK)
    win.blit(text_button, (x + 50, y + 10))
