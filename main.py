import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('img/spaceship.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('img/player.png')
playerX = 370
playerY = 520

def player(x,y):
    screen.blit(playerImg,(x,y))

running = True
while running:

    screen.fill((0, 0, 0))
    playerX += 0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

    player(playerX,playerY)
    pygame.display.update()