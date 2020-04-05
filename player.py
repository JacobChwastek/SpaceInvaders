import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):

        super(Player, self).__init__()

        self.surf = pygame.image.load("rocket.png").convert()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)

        self.rect = self.surf.get_rect()