import pygame
from ship import Ship

# 2 tutorial
myPyGame = pygame.init()
win = pygame.display.set_mode([600, 600])
pygame.display.set_caption("My first game")

screenWidth = 600
screenHeight = 600
width = 40
height = 60
vel = 20
run = True
y = screenHeight - height
x = int(screenWidth / 2)
missleX = x
missleY = y
shot = False

while run:

    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screenWidth - width:
        x += vel

    win.fill((0, 0, 0))

    pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))

    # pocisk
    if keys[pygame.K_SPACE]:
        shot = True
    if shot:
        missleY -= vel
        pygame.draw.rect(win, (225, 0, 0), (missleX + width / 2, missleY, 10, 10))

    if missleY < 0:
        shot = False
        missleY = y
    print(missleY)

    # update
    pygame.display.update()
pygame.quit()
