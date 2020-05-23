from bomb import Bomb
import math
import pygame


class BombController(pygame.sprite.Sprite):
    bomb_list = []

    @staticmethod
    def create_bomb(x, y, speed):
        newBomb = Bomb(x, y, True, speed)
        BombController.bomb_list.append(newBomb)

    @staticmethod
    def move_bomb(i):
        if BombController.bomb_list[i].y > 600:
            BombController.bomb_list.pop(i)
        else:
            BombController.bomb_list[i].y += BombController.bomb_list[i].bomb_speed

    @staticmethod
    def is_alive(i):
        if i >= len(BombController.bomb_list):
            return False
        return True

    @staticmethod
    def display_bomb(win, i):
        if i < len(BombController.bomb_list):
            bomb = BombController.bomb_list[i]
            if bomb.bomb_state:
                win.blit(bomb.surf, (bomb.x, bomb.y))

    @staticmethod
    def is_collision(playerX, playerY, i):
        if i < len(BombController.bomb_list):
            bomb = BombController.bomb_list[i]
            distanceX = math.fabs(bomb.x - playerX)
            distanceY = math.fabs(bomb.y - playerY)

            if distanceX < 20 and distanceY < 33:
                return True

        return False
