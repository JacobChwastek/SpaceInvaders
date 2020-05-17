import pygame
import math
from player import Player
from bullet import Bullet
from enemyController import EnemyController
from bombController import BombController

myPyGame = pygame.init()
win = pygame.display.set_mode([600, 600])
icon = pygame.image.load("img/rocket.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Space Invaders")
run = True

# Enemies
num_of_enemies = 6
enemy_list = EnemyController.generateNewEnemies(6)
bombController = BombController

# Player
player = Player(278, 530, 0, win)

# Bullet
bullet = Bullet(0, 530, 'ready', 2)

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Background
background = pygame.image.load("background.jpg")


def showScore(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    win.blit(score, (x, y))


def isCollision(currentEnemyX, currentEnemyY, currentBulletX, currentBulletY):
    distance = math.sqrt((math.pow(currentEnemyX - currentBulletX, 2)) + (math.pow(currentEnemyY - currentBulletY, 2)))
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
    Player.showPlayer(player)

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

    for i in range(num_of_enemies):
        EnemyController.updateEnemyX(i)
        isShooting = EnemyController.isShooting()
        if isShooting:
            bombController.createBomb(enemy_list[i].x, enemy_list[i].y, 1)

        if bombController.isAlive(i):
            bombController.moveBomb(i)
            BombController.displayBomb(win, i)

        if enemy_list[i].x <= 0:
            EnemyController.updateEnemyY(i)
            EnemyController.updateEnemyXChange(i, 0.5)
        elif enemy_list[i].x >= 540:
            EnemyController.updateEnemyY(i)
            EnemyController.updateEnemyXChange(i, -0.5)

        collision = isCollision(enemy_list[i].x, enemy_list[i].y, bullet.x, bullet.y)
        if bombController.isCollision(player.x, player.y, i):
            run = False

        if collision:
            bullet.y = 530
            bullet.bullet_state = "ready"
            score_value += 1
            EnemyController.killEnemy(i)

        enemy_list = EnemyController.refreshEnemyList()
        EnemyController.displayEnemy(win, i)

    # bullet movement
    if bullet.y <= 0:
        bullet.y = 530
        bullet.bullet_state = "ready"

    if bullet.bullet_state == "fire":
        fire_bullet(bullet.x, bullet.y)
        bullet.y -= bullet.bullet_speed
    showScore(textX, textY)

    pygame.display.update()

pygame.quit()
