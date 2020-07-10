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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            print("A keystroke is pressed")
            if event.key == pygame.K_LEFT:
                print("Left arrow is pressed")
            if event.type == pygame.K_RIGHT:
                print("Right arrow is pressed")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("keystroke has been released")
    

    player(playerX,playerY)
    pygame.display.update()