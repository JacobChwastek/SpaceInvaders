from bomb import Bomb
import math
import pygame


class BombController(pygame.sprite.Sprite):
    bomb_list = []

    @staticmethod
    def createBomb(x, y, speed):
        newBomb = Bomb(x, y, True, speed)
        BombController.bomb_list.append(newBomb)

    @staticmethod
    def moveBomb(i):
        BombController.bomb_list[i].y += BombController.bomb_list[i].bomb_speed

    @staticmethod
    def isAlive(i):
        if i >= len(BombController.bomb_list):
            return False
        return True

    @staticmethod
    def displayBomb(win, i):
        bomb = BombController.bomb_list[i]
        if bomb.bomb_state:
            win.blit(bomb.surf, (bomb.x, bomb.y))

    @staticmethod
    def isCollision(playerX, playerY, i):
        if i < len(BombController.bomb_list):
            bomb = BombController.bomb_list[i]
            distanceX = math.fabs(bomb.x - playerX)
            distanceY = math.fabs(bomb.y - playerY)

            if distanceX < 20 and distanceY < 33:
                print(distanceY)
                print(distanceX)
                return True

        return False
