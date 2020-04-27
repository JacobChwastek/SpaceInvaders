import pygame


class Bomb(pygame.sprite.Sprite):

    def __init__(self, x=None, y=None, bomb_state=None, bomb_speed=None):
        super(Bomb, self).__init__()

        self.x = x
        self.y = y
        self.bomb_speed = bomb_speed
        self.surf = pygame.image.load('img/bomb.png')
        self.surf.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        self.bomb_state = bomb_state
        self.rect = self.surf.get_rect()
