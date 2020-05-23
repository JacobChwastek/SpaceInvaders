import math
import pygame
from player import Player
from bullet import Bullet
from enemyController import EnemyController
from bombController import BombController
from level import Level


def game():

    game_level = Level()
    win = pygame.display.set_mode([600, 600])
    icon = pygame.image.load("img/rocket.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Space Invaders")
    run = True

    # Enemies
    enemy_list = EnemyController.generate_enemies(3)
    bombController = BombController

    # Player
    player = Player(278, 530, 0, win)

    # Bullet
    bullet = Bullet(0, 530, 'ready', 2)

    # Score
    score_value = 0
    font = pygame.font.Font('freesansbold.ttf', 32)
    text_x = 10
    text_y = 10

    background = pygame.image.load("background.jpg")

    def show_score(x, y):
        score = font.render("Score: {}".format(score_value), True, (255, 255, 255))
        win.blit(score, (x, y))

    def show_level(x, y):
        level = font.render("Level: {}".format(game_level.level), True, (255, 255, 255))
        win.blit(level, (x, y))

    def is_colliding(current_enemy_x, current_enemy_y, current_bullet_x, current_bullet_y):
        distance = math.sqrt(
            (math.pow(current_enemy_x - current_bullet_x, 2))
            + (math.pow(current_enemy_y - current_bullet_y, 2)))
        if distance < 27:
            return True
        return False

    def fire_bullet(x, y):
        bullet.bullet_state = "fire"
        win.blit(bullet.surf, (int(x + 16), int(y + 16)))

    # game loop
    while run:

        win.fill((0, 0, 0))
        win.blit(background, (0, 0))
        Player.show_player(player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.player_speed = -0.7
                if event.key == pygame.K_RIGHT:
                    player.player_speed = 0.7
                if event.key == pygame.K_SPACE:
                    if bullet.bullet_state == "ready":
                        bullet.x = player.x
                        fire_bullet(bullet.x, bullet.y)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.player_speed = 0

        player.x += player.player_speed
        if player.x <= 0:
            player.x = 0
        elif player.x >= 540:
            player.x = 540

        # enemies

        for i, enemy in enumerate(enemy_list):

            EnemyController.update_enemy_x(i)
            isShooting = EnemyController.is_shooting()
            if isShooting:
                bombController.create_bomb(enemy.x, enemy.y, 1 + game_level.level * 0.25)

            if bombController.is_alive(i):
                bombController.move_bomb(i)
                bombController.display_bomb(win, i)

            if enemy.x <= 0:
                EnemyController.update_enemy_y(i)
                EnemyController.update_enemy_x_change(i, 0.5)
            elif enemy.x >= 540:
                EnemyController.update_enemy_y(i)
                EnemyController.update_enemy_x_change(i, -0.5)

            collision = is_colliding(enemy.x, enemy.y, bullet.x, bullet.y)
            if bombController.is_collision(player.x, player.y, i):
                run = False

            if collision:
                bullet.y = 530
                bullet.bullet_state = "ready"
                score_value += 1 * game_level.level
                EnemyController.killEnemy(i)

            enemy_list = EnemyController.refresh_enemy_list()
            EnemyController.displayEnemy(win, i)

        if bullet.y <= 0:
            bullet.y = 530
            bullet.bullet_state = "ready"

        if bullet.bullet_state == "fire":
            fire_bullet(bullet.x, bullet.y)
            bullet.y -= bullet.bullet_speed
        show_score(text_x, text_y)
        show_level(text_x, text_y + 40)

        if EnemyController.count_alive_enemies() == 0:
            game_level.level += 1
            enemy_list = EnemyController.generate_enemies(3 + game_level.level)

        pygame.display.update()

    pygame.quit()
