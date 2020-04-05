import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self):

        super(Bullet, self).__init__()

        self.surf = pygame.image.load('img/bullet.png').convert()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)

        self.rect = self.surf.get_rect()