from enemy import Enemy
import pygame
import random


class EnemyController(pygame.sprite.Sprite):
    enemy_list = []

    @staticmethod
    def generate_enemies(num_of_enemies):
        EnemyController.enemy_list.clear()
        y = 1
        x = 0
        for i in range(num_of_enemies):
            if x > 550:
                x = 0
                y += 0.5
            newEnemy = Enemy(x, y * 100, 0.5, 40, False)
            EnemyController.enemy_list.append(newEnemy)
            x += 70
        return EnemyController.enemy_list

    @staticmethod
    def update_enemy_x(i):
        EnemyController.enemy_list[i].x += EnemyController.enemy_list[i].x_change

    @staticmethod
    def updateEnemyXChange(i, value):
        EnemyController.enemy_list[i].x_change = value

    @staticmethod
    def updateEnemyY(i):
        EnemyController.enemy_list[i].y += EnemyController.enemy_list[i].y_change

    @staticmethod
    def refreshEnemyList():
        return EnemyController.enemy_list

    @staticmethod
    def killEnemy(i):
        # enemy = EnemyController.enemy_list[i]
        # enemy.is_destroyed = True
        EnemyController.enemy_list.pop(i)

    @staticmethod
    def displayEnemy(win, i):
        if len(EnemyController.enemy_list) > i:
            enemy = EnemyController.enemy_list[i]
            win.blit(enemy.surf, (enemy.x, enemy.y))


    @staticmethod
    def count_alive_enemies():
        enemies = EnemyController.enemy_list
        aliveEnemies = [enemy for enemy in enemies if enemy.is_destroyed is False]
        return len(aliveEnemies)

    @staticmethod
    def isShooting():
        x = random.randint(1, 1000)
        if x == 1:
            return True
        return False
