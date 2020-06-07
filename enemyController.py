from enemy import Enemy
import random


class EnemyController:

    enemy_list = []

    def __init__(self, screen_width):
        self.screen_width = screen_width

    def generate_enemies(self, num_of_enemies):
        self.enemy_list.clear()
        y = 1
        x = 0
        for i in range(num_of_enemies):
            if x > self.screen_width:
                x = 0
                y += 0.5
            newEnemy = Enemy(x, y * 100, 0.5, 40, False)
            self.enemy_list.append(newEnemy)
            x += 70
        return self.enemy_list

    def update_enemy_x(self, i):
        self.enemy_list[i].x += self.enemy_list[i].x_change

    def update_enemy_x_change(self, i, value):
        self.enemy_list[i].x_change = value

    def update_enemy_y(self, i):
        self.enemy_list[i].y += self.enemy_list[i].y_change

    def refresh_enemy_list(self):
        return self.enemy_list

    def killEnemy(self, i):
        self.enemy_list.pop(i)

    def displayEnemy(self, win, i):
        if len(self.enemy_list) > i:
            enemy = self.enemy_list[i]
            win.blit(enemy.surf, (enemy.x, enemy.y))

    def count_alive_enemies(self):
        enemies = self.enemy_list
        aliveEnemies = [enemy for enemy in enemies if enemy.is_destroyed is False]
        return len(aliveEnemies)

    def is_shooting(self, level):
        x = random.randint(1, (1000 - level * 10))
        if x == 1:
            return True
        return False
