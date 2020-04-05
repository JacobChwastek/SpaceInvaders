import pygame
import random
import math
from player import Player
from bullet import Bullet

# initialize the pygame
myPyGame = pygame.init()
# create a screen
win = pygame.display.set_mode([600, 600])
icon = pygame.image.load("img/rocket.png")
pygame.display.set_icon(icon)

pygame.display.set_caption("Space Invaders")
run = True

# Player
player = Player(278, 530, 0)

# Bullet
bullet = Bullet(0, 530, 'ready', 2)

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Background

background = pygame.image.load("background.jpg")

# Enemy

isDestroyed = []
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("ufo.png"))
    enemyX.append(random.randint(0, 550))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.5)
    enemyY_change.append(20)
    isDestroyed.append(False)
    score = 0


def showScore(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    win.blit(score, (x, y))


def enemy(x, y, i):
    if not isDestroyed[i]:
        win.blit(enemyImg[i], (x, y))


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
    win.blit(player.surf, (int(player.x), int(player.y)))

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

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyY[i] += enemyY_change[i]
            enemyX_change[i] = 0.5
        elif enemyX[i] >= 540:
            enemyY[i] += enemyY_change[i]
            enemyX_change[i] = -0.5
        collision = isCollision(enemyX[i], enemyY[i], bullet.x, bullet.y)
        if collision:
            bullet.y = 530
            bullet.bullet_state = "ready"
            score_value += 1
            isDestroyed[i] = True
            enemyX[i] = 0
            enemyY[i] = 0
        enemy(enemyX[i], enemyY[i], i)

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
