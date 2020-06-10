import unittest
import pygame

from bombController import BombController
from enemyController import EnemyController
from images import Images
from colors import Color
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 600
PLAYER_X = 0
PLAYER_Y = 0
WIN = pygame.display.set_mode([DISPLAY_WIDTH, DISPLAY_HEIGHT])
pygame.init()


class BombControllerTest(unittest.TestCase):
    def setUp(self):
        Images.set_up()
        self.bomb_controller = BombController()

    def test_bomb_create(self):
        bomb_x = 100
        bomb_y = 100
        bomb_speed = 10
        self.bomb_controller.create_bomb(bomb_x, bomb_y, bomb_speed)
        self.assertEqual(1, len(self.bomb_controller.bomb_list))


class EnemyControllerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.enemy_controller = EnemyController
        self.number_of_enemies = 3

    def test_generate_enemies(self):
        x = self.number_of_enemies
        self.enemy_controller.generate_enemies(x)
        self.assertEqual(x, self.enemy_controller.count_alive_enemies())

    def test_kill_enemy(self):
        x = self.number_of_enemies
        self.enemy_controller.killEnemy(x - 1)
        self.assertEqual(x - 1, self.enemy_controller.count_alive_enemies())




if __name__ == '__main__':
    unittest.main()
