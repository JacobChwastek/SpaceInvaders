import pygame


class Images:

    @staticmethod
    def set_up():
        Images.BOMB = pygame.image.load('img/bomb.png')
        Images.FONT = pygame.font.Font("freesansbold.ttf", 32)
        Images.BULLET = pygame.image.load('img/bullet.png').convert()
        Images.UFO = pygame.image.load('img/ufo.png')
        Images.ROCKET = pygame.image.load("img/rocket.png")
        Images.BACKGROUND = pygame.image.load("img/background.jpg")