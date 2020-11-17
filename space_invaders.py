import pygame

#initilize the pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((800,600)) #((width,height))

# make a fullscreen:
#screen = pygame.display.set_mode((0,0))
#print('height: %s' % screen.get_height())
#print('width: %s' % screen.get_width())


#Title & Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('001-spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0
rate = 0.3 #rate of change pos


def player(x, y):
    screen.blit(playerImg, (x, y))


# the game loop (keeps window open until we quit) 
running = True
while running:
     
    screen.fill((0,0,0)) #((R,G,B))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # if keystroke is pressed check whethere right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -rate
            if event.key == pygame.K_RIGHT:
                playerX_change = rate
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    player(playerX, playerY) #player called after screen as player must be on top of screen.
    pygame.display.update()
