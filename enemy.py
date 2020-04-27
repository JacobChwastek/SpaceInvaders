import random

import pygame


class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y, x_change, y_change, is_destroyed):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load('ufo.png')
        self.x = x
        self.y = y
        self.x_change = x_change
        self.y_change = y_change
        self.is_destroyed = is_destroyed



