import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('img/spaceship.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('img/player.png')
playerX = 370
playerY = 480
playerX_change = 0

enemyImg = pygame.image.load('img/alien.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0.3
enemyY_change = 40

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    playerX += playerX_change

    if playerX <= 0 :
        playerX = 0
    elif playerX >= 736 :
        playerX = 736

    enemyX += enemyX_change

    if enemyX <= 0 :
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736 :
        enemyX_change = -0.3
        enemyY += enemyY_change


    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()