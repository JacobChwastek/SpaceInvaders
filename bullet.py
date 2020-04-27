import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x=None, y=None, bullet_state=None, bullet_speed=None):

        super(Bullet, self).__init__()
        
        self.x = x
        self.y = y
        self.bullet_speed = bullet_speed
        self.surf = pygame.image.load('img/bullet.png').convert()
        self.surf.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        self.bullet_state = bullet_state
        self.rect = self.surf.get_rect()

    def renderBullet(self):
        self.win.blit(self.surf, (int(self.x), int(self.y)))
