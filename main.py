import pygame
from menu import Menu
from button import *

myPyGame = pygame.init()
display_width = 600
display_height = 600

win = pygame.display.set_mode([display_width, display_height])
pygame.display.set_caption("Space Invaders")
background = pygame.image.load("background.jpg")
run = True
game_state = "menu"
menu = Menu(game_state, win)




while run:
    win.fill((0, 0, 0))
    win.blit(background, (0, 0))
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if menu.game_state == 'menu':
        menu.display()
    elif menu.game_state == 'game':
        from game import *
    elif menu.game_state == 'exit':
        run = False

    pygame.display.update()

pygame.quit()
