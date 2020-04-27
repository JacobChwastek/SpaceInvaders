from enemy import Enemy
import pygame


class EnemyController(pygame.sprite.Sprite):
    enemy_list = []

    @staticmethod
    def generateNewEnemies(num_of_enemies):
        for i in range(num_of_enemies):
            newEnemy = Enemy(i * 70, 100, 0.5, 40, False)
            EnemyController.enemy_list.append(newEnemy)

        return EnemyController.enemy_list

    @staticmethod
    def updateEnemyX(i):
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
        enemy = EnemyController.enemy_list[i]
        enemy.is_destroyed = True

    @staticmethod
    def displayEnemy(win,i):
        enemy = EnemyController.enemy_list[i]
        if not enemy.is_destroyed:
            win.blit(enemy.surf, (enemy.x, enemy.y))

    @staticmethod
    def countAliveEnemies():
        enemies = EnemyController.enemy_list
        aliveEnemies = [enemy for enemy in enemies if enemy.is_destroyed is False]
        return len(aliveEnemies)