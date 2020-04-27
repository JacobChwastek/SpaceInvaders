from bomb import Bomb
import pygame

class BombController(pygame.sprite.Sprite):
    bomb_list = []

    def createBomb(x,y,speed):
       newBomb = Bomb(x,y,True,speed)
       BombController.bomb_list.append(newBomb)

    def moveBomb(i):
        BombController.bomb_list[i].y += BombController.bomb_list[i].bomb_speed


    def isAlive(i):
        if i >= len(BombController.bomb_list):
            return False
        return True
    def displayBomb(win, i):
        bomb = BombController.bomb_list[i]
        if bomb.bomb_state:
            win.blit(bomb.surf, (bomb.x, bomb.y))
