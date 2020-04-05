import pygame


class Score(pygame.sprite.Sprite):

    def __init__(self, x, y, player_speed=None):
        super(Score, self).__init__()

        self.x = x
        self.y = y
        self.player_speed = player_speed
        self.surf = pygame.image.load('./img/rocket.png').convert()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()

