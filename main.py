import pygame
import random
import math
from player import Player

# initialize the pygame
myPyGame = pygame.init()
# create a screen
win = pygame.display.set_mode([600, 600])
icon = pygame.image.load("img/rocket.png")
pygame.display.set_icon(icon)

pygame.display.set_caption("Space Invaders")
run = True

# Player
classPlayer = Player()
playerImg = pygame.image.load("img/bullet.png")
playerX = 278
playerY = 530
playerX_change = 0

# Bullet

bulletImg = pygame.image.load("bullet.png")
bulletY = 530
bulletX = 0
bullet_state = "ready"
bulletY_change = 2

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Background

background = pygame.image.load("background.jpg")

# Enemy

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
    score = 0


def showScore(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    win.blit(score, (x, y))


def player(x, y):
    win.blit(playerImg, (x, y))


def enemy(x, y, i):
    win.blit(enemyImg[i], (x, y))


def isCollision(currentEnemyX, currentEnemyY, currentBulletX, currentBulletY):
    distance = math.sqrt((math.pow(currentEnemyX - currentBulletX, 2)) + (math.pow(currentEnemyY - currentBulletY, 2)))
    if distance < 27:
        return True
    return False


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    win.blit(bulletImg, (int(x + 16), int(y + 16)))


# game loop
while run:
    win.fill((0, 0, 0))
    win.blit(background, (0, 0))
    win.blit(classPlayer.surf, (playerX, playerY))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.7
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.7
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 540:
        playerX = 540

    # enemies

    for i in range(num_of_enemies):

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyY[i] += enemyY_change[i]
            enemyX_change[i] = 0.5
        elif enemyX[i] >= 540:
            enemyY[i] += enemyY_change[i]
            enemyX_change[i] = -0.5
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 530
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 550)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 530
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    showScore(textX, textY)
    pygame.display.update()

pygame.quit()
