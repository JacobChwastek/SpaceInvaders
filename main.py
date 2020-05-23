import pygame
from menu import Menu

myPyGame = pygame.init()
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 600

win = pygame.display.set_mode([DISPLAY_WIDTH, DISPLAY_HEIGHT])
pygame.display.set_caption("Space Invaders")
background = pygame.image.load("background.jpg")
RUN = True
menu = Menu("menu", win)

while RUN:
    win.fill((0, 0, 0))
    win.blit(background, (0, 0))
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    if menu.game_state == 'menu':
        menu.display()
        pygame.display.update()
    elif menu.game_state == 'game':
        from game import *
    elif menu.game_state == 'exit':
        RUN = False
        pygame.display.update()



pygame.quit()
