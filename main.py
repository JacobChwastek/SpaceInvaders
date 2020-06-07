import pygame
import math
import pygame

from player import Player
from bullet import Bullet
from enemyController import EnemyController
from bombController import BombController
from level import Level
from colors import Color
from menu import Menu
from images import Images

DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 600
WIN = pygame.display.set_mode([DISPLAY_WIDTH, DISPLAY_HEIGHT])
menu = Menu(WIN)


def main():
    pygame.init()
    pygame.display.set_caption("Space Invaders")
    Images.set_up()

    background = Images.BACKGROUND
    run = True

    while run:

        pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if menu.game_state == 'menu':
            WIN.fill((0, 0, 0))
            WIN.blit(background, (0, 0))
            menu.display()
            pygame.display.update()
        elif menu.game_state == 'game':
            game()
            pygame.display.update()
        elif menu.game_state == 'exit':
            run = False
            pygame.display.update()

    pygame.quit()


def game():
    run = True
    game_level = Level()
    icon = Images.ROCKET
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Space Invaders")
    enemyController = EnemyController(550)
    enemy_list = enemyController.generate_enemies(3)
    bombController = BombController()

    # Player
    player = Player(278, 530, 0, WIN)

    # Bullet
    bullet = Bullet(0, 530, 'ready', 2)

    # Score
    score_value = 0
    font = Images.FONT
    text_x = 10
    text_y = 10

    background = background = Images.BACKGROUND

    def show_score(x, y):
        score = font.render(f"Score: {score_value}", True, Color.WHITE)
        WIN.blit(score, (x, y))

    def show_level(x, y):
        level = font.render(f"Level: {game_level.level}", True, Color.WHITE)
        WIN.blit(level, (x, y))

    def is_colliding(current_enemy_x, current_enemy_y, current_bullet_x, current_bullet_y):
        distance = math.sqrt(
            (math.pow(current_enemy_x - current_bullet_x, 2))
            + (math.pow(current_enemy_y - current_bullet_y, 2)))
        if distance < 27:
            return True
        return False

    def fire_bullet(x, y):
        bullet.bullet_state = "fire"
        WIN.blit(bullet.surf, (int(x + 16), int(y + 16)))

    # game loop
    while run:

        WIN.fill((0, 0, 0))
        WIN.blit(background, (0, 0))
        Player.show_player(player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                menu.game_state = "menu"

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

            enemyController.update_enemy_x(i)
            isShooting = enemyController.is_shooting(game_level.level)
            if isShooting:
                bombController.create_bomb(enemy.x, enemy.y, 1 + game_level.level * 0.25)

            if bombController.is_alive(i):
                bombController.move_bomb(i)
                bombController.display_bomb(WIN, i)

            if enemy.x <= 0:
                enemyController.update_enemy_y(i)
                enemyController.update_enemy_x_change(i, 0.5)
            elif enemy.x >= 540:
                enemyController.update_enemy_y(i)
                enemyController.update_enemy_x_change(i, -0.5)

            collision = is_colliding(enemy.x, enemy.y, bullet.x, bullet.y)
            if bombController.is_collision(player.x, player.y, i):
                run = False

            if collision:
                bullet.y = 530
                bullet.bullet_state = "ready"
                score_value += 1 * game_level.level
                enemyController.killEnemy(i)

            enemy_list = enemyController.refresh_enemy_list()
            enemyController.displayEnemy(WIN, i)

        if bullet.y <= 0:
            bullet.y = 530
            bullet.bullet_state = "ready"

        if bullet.bullet_state == "fire":
            fire_bullet(bullet.x, bullet.y)
            bullet.y -= bullet.bullet_speed
        show_score(text_x, text_y)
        show_level(text_x, text_y + 40)

        if enemyController.count_alive_enemies() == 0:
            game_level.level += 1
            enemy_list = enemyController.generate_enemies(3 + game_level.level)

        pygame.display.update()

    menu.game_state = "menu"


if __name__ == '__main__':
    main()
