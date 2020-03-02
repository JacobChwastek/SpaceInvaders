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
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
pygame.quit()
