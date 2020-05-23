import pygame
from menu import Menu
from game import game

DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 600


def main():
    pygame.init()
    win = pygame.display.set_mode([DISPLAY_WIDTH, DISPLAY_HEIGHT])
    pygame.display.set_caption("Space Invaders")
    background = pygame.image.load("background.jpg")
    run = True
    menu = Menu(win)

    while run:

        pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if menu.game_state == 'menu':
            win.fill((0, 0, 0))
            win.blit(background, (0, 0))
            menu.display()
            pygame.display.update()
        elif menu.game_state == 'game':
            game()
            pygame.display.update()
        elif menu.game_state == 'exit':
            run = False
            pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
