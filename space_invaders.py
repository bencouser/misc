import pygame
import random

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
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('001-spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0
speed = 0.3 #rate of change pos

#enemy
enemyImg = pygame.image.load('ufo.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0.3
enemyY_change = 40

#laser
laserImg = pygame.image.load('laser.png')
laserX = 0
laserY = 480
laserX_change = 0
laserY_change = 2
laser_state = "ready" #you cant see the bullet on screan (fire state means its moving)

def fire_laser(x,y):
    global laser_state
    laser_state = "fire"
    screen.blit(laserImg, (x + 16, y + 10))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

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
                playerX_change = -speed
            if event.key == pygame.K_RIGHT:
                playerX_change = speed
            if event.key == pygame.K_SPACE:
                if laser_state == "ready":
                    fire_laser(playerX, laserY)
                    laserX = playerX
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    playerX += playerX_change
    
    #boundries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
    #enemy movement
    enemyX += enemyX_change
    
    #bounds of enemy
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change

    #bullet move
    if laser_state is "fire":
        fire_laser(laserX, laserY)
        laserY -= laserY_change

    if laserY <= 0:
        laserY = 480
        laser_state = "ready"

    enemy(enemyX, enemyY)
    player(playerX, playerY) #player called after screen as player must be on top of screen.
    pygame.display.update()
