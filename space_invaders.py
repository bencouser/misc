import pygame
import math
import random
from pygame import mixer

#initilize the pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((800,600)) #((width,height))

mixer.music.load('background.wav')
mixer.music.play(-1)

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
speed = 0.5 #rate of change pos

#enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint(100,700))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

#laser
laserImg = pygame.image.load('laser.png')
laserX = 0
laserY = 480
laserX_change = 0
laserY_change = 2
laser_state = "ready" #you cant see the bullet on screan (fire state means its moving)

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

#game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

textX = 10
textY = 10

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("Game Over", True, (255,255,255))
    screen.blit(over_text, (200, 250))


def fire_laser(x,y):
    global laser_state
    laser_state = "fire"
    screen.blit(laserImg, (x + 16, y + 10))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def isCollision(enemyX, enemyY, laserX, laserY):
    distance = math.sqrt((enemyX - laserX)**2 + (enemyY - laserY)**2)
    if distance < 27:
        return True
    else:
        return False

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
                    laser_sound = mixer.Sound('laser.wav')
                    laser_sound.play()
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
    for i in range(num_of_enemies):

        # game over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]
        
        collision = isCollision(enemyX[i], enemyY[i], laserX, laserY)
        if collision:
            laserY = 480
            laser_state = "ready"
            score_value += 8 + random.randint(0,4)
            enemyX[i] = random.randint(100,700)
            enemyY[i] = random.randint(50,150)
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
                    

        enemy(enemyX[i], enemyY[i], i)

    #laser move
    if laser_state is "fire":
        fire_laser(laserX, laserY)
        laserY -= laserY_change

    if laserY <= 0:
        laserY = 480
        laser_state = "ready"
    
    show_score(textX, textY)

    player(playerX, playerY) #player called after screen as player must be on top of screen.
    pygame.display.update()
