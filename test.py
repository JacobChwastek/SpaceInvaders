import unittest
import pygame

from bombController import BombController
from enemyController import EnemyController
from images import Images
from player import Player
from colors import Color


class BombControllerTest(unittest.TestCase):
    def setUp(self):
        pygame.init()
        pygame.display.set_mode([1, 1])
        Images.set_up()
        self.bomb_controller = BombController()

    def test_bomb_create(self):
        bomb_x = 100
        bomb_y = 100
        bomb_speed = 700
        self.bomb_controller.bomb_list.clear()
        self.bomb_controller.create_bomb(bomb_x, bomb_y, bomb_speed)
        self.assertEqual(1, len(self.bomb_controller.bomb_list))

    def test_move_bomb_off_screen(self):

        amount_of_bombs = len(self.bomb_controller.bomb_list)
        self.bomb_controller.create_bomb(550, 550, 60)
        self.bomb_controller.move_bomb(0)
        amount_of_bombs_after = len(self.bomb_controller.bomb_list)

        self.assertEqual(amount_of_bombs, amount_of_bombs_after - 1)

    def test_move_bomb(self):
        bomb_y = 100
        bomb_x = 100
        move_distance = 60
        self.bomb_controller.bomb_list.clear()

        self.bomb_controller.create_bomb(bomb_x, bomb_y, move_distance)
        self.bomb_controller.move_bomb(0)

        bomb_y_after_move = self.bomb_controller.bomb_list[0].y
        bomb_x_after_move = self.bomb_controller.bomb_list[0].x

        self.assertEqual(bomb_x, bomb_x_after_move)
        self.assertEqual(bomb_y + move_distance, bomb_y_after_move)


class CollisionTest(unittest.TestCase):
    def setUp(self) -> None:
        pygame.init()
        pygame.display.set_mode([1, 1])
        Images.set_up()
        self.bomb_controller = BombController()

    def test_collision_same_coordinates(self):
        x_pos = 100
        y_pos = 100
        self.bomb_controller.bomb_list.clear()
        self.bomb_controller.create_bomb(x_pos, y_pos, 10)
        self.player = Player(x_pos, y_pos, 10)
        is_collision = self.bomb_controller.is_collision(self.player.x, self.player.y, 0)

        self.assertTrue(is_collision)

    def test_collision_x_10_diff_y_10_diff(self):
        x_pos = 100
        y_pos = 100
        self.bomb_controller.bomb_list.clear()
        self.bomb_controller.create_bomb(x_pos + 10, y_pos + 10, 10)
        self.player = Player(x_pos, y_pos, 10)
        is_collision = self.bomb_controller.is_collision(self.player.x, self.player.y, 0)
        self.assertTrue(is_collision)

    def test_collision_x_40_diff_y_10_diff(self):
        x_pos = 100
        y_pos = 100
        self.bomb_controller.bomb_list.clear()
        self.bomb_controller.create_bomb(x_pos + 40, y_pos + 10, 10)
        self.player = Player(x_pos, y_pos, 10)
        is_collision = self.bomb_controller.is_collision(self.player.x, self.player.y, 0)
        self.assertFalse(is_collision)


class EnemyControllerTest(unittest.TestCase):
    def setUp(self) -> None:
        pygame.init()
        pygame.display.set_mode([1, 1])
        Images.set_up()
        self.enemy_controller = EnemyController(600)
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
